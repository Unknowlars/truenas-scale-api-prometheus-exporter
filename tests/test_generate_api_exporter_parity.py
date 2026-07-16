from scripts.generate_api_exporter_parity import build_audit

# R08 regression test.
#
# Deliberately built from lowercase text and upper()'d at runtime, rather than
# spelling the metric variable/method name as literal uppercase/dotted
# substrings: the generator under test scans every file under tests/ for such
# substrings as fixture evidence, and a literal match here would pollute
# unrelated rows' evidence with this file's path (this happened during
# development of this test — see the R08 commit body for the two collisions
# it produced before this workaround).
_TARGET_VARIABLE = "pool_status_code".upper()


def _target_row():
    audit = build_audit()
    for row in audit["field_mappings"]:
        if row["variable"] == _TARGET_VARIABLE:
            return row
    raise AssertionError(f"{_TARGET_VARIABLE} row missing from field_mappings")


def test_zpool_status_code_row_cites_correct_evidence_and_note():
    """The parity row for the v26 zpool status-code gauge must not cite the
    unrelated 25.10 fixture for the plain (non-z) pool listing method (a
    substring-match artifact of one method name being contained in the
    other) and must explain the v26-only, profile-gated nature of the
    source instead of the generic "absent from the pinned method/event
    leaves" note.
    """
    row = _target_row()

    assert row["fixture_test"] == "tests/test_t21_low_cost_metrics.py"
    assert "pool_query.json" not in row["fixture_test"]

    expected_notes = (
        "v26-only " + "zpool".lower() + ".query, profile-gated via V26_ADDED_METHODS; "
        "absent on 25.10/unknown; status_code documented in the v26 corpus."
    )
    assert row["notes"] == expected_notes

    assert "undocumented/unavailable" not in row["documented_type_unit"]
    assert "docs/truenas-api-v26/methods/zpool/query.md" in row["documented_type_unit"]

    # Still correctly disposed as an actively producing, profile-gated metric.
    assert row["implementation_status"] == "active dedicated"
