import csv
from pprint import pprint
from typing import Dict

import numpy as np
from matplotlib import pyplot as plt


def load_dataset():
    # read data set by lines
    file = open("cleaned.csv", "r")
    csv_data = csv.reader(file)
    data = np.array([row for row in csv_data])
    file.close()
    return data


def plot_bar(data: dict):
    values = list(data.values())
    keys = list(data.keys())

    plt.xticks(rotation=90)
    plt.tick_params(axis="x", pad=-200)
    plt.bar(keys, values)
    plt.show()


def get_top_purchased_games(ds, top):
    ds = np.array(list(filter(lambda r: r[2] == "purchase", ds)))
    transposed = np.transpose(ds)
    games_count: dict[str, int] = {}
    for game in transposed[1]:
        if game in games_count.keys():
            games_count[game] += 1
        else:
            games_count[game] = 1
    sorted_games = {
        k: v
        for k, v in sorted(games_count.items(), key=lambda item: item[1], reverse=True)
    }
    vals = list(sorted_games.items())
    return dict(vals[:top])


def get_games_per_player(data):
    # Many more statistical functions can be created using this function
    purchased: Dict[str, Dict[str, bool]] = {}
    for row in data:
        if row[2] == "purchase":
            if row[0] in purchased.keys():
                purchased[row[0]].update({row[1]: False})
            else:
                purchased[row[0]] = {row[1]: False}
            continue
        elif row[2] == "play":
            if row[0] in purchased.keys():
                purchased[row[0]][row[1]] = True
    return purchased


def get_ratio_of_played_purchased_per_player(data):
    purchased = get_games_per_player(data)

    ratio: Dict[str, int] = {}
    for player_id, value in purchased.items():
        purchased = len(value)
        played = 0
        for _, played_game in value.items():
            if played_game:
                played += 1
        if played == 0 or purchased == 0:
            ratio[player_id] = 0
        ratio[player_id] = int((played / purchased) * 100)
    return sum(ratio.values()) / len(ratio)


def main():
    top = 20
    ds = load_dataset()
    average_play_rate = get_ratio_of_played_purchased_per_player(ds)
    print(
        f"On average a steam user plays {int(average_play_rate)}% of his purchased games"
    )
    top_games = get_top_purchased_games(ds, 20)
    print(f"Top {top} games:")
    pprint(top_games, sort_dicts=False)
    plot_bar(top_games)


if __name__ == "__main__":
    main()

# Source
# https://www.kaggle.com/datasets/tamber/steam-video-games
