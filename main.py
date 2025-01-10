from fpgrowth_py import fpgrowth
import os
import pandas as pd
import pickle


PLAYLISTS_DATASET_PATH = os.getenv("PLAYLISTS_DATASET_PATH", "/app/data/2023_spotify_ds1.csv")
MODEL_SAVE_PATH = os.getenv("MODEL_SAVE_PATH", "/app/data/playlists_rules.pkl")


def get_playlists_data() -> list[list[str]]:
    print("Reading playlists data...")
    data = pd.read_csv(PLAYLISTS_DATASET_PATH)
    data = data.dropna()
    data = data.drop_duplicates()


    playlists = data.groupby('pid')['track_name'].apply(list).reset_index(name='playlist')

    playlists = playlists['playlist'].tolist()

    return playlists


def get_frequent_itemsets(playlists: list[list[str]]) -> list[list]:
    print("Generating frequent playlists itemsets...")

    _, rules = fpgrowth(playlists, minSupRatio=0.05, minConf=0.1)

    return rules


def format_rules(rules: list[list]) -> dict[str, set[str]]:
    print("Formatting playlists rules...")
    formatted_rules = {}

    for rule in rules:
        for song in rule[0]:
            song = song.lower()
            if song not in formatted_rules:
                formatted_rules[song] = set()

            for recommended_song in rule[1]:
                formatted_rules[song].add(recommended_song.lower())

    return formatted_rules


def save_frequent_itemsets(rules: dict[str, set[str]]):
    print("Saving playlists rules...")
    with open(MODEL_SAVE_PATH, 'wb') as f:
        pickle.dump(rules, f)


def generate_playlists_rules():
    playlists = get_playlists_data()

    rules = get_frequent_itemsets(playlists)

    rules = format_rules(rules)

    save_frequent_itemsets(rules)


if __name__ == '__main__':
    print("Generating playlists rules...")

    generate_playlists_rules()
