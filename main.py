# for file management:
from pathlib import Path

from src.customer import Customer


def parse_input(dir):
    # ! Shadows built-in name 'dir'

    working_dir: Path = Path.cwd()

    # warn the user that data is empty/does not exist
    target_dir = working_dir / dir
    if not target_dir.is_dir():
        print("You are missing a data folder in this directory.")

    # ? What's the point of this block of code?
    valid_files: int = 0
    for file in target_dir.iterdir():
        if file.suffix == ".txt":
            pass
            # print(file)
            # valid_files += 1

    input_letter = input("Enter the file you want to use's corresponding letter\n")
    while True:
        if input_letter == "exit":
            exit()

        # ? Use strings.ascii_lowercase or ord instead?
        if input_letter in char_range("a", "e"):
            # stop iterating at input_letter
            for file in target_dir.iterdir():
                # ? Use file.endswith / file.startswith instead?
                if file.suffix == ".txt" and file.name[0] == input_letter:
                    print(file.name)
                    # ? Perhaps return a path if found instead?
                    extract_customer_preferences(target_dir / file.name)
            break
        input_letter = input("Enter a letter in the range 'a' to 'e' or exit.\n")


def extract_customer_preferences(path):
    # f = open("a_an_example.in.txt", "r")
    # print the file into terminal
    loves = []
    dislikes = []

    with open(path, mode="r") as f:
        f.readline()
        for index, value in enumerate(f):
            ingredient_list = value.rstrip()
            # ? Not needed to specify what to split here?
            ingredient_list = ingredient_list.split(" ")[1:]

            if not index % 2:
                loves.append(ingredient_list)
            else:
                dislikes.append(ingredient_list)

        # Create instances of customer
        for current in range(len(loves)):
            # ? I've modified the params' requirements to be more flexible, so you don't have to change to tuple
            cust1 = Customer(tuple(loves[current]), tuple(dislikes[current]))
            print(cust1)


def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    parse_input("data")
