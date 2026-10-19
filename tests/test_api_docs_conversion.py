"""Documentation conversion acceptance tests through the converter CLI."""

import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts/convert_truenas_api_docs_to_markdown.py"


def snapshot(tmp_path):
    source = tmp_path / "source"
    (source / "_sources").mkdir(parents=True)
    (source / "_sources/api_methods_system.rst.txt").write_text(
        "system\n======\n\n.. toctree::\n\n   api_methods_system.info\n"
    )
    (source / "_sources/api_methods_system.info.rst.txt").write_text(
        'system.info\n===========\n\nRead system information.\n\n.. raw:: html\n\n'
        '    <div id="json-schema"><div class="accordion"><div class="card">'
        '<div class="card-header"><span class="property-name">Return value</span></div>'
        '<div><div class="card-body"><span class="value-type">Type: object</span>'
        '<span class="description">See <a href="api_methods_system.html">system</a>.</span>'
        '</div></div></div></div></div>\n\n*Required roles:* READONLY_ADMIN | SYSTEM_READ\n'
    )
    for name in ("api_methods_system", "api_methods_system.info", "jsonrpc", "query_methods", "jobs", "rbac", "changelog"):
        (source / f"{name}.html").write_text(
            f'<div class="bodywrapper"><div class="body"><h1>{name}</h1>'
            '<p>See <a href="api_methods_system.info.html">system.info</a>.</p></div></div>'
        )
    return source


def run(source, output, *args):
    return subprocess.run(
        [sys.executable, str(SCRIPT), "--source", str(source), "--output", str(output), *args],
        capture_output=True, text=True, check=False,
    )


def test_invalid_snapshot_preserves_existing_output(tmp_path):
    source = tmp_path / "missing"
    source.mkdir()
    output = tmp_path / "output"
    output.mkdir()
    marker = output / "preserve.md"
    marker.write_text("existing documentation")
    result = run(source, output, "--clean")
    assert result.returncode != 0
    assert marker.read_text() == "existing documentation"


