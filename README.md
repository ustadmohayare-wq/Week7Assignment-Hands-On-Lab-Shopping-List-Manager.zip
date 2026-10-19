# Week 7 Assignment: Hands-On Lab — Shopping List Manager

## Files

- `list_warmup.py` - Demonstrates creating, adding, removing, and counting items in a list.
- `shopping_list.py` - Provides an interactive shopping list manager using a menu.
- `list_report.py` - Displays a numbered shopping list and finds the number of long item names and the longest item.

## Why is it safer to check in before calling `.remove()`?

It is safer to check if an item is in the list before using `.remove()` because `.remove()` causes an error if the item does not exist. Using `in` first prevents the program from crashing and allows us to display a helpful message instead.