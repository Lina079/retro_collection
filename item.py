from __future__ import annotations
from typing import List
from config import TYPES

class Item:
    ITEMS: List[Item] = []

    def __init__(self, title: str, type_id: int, date_added: str, date_made: str, description: str):
        self.__id = Item.__get_next_id()
        self.title = title
        self.type_id = type_id
        self.date_added = date_added
        self.date_made = date_made
        self.description = description
        Item.ITEMS.append(self)

    @staticmethod
    def __get_next_id() -> int:
        return len(Item.ITEMS) + 1

    @property
    def id(self):
        return self.__id

    @property
    def type_name(self):
        return TYPES.get(self.type_id, "Unknown")

    def to_dict(self):
        return {
            "id": self.__id,
            "title": self.title,
            "type": self.type_name,
            "date_added": self.date_added,
            "date_made": self.date_made,
            "description": self.description
        }

    def update_field(self, field: str, new_value: str):
        if field == "title":
            self.title = new_value
        elif field == "type":
            try:
                type_id = int(new_value)
                if type_id in TYPES:
                    self.type_id = type_id
                else:
                    print("Invalid type.")
            except ValueError:
                print("Type must be a number.")
        elif field == "date_added":
            self.date_added = new_value
        elif field == "date_made":
            self.date_made = new_value
        elif field == "description":
            self.description = new_value
        else:
            print("Invalid field.")


    @staticmethod
    def get_all_by_type(type_id: int) -> List[Item]:
        return [item for item in Item.ITEMS if item.type_id == type_id]

    @staticmethod
    def get_all_items() -> List [Item]:
        return Item.ITEMS

    @staticmethod
    def delete_by_index(index: int):
        if 0<= index < len(Item.ITEMS):
            return Item.ITEMS.pop(index)
        else:
            return None

