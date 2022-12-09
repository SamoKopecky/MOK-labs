from typing import List

import numpy as np
import matplotlib.pyplot as plt

from ex1 import load_dataset


def statistics(
        data: np.ndarray[str], langs: List[str]
) -> tuple[dict[str, np.ndarray[np.float32]], dict[str, np.ndarray[np.float32]]]:
    """Extracts *nr* and *pc* datasets from dataset.

    :param data: Full dataset loaded using `load_dataset` function.
    :param langs: List of languages to extract.
    :return: Tuple of dictionaries representing *nr* and *pc* datasets
    """
    nr_data: np.ndarray[str] = data[data[:, 0] == "NR"]
    pc_data: np.ndarray[str] = data[data[:, 0] == "PC"]

    nr_dict, pc_dict = {}, {}

    for lang in langs:
        nr_dict[lang] = (
            nr_data[nr_data[:, 1] == lang, 4:].astype(np.float32).sum(axis=0)
        )
        pc_dict[lang] = (
            pc_data[pc_data[:, 1] == lang, 4:].astype(np.float32).sum(axis=0)
        )

    return nr_dict, pc_dict


def plot_bar(data: dict[str, np.ndarray[np.float32]], langs: List[str]):
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


def main():
    ds = load_dataset()
    attrs = np.transpose(ds)
    langs = set(attrs[1])
    langs.remove('TOTAL')
    langs.remove('OTH')
    langs_list = list(langs)

    ds = np.array(list(filter(lambda row: row[1] != "TOTAL" and row[1] != "OTH", ds)))
    print("test")
    nr, pc = statistics(ds, langs_list)
    plot_bar(nr, langs_list)


if __name__ == "__main__":
    main()
