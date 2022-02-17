# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from src.customer import Customer


def parse_input(file_name):
    # TODO: Parse input file with a dir
    f = open("a_an_example.in.txt", "r")
    # print the file into terminal
    loves = []
    dislikes = []

    f.readline()
    for index, value in enumerate(f):
        ingredient_list = value.rstrip()
        ingredient_list = ingredient_list.split(" ")[1:]

        if not index % 2:
            loves.append(ingredient_list)
        else:
            dislikes.append(ingredient_list)

    # Create instances of customer
    for current in range(len(loves)):
        cust1 = Customer(tuple(loves[current]), tuple(dislikes[current]))
        print(cust1)

    f.close()


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    parse_input("")
