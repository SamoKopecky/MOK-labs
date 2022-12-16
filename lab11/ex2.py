from typing import List

import numpy as np
import matplotlib.pyplot as plt

from ex1 import load_dataset


def statistics(data, langs: List[str]):
    """Extracts *nr* and *pc* datasets from dataset.
    :param data: Full dataset loaded using `load_dataset` function.
    :param langs: List of languages to extract.
    :return: Tuple of dictionaries representing *nr* and *pc* datasets
    """
    nr_data = data[data[:, 0] == "NR"]
    pc_data = data[data[:, 0] == "PC"]

    nr_dict, pc_dict = {}, {}

    for lang in langs:
        nr_dict[lang] = (
            nr_data[nr_data[:, 1] == lang, 4:].astype(np.float32).sum(axis=0)
        )
        pc_dict[lang] = (
            pc_data[pc_data[:, 1] == lang, 4:].astype(np.float32).sum(axis=0)
        )

    return nr_dict, pc_dict


def plot_bar(data, langs: List[str]):
    """Plots bar chart for year 2019 of provided dataset.
    :param data: Dictionary representing dataset, generated using `statistics` function.
    :param langs: List of languages to plot.
    """
    values = []

    for lang in langs:
        values.append(data[lang][0])

    plt.xticks(rotation=90)
    plt.bar(langs, values)
    plt.show()


def generalize(data):
    """Generalize value in a bigger category.
    :param data: Dictionary representing dataset, generated using `statistics` function.
    :return: Generalized dataset in same format as input dataset.
    """
    maxes = []
    mins = []
    for key, value in data.items():
        maxes.append(max(value))
        mins.append(min(value))

    high = 1000000
    low = 5000
    print(f"Low: {low}, high: {high}")
    new_data = data
    for key, value in data.items():
        average = sum(value) / len(value)
        for i in range(value.shape[0]):
            if average > high:
                new_data[key][i] = high
                continue
            elif average < low:
                new_data[key][i] = low
                continue
            else:
                new_data[key][i] = average
    return new_data


def main():
    ds = load_dataset()
    attrs = np.transpose(ds)
    langs = set(attrs[1])
    langs.remove("TOTAL")
    langs.remove("OTH")
    langs_list = list(langs)
    # print(set(attrs[3]))

    ds = np.array(list(filter(lambda row: row[1] != "TOTAL" and row[1] != "OTH", ds)))

    nr, _ = statistics(ds, langs_list)

    plot_bar(nr, langs_list)
    nr = generalize(nr)
    plot_bar(nr, langs_list)


if __name__ == "__main__":
    main()