def test_versioned_conversion_is_deterministic_and_preserves_roles_links_and_provenance(tmp_path):
    source = snapshot(tmp_path)
    output = tmp_path / "output"
    args = ("--api-version", "27.0.0", "--source-url", "https://example.test/api/", "--retrieved-at", "2026-10-19")
    result = run(source, output, *args)
    assert result.returncode == 0, result.stderr
    page = (output / "methods/system/info.md").read_text()
    assert "- `READONLY_ADMIN`\n- `SYSTEM_READ`" in page
    assert "[system](index.md)" in page
    manifest = json.loads((output / "MANIFEST.json").read_text())
    assert manifest["truenas_version"] == "27.0.0"
    assert manifest["source_url"] == "https://example.test/api/"
    assert manifest["retrieved_at"] == "2026-10-19"
    assert len(manifest["source_files"]) == 9
    assert manifest["inventory"][0]["name"] == "system.info"
    assert manifest["inventory"][0]["required_roles"] == ["READONLY_ADMIN", "SYSTEM_READ"]
    assert (output / "authentication.md").is_file()
    before = {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
    assert run(source, output, *args, "--check").returncode == 0
    assert before == {p.relative_to(output): p.read_bytes() for p in output.rglob("*") if p.is_file()}
    (output / "README.md").write_text("out of date")
    assert run(source, output, *args, "--check").returncode != 0
    assert (output / "README.md").read_text() == "out of date"


def test_ambiguous_page_titles_and_missing_toctree_targets_do_not_replace_output(tmp_path):
    source = snapshot(tmp_path)
    output = tmp_path / "output"
    assert run(source, output).returncode == 0
    previous = (output / "README.md").read_text()
    duplicate = source / "_sources/api_methods_duplicate.rst.txt"
    duplicate.write_text((source / "_sources/api_methods_system.info.rst.txt").read_text())
    (source / "api_methods_duplicate.html").write_text("duplicate")
    assert "Duplicate output path" in run(source, output, "--clean").stderr
    assert (output / "README.md").read_text() == previous
    duplicate.unlink()
    (source / "_sources/api_methods_system.rst.txt").write_text("system\n======\n\n.. toctree::\n\n   api_methods_missing\n")
    assert "Missing toctree pages" in run(source, output, "--clean").stderr
    assert (output / "README.md").read_text() == previous


def test_schema_nesting_keeps_optional_fields_and_valid_markdown_headings(tmp_path):
    source = snapshot(tmp_path)
    page = source / "_sources/api_methods_system.info.rst.txt"
    text = page.read_text()
    nested = '<div class="accordion"><div class="card"><div class="card-header"><span class="property-name">optional</span></div><div><div class="card-body">INNER</div></div></div></div>'
    schema = '<span class="value-type">Type: string</span>'
    for _ in range(9):
        schema = nested.replace("INNER", schema)
    page.write_text(text.replace('<span class="value-type">Type: object</span>', schema))
    output = tmp_path / "output"
    assert run(source, output).returncode == 0
    markdown = (output / "methods/system/info.md").read_text()
    assert "Type: string" in markdown
    assert "#######" not in markdown
    assert "optional (required)" not in markdown


def test_archive_conversion_rejects_traversal_and_pins_original_archive_digest(tmp_path):
    import hashlib
    from zipfile import ZipFile

    source = snapshot(tmp_path)
    archive = tmp_path / "docs.zip"
    output = tmp_path / "output"
    with ZipFile(archive, "w") as bundle:
        for path in source.rglob("*"):
            if path.is_file():
                bundle.write(path, path.relative_to(source))
    args = ("--archive", str(archive), "--api-version", "27.0.0", "--source-url", "https://example.test/api/", "--retrieved-at", "2026-10-19")
    result = run(source, output, *args)
    assert result.returncode == 0, result.stderr
    manifest = json.loads((output / "MANIFEST.json").read_text())
    assert manifest["archive_sha256"] == hashlib.sha256(archive.read_bytes()).hexdigest()
    assert "docs.zip" in (output / "README.md").read_text()
    with ZipFile(archive, "a") as bundle:
        bundle.writestr("../escape.txt", "unsafe")
    result = run(source, output, *args, "--clean")
    assert result.returncode != 0
    assert not (tmp_path / "escape.txt").exists()
    assert (output / "MANIFEST.json").is_file()


def test_one_of_authentication_branches_are_not_truncated(tmp_path):
    source = snapshot(tmp_path)
    page = source / "_sources/api_methods_system.info.rst.txt"
    text = page.read_text()
    choice = ('<div class="one-of-value"><ul class="nav"><li><a class="nav-link">API key</a></li>'
              '<li><a class="nav-link">Password</a></li></ul><div class="tab-content">'
              '<div class="tab-pane"><span class="description">API_KEY_PLAIN</span></div>'
              '<div class="tab-pane"><span class="description">PASSWORD_PLAIN</span></div></div></div>')
    page.write_text(text.replace('<span class="value-type">Type: object</span>', choice))
    output = tmp_path / "output"
    assert run(source, output).returncode == 0
    markdown = (output / "methods/system/info.md").read_text()
    assert "One of" in markdown
    assert "API_KEY_PLAIN" in markdown
    assert "PASSWORD_PLAIN" in markdown


def test_schema_enum_const_and_pattern_constraints_are_preserved(tmp_path):
    source = snapshot(tmp_path)
    page = source / "_sources/api_methods_system.info.rst.txt"
    constraint = ('<span class="const-value">Specific value: <code>"SUCCESS"</code></span>'
                  '<span class="pattern-value">Must match regular expression: <code>^ok$</code></span>'
                  '<div class="enum-value"><h5>Must be one of:</h5>'
                  '<ul><li>"RUNNING"</li><li>"STOPPED"</li></ul></div>')
    page.write_text(page.read_text().replace('<span class="value-type">Type: object</span>', constraint))
    output = tmp_path / "output"
    assert run(source, output).returncode == 0
    markdown = (output / "methods/system/info.md").read_text()
    for expected in ('"SUCCESS"', '^ok$', '"RUNNING"', '"STOPPED"'):
        assert expected in markdown


def test_explicit_version_rejects_a_different_served_documentation_version(tmp_path):
    source = snapshot(tmp_path)
    (source / "index.html").write_text("<title>TrueNAS API v26.0.0 documentation</title>")
    output = tmp_path / "output"
    result = run(source, output, "--api-version", "27.0.0", "--source-url", "https://example.test/", "--retrieved-at", "2026-10-19")
    assert result.returncode != 0
    assert "version" in result.stderr.lower()
    assert not output.exists()


def test_shared_guides_preserve_captioned_rpc_examples(tmp_path):
    source = snapshot(tmp_path)
    (source / "jsonrpc.html").write_text(
        '<div class="bodywrapper"><div class="body"><h1>JSON-RPC</h1>'
        '<div class="literal-block-wrapper docutils container" id="subscribe-example">'
        '<div class="code-block-caption"><span class="caption-text">Subscribe example</span></div>'
        '<div class="highlight-json notranslate"><div class="highlight"><pre>'
        '{"method": "core.subscribe", "params": ["alert.list"]}'
        '</pre></div></div></div></div></div>'
    )
    output = tmp_path / "output"
    assert run(source, output).returncode == 0
    markdown = (output / "shared/jsonrpc.md").read_text()
    assert "Subscribe example" in markdown
    assert '"core.subscribe"' in markdown
    assert '"alert.list"' in markdown


def test_rst_upload_reference_targets_the_jobs_guide_and_retains_its_anchor(tmp_path):
    source = snapshot(tmp_path)
    page = source / "_sources/api_methods_system.info.rst.txt"
    page.write_text(page.read_text().replace("Read system information.", "See :ref:`uploading-files`."))
    (source / "jobs.html").write_text('<div class="bodywrapper"><div class="body"><span id="uploading-files"></span><h1>Uploads</h1></div></div>')
    output = tmp_path / "output"
    result = run(source, output, "--api-version", "27.0.0", "--source-url", "https://example.test/api/", "--retrieved-at", "2026-10-19")
    assert result.returncode == 0, result.stderr
    assert "[uploading-files](../../shared/jobs.md#uploading-files)" in (output / "methods/system/info.md").read_text()
    assert 'id="uploading-files"' in (output / "shared/jobs.md").read_text()
