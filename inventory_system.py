""" Inventory System Module
Provides inventory management functionality to add, remove, save, load items
with quantity."""

import json
from datetime import datetime
import logging

# Global variable
stock_data = {}
logger = logging.getLogger(__name__)


def add_item(item="default", qty=0, logs=None):
    """Add or update an item in the inventory
    args:   item(str) - item to be added
            qty(int) - quantity to add
            logs(list) - list to store log entries"""

    if not isinstance(item, str) or not isinstance(qty, int):
        logger.warning("Invalid input types for add_item: item=%s, qty=%s",
                       item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    msg = f"{datetime.now()}: Added {qty} of {item}"
    logger.info("%s", msg)
    if logs is not None:
        logs.append(msg)


def remove_item(item, qty):
    """Remove an item by quantity qty from the inventory
    args:   item(str) - item to be removed
            qty(int) - quantity to remove"""
    if not isinstance(item, str) or not isinstance(qty, int):
        logger.warning("Invalid input types for remove_item: item=%s, qty=%s",
                       item, qty)
        return
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logger.info("Item '%s' removed completely from inventory.", item)
        else:
            logger.info("Removed %s of '%s'. Remaining: %s",
                        qty, item, stock_data[item])
    except KeyError as e:
        logger.error("Attempted to remove non-existent item: '%s'", item)
        print(f"an exception {e} has occured : check if item exists")
    except TypeError as e:
        logger.error("Type error while removing item '%s': %s", item, e)
        print(f"an exception {e} has occured : check if item exists")


def get_qty(item):
    """Retrieve quantity of a given item
    args: item(str) - item's name
    returns: int - item's quantity or 0 if not found"""
    if not isinstance(item, str):
        logger.warning("Invalid item type in get_qty: item=%s", item)
        return 0
    return stock_data.get(item, 0)


def load_data(file="inventory.json"):
    """Load inventory from json file
    args: file(str) - path to json file"""
    try:
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            logger.info("Inventory loaded from %s.", file)
            return data
    except FileNotFoundError:
        logger.warning("File not found: %s", file)
        return {}
    except json.JSONDecodeError as e:
        logger.error("Error decoding JSON from %s: %s", file, e)
        return {}


def save_data(file="inventory.json"):
    """Save current data to a JSON file
    args: file(str) - path to the file where data will be saved"""
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(stock_data, f, indent=2)
        logger.info("Inventory saved to %s.", file)
    except OSError as e:
        logger.error("Error saving inventory to %s: %s", file, e)


def print_data():
    """Print the full inventory"""
    print("Items Report")
    logger.info("Generate inventory report")
    for item, qty in stock_data.items():
        print(item, "->", qty)


def check_low_items(threshold=5):
    """Return list of items below quantity threshold
    args: threshold(int) - minimum quantity
    returns: list of items with low stock"""
    if not isinstance(threshold, int):
        logger.warning("Invalid threshold type: %s", threshold)
        return []
    result = []
    for item, qty in stock_data.items():
        if qty < threshold:
            result.append(item)
    logger.info("Items below threshold (%s): %s", threshold, result)
    return result


def main():
    """Main to demonstrate inventory options"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filename="inventory.log",
        filemode="a",
    )
    add_item("apple", 10)
    add_item("banana", -2)
    add_item(123, "ten")  # invalid types, no check
    remove_item("apple", 3)
    remove_item("orange", 1)
    print("Apple stock:", get_qty("apple"))
    print("Low items:", check_low_items())
    save_data()
    loaded_data = load_data()
    stock_data.clear()
    stock_data.update(loaded_data)
    print_data()
    str("print('eval used')")  # dangerous


main()
