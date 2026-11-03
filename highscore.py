import json

def load_high_score():
    with open("highscore.json") as h:
        data = json.load(h)
        return data["high_score"]

def save_high_score(score):
    high_score = load_high_score()

    if score > high_score:
        with open("highscore.json", "w") as h:
            json.dump({"high_score": score}, h)
