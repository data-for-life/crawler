import json
from datetime import datetime

def to_json(data, filename=None):
    if filename is None:
        filename = "data/" + datetime.strftime('%Y%m%d-%H%M%S') + ".json"
    with open(filename, "w+", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii = False)