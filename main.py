import os

def parse(filename):
    with open(filename) as f:  # opening a file
        lines = f.readlines()  # creating an array called lines with lines in that mf
    print(lines)
    




if __name__ == '__main__':
    parse('sample_output.out')


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
