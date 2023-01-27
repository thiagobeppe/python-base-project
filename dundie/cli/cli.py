import argparse

from ..core import load


def main():
    parser = argparse.ArgumentParser(
        description="Dunder Mifflin Rewards CLI",
        epilog= "Enjoy and use with cautious.",
    )
    parser.add_argument(
        "subcommand",
        type=str,
        help="The subcommand to show",
        choices=["load","show", "send"],
        default="help",

    )
    parser.add_argument(
        "filepath",
        type=str,
        help= "Path to load a file",
    )

    args = parser.parse_args()

    try:
        globals()[args.subcommand](args.filepath)
    except KeyError:
        print("Subcommand is invalid")