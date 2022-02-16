# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def parse_input(file_name):
    # open file
    f = open("a_an_example.in.txt", "r")
    # print the file into terminal
    loves = []
    dislikes = []

    f.readline()
    for index, value in enumerate(f):
        ingredient_list = value.split(" ")
        ingredient_list[-1] = ingredient_list[-1].rstrip()
        if not index % 2:
            loves.append(ingredient_list)
        else:
            dislikes.append(ingredient_list)

    # Create instances of customer
    for customer in loves:

    print(loves)
    print(dislikes)

    # close file
    f.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    parse_input("")
