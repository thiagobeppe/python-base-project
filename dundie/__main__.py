import argparse


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


def load(filepath: str):
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError:
        print(f"This filepath is invalid: {filepath}")
if __name__ == "__main__":
    main()
