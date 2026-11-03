import json
from pathlib import Path

HIGHSCORE_FILE = Path(__file__).resolve().parent / "data" / "highscore.json"


def load_high_score() -> int:
    """Devuelve el récord guardado, o 0 si no existe o no es válido."""
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            value = json.load(f)["high_score"]
    except (OSError, ValueError, KeyError, TypeError):
        return 0

    if type(value) is int and value >= 0:
        return value
    return 0


def save_high_score(score: int) -> None:
    """Guarda el score solo si supera al récord actual."""
    if score <= load_high_score():
        return

    try:
        HIGHSCORE_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(HIGHSCORE_FILE, "w") as f:
            json.dump({"high_score": score}, f)
    except OSError as e:
        print(f"No se pudo guardar el récord: {e}")