def load(filepath: str):
    try:
        with open(filepath) as file_:
            for line in file_:
                print(line)
    except FileNotFoundError:
        print(f"This filepath is invalid: {filepath}")
