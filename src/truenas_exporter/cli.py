"""Command-line entry point."""

import argparse
from collections.abc import Sequence

from .runtime import main as _runtime_main
from .version import __version__


def main(argv: Sequence[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="TrueNAS SCALE Prometheus exporter")
    parser.add_argument("--version", action="version", version=__version__)
    parser.parse_args(argv)
    _runtime_main()


if __name__ == "__main__":
    main()
