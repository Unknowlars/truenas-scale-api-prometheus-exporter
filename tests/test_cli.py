import pytest

from truenas_exporter.cli import main
from truenas_exporter.version import __version__


def test_cli_version(capsys):
    with pytest.raises(SystemExit) as exc_info:
        main(["--version"])

    assert exc_info.value.code == 0
    assert capsys.readouterr().out.strip() == __version__
