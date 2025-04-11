import json
from item import Item
from config import TYPES


DATA_FILE = "collection_data.json"
TYPES_FILE = "types.json"

def save_items():
    data = [item.to_dict() for item in Item.get_all_items()]
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

    with open(TYPES_FILE, "w", encoding="utf-8") as t:
        json.dump(TYPES,  t, indent=4)

def load_items():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            for d in data:
                type_name = d["type"]
                type_id = next((k for k, v in TYPES.items() if v == type_name), None)
                if type_id:
                    Item(
                        title=d["title"],
                        type_id=type_id,
                        date_added=d["date_added"],
                        date_made=d["date_made"],
                        description=d["description"]
                    )
    except FileNotFoundError:
        pass

def load_types():
    try:
        with open(TYPES_FILE, "r", encoding="utf-8") as t:
            loaded = json.load(t)
            TYPES.clear()
            for key, value in loaded.items():
                TYPES[int(key)] = value
    except FileNotFoundError:
        pass

