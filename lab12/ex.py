from typing import List
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

col_labels = ["2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012"]
row_labels = [
    "ARA",
    "BUL",
    "CHI",
    "CZE",
    "DAN",
    "DUT",
    "ENG",
    "EST",
    "FIN",
    "FRE",
    "GER",
    "GLE",
    "GRE",
    "HRV",
    "HUN",
    "ITA",
    "JPN",
    "LAV",
    "LIT",
    "MLT",
    "POL",
    "POR",
    "RUM",
    "RUS",
    "SLO",
    "SLV",
    "SPA",
    "SWE",
    "UNK",
]

ndata = np.array(
    [
        [99342.4, 162120.4, 94356.0, 57324.0, 50720.0, 18121.0, 20058.0, 1288.0],
        [322.0, 534.0, 1021.0, 283.0, 236.0, 304.0, 288.0, 87.0],
        [317187.0, 647921.6, 305696.4, 204490.0, 173692.0, 68960.0, 61144.0, 1420.0],
        [3339.0, 4766.0, 3353.0, 1604.0, 1731.0, 1444.0, 1061.0, 1408.0],
        [33874.0, 35053.0, 36646.0, 32376.0, 33804.0, 33253.0, 35433.0, 170.0],
        [
            1380147.8,
            1661173.6,
            1371050.8,
            850248.0,
            864924.0,
            872040.0,
            873722.0,
            270.0,
        ],
        [
            137789111.3,
            193032555.9,
            193296416.2,
            127745453.0,
            126976072.2,
            126326901.6,
            125028454.2,
            18426947.4,
        ],
        [85601.0, 119546.0, 40628.0, 37723.0, 37890.0, 38329.0, 35063.0, 164.0],
        [126772.0, 167378.0, 127768.0, 50714.0, 51647.0, 54433.0, 56397.0, 262.0],
        [
            23911563.6,
            36789392.6,
            24811896.7,
            22532121.4,
            22575473.2,
            22871900.4,
            23566772.6,
            5305847.3,
        ],
        [
            18828985.6,
            26286194.7,
            19488778.2,
            17579553.0,
            17589724.0,
            17693847.0,
            17872219.0,
            1539510.0,
        ],
        [28.0, 0.0, 5261.9, 0.0, 0.0, 0.0, 0.0, 0.0],
        [6558.8, 6857.7, 6466.2, 1203.0, 1206.0, 1441.0, 743.0, 1189.0],
        [6232.0, 6443.0, 5762.0, 5177.0, 5678.0, 5494.0, 6248.0, 5627.0],
        [5134.0, 5250.0, 5016.0, 2193.0, 2421.0, 2628.0, 2639.0, 3168.0],
        [
            1874320.3,
            2571813.9,
            1953325.8,
            1600879.8,
            1613125.7,
            1626926.2,
            1649775.0,
            319678.6,
        ],
        [43162.2, 88751.6, 42350.4, 12900.0, 12126.0, 11120.0, 14509.0, 5342.0],
        [37.0, 21.0, 26.0, 10.0, 8.0, 10.0, 12.0, 26.0],
        [1007.0, 1379.0, 1075.0, 497.0, 468.0, 473.0, 505.0, 466.0],
        [0.0, 2026.0, 0.0, 0.0, 3344.0, 0.0, 0.0, 0.0],
        [31670.0, 36748.4, 30384.2, 12016.0, 2262.0, 1018.0, 1221.0, 318.0],
        [117839.2, 56606.6, 54823.1, 41507.0, 36728.0, 35486.0, 36175.0, 714.0],
        [4282.0, 5095.0, 4172.0, 1674.0, 1903.0, 1999.0, 2408.0, 1816.0],
        [
            2570495.9,
            3597773.9,
            2804998.6,
            2660693.2,
            2751853.0,
            2809613.0,
            2842094.0,
            287314.7,
        ],
        [90292.0, 129050.0, 90824.0, 44737.0, 45011.0, 45956.0, 47150.0, 1003.0],
        [12817.0, 16921.0, 14081.0, 6309.0, 3988.0, 3922.0, 3746.0, 10028.0],
        [
            18233292.2,
            25285087.1,
            17590493.4,
            14118243.6,
            13510404.6,
            12992869.6,
            12618636.2,
            1136378.4,
        ],
        [
            1396924.0,
            1758306.0,
            1345420.0,
            570200.0,
            589432.0,
            594255.0,
            608301.0,
            412.0,
        ],
        [536704.0, 721953.8, 396938.0, 482828.0, 458536.0, 487764.0, 473634.0, 3440.0],
    ]
)


def ex1(k: int, attr: "np.ndarray[np.float32]") -> "np.ndarray[np.float32]":
    """Anonymise attribute values using microaggregation.
    :param k: Number of elements in a cluster.
    :param attr: Values for given attribute.
    :return: Anonymised attribute.
    """
    result = attr.copy()
    sorted_attr = sorted(attr)
    for i in range(len(attr) // k):
        group = sorted_attr[i * k: (i + 1) * k]
        centroid = group[k // 2]
        for z in range(len(group)):
            for j in range(len(result)):
                if result[j] == group[z]:
                    result[j] = centroid
                    break
    return result


def ex2(k: int, dataset: "np.ndarray[np.float32]") -> "np.ndarray[np.float32]":
    """Anonymise dataset using microaggregation.
    :param k: Number of elements in a cluster.
    :param dataset: Dataset to be anonymised.
    :return: Anonymised dataset.
    """
    ds = dataset.transpose()
    a_ds = []
    for attr in ds:
        a_ds.append(ex1(k, attr))
    a_ds = np.array(a_ds)
    return a_ds.transpose()


def plot_table(
        data: "np.ndarray[np.float32]", row_labels: List[str], col_labels: List[str]
):
    """Plot dataset to table.
    :param data: Dataset to be plotted.
    :param row_labels: List of labels for each row in dataset.
    :param col_labels: List of labels for each column in dataset.
    """
    colors = plt.cm.BuPu(np.linspace(0, 0.5, len(data)))
    fig, ax = plt.subplots(1, 1)
    df = pd.DataFrame(data, columns=col_labels)
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(
        cellText=df.values,
        rowLabels=row_labels,
        rowColours=colors,
        colLabels=df.columns,
        fontsize=50,
        loc="center",
    )

    ax.axis("off")

    fig.canvas.draw()
    bbox = table.get_window_extent(fig.canvas.get_renderer())
    bbox_inches = bbox.transformed(fig.dpi_scale_trans.inverted())
    my_dpi = 96
    plt.figure(figsize=(800 / my_dpi, 800 / my_dpi), dpi=my_dpi)

    fig.savefig("table.png", bbox_inches=bbox_inches, dpi=my_dpi * 5)


def main():
    k = 4
    attribute = ndata.transpose()
    print(list(ex1(k, np.array(attribute[0]))))
    plot_table(ex2(k, ndata), row_labels, col_labels)


if __name__ == "__main__":
    main()
