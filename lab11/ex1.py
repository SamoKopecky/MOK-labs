import numpy as np


def load_dataset():
    # read data set by lines
    with open("edu.txt", "r") as file:
        lines = file.readlines()
    data = []
    for line in lines[1:]:
        data.append(line.replace(":", "0").split())
    return np.array(data)


def students_per_year(data, lang: str):
    """Count the total number of students per year.

    :param data: Data set loaded from 'edu.txt' file.
    :param lang: Language acronym (e.g. CZE).
    :return: List of students studying given language.
    """
    students = np.zeros(8)
    numbers = list(filter(lambda row: row[0] == "NR" and row[1] == lang, data))
    for student in numbers:
        for i in range(8):
            students[i] += float(student[i + 4])
    return np.array(students)


def main():
    ds = load_dataset()
    print(ds)

    attrs = np.transpose(ds)
    langs = set(attrs[1])
    langs.remove('TOTAL')
    langs.remove('OTH')
    langs_list = list(langs)
    print(langs_list)
    print(len(langs_list))
    students_per_year(ds, "CZE")


if __name__ == "__main__":
    main()
