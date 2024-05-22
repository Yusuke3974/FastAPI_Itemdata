from typing import List, Optional
from enum import Enum
from schemas import ItemCreate, ItemUpdate, ItemStatus


class Item:
    def  __init__(
        self,
        id: int,
        name: str,
        price:int,
        description:Optional[str],
        status: ItemStatus
    ):
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.status = status

items = [
    Item(id=1, name="Item 1", price=100, description="Item 1 description", status=ItemStatus.ON_SALE),
    Item(id=2, name="Item 2", price=200, description="Item 2 description", status=ItemStatus.SOLD_OUT),
    Item(id=3, name="Item 3", price=300, description="Item 3 description", status=ItemStatus.ON_SALE),
]

def get_all_items():
    return items


def get_item_by_id(id: int):
    for item in items:
        if item.id == id:
            return item
    return None

def find_by_name(name: str):
    filtered_items = []
    for item in items:
        if name in item.name:
            filtered_items.append(item)
    return filtered_items

def create_item(item_create: ItemCreate):
    new_item = Item(
        len(items) + 1,
        item_create.name,
        item_create.price,
        item_create.description,
        ItemStatus.ON_SALE
    )
    items.append(new_item)
    return new_item

def update_item(id: int, item_update: ItemUpdate):
    for item in items:
        if item.id == id:
            item.name = item.name if item_update.name is None else item_update.name
            item.price = item.price if item_update.price is None else item_update.price
            item.description = item.description if item_update.description is None else item_update.description
            item.status = item.status if item_update.status is None else item_update.status
            return item
    return None

def delete_item(id: int):
    for i in range(len(items)):
        if item[i] == id:
            delete_item = items.pop(i)
            return delete_item
    return None