import json
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

HIGHSCORE_FILE = DATA_DIR / "highscore.json"

def load_high_score():
    try:
        with open(HIGHSCORE_FILE, "r") as h:
            data = json.load(h)
            return data["high_score"]

    except FileNotFoundError:
        with open(HIGHSCORE_FILE, "w") as h:
            json.dump({"high_score": 0}, h)

        return 0

def save_high_score(score):
    high_score = load_high_score()

    if score > high_score:
        with open(HIGHSCORE_FILE, "w") as h:
            json.dump({"high_score": score}, h)
