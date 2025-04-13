# Python Grocery List App

A basic command-line grocery list simulator that maintains a fixed shopping workflow. The app demonstrates fundamental list operations in Python.

## Features
- Session timestamp display (mm/dd hh:mm)
- Fixed starting list with two items (Meat, Cheese)
- Addition of exactly three user-defined items
- Basic list display and alphabetical sorting
- Simulated shopping for three items
- Simple out-of-stock replacement for final item

## Requirements
- Python 3.x
- datetime module (standard library)

## Program Flow
1. Displays timestamp and initial two items
2. User adds exactly three items
3. Shows original and sorted list
4. User "purchases" three items sequentially
5. Replaces final item due to "out of stock"

## Usage
```
python grocery_list_app.py
```

Follow the prompts to add items, simulate purchases, and handle the final replacement.

## Notes
- All items are automatically converted to title case
- Shopping simulation removes exactly three items
- Final item is always marked as "out of stock"
- Replacement item is added to the start of the list
