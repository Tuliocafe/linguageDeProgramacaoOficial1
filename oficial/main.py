# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import csv


# read csv file as a list of lists
def read_csv():
    courses = []
    with open('cursos-prouni2.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            courses.append(row[0])

    return courses


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    courses_name = read_csv()
    print(courses_name)
    print(type(courses_name))

    # Coloca a lista em ordem alfabetica e remove as duplicatas
    cursos = sorted(set(courses_name))
    print(cursos)
    print(f'Foram cadastrados {len(cursos)} cursos')

    # Tambem fiz o codigo manual caso prefira ver como funciona em um for
    # cursos = []
    # courses_name.sort()

    # for c in range(1, len(courses_name)):
    #     if c == 1:
    #         cursos.append(courses_name[c])
    #     elif courses_name[c] != courses_name[c - 1]:
    #         cursos.append(courses_name[c])

    # print(cursos)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
