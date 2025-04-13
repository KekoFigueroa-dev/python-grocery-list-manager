# Initialize datetime module for tracking shopping session timestamp
import datetime

# Configure timestamp formatting for session tracking
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# Initialize default grocery list with starter items
# All items stored in title case for consistent display
grocery_list = ["Meat", "Cheese"]

# Display application header with current session timestamp
print("Welcome to the Grocery List App")
print(f"Current Date and Time: {month}/{day} {hour}:{minute}")
print(f"You currently have {grocery_list[0]} and {grocery_list[1]} in your list.")

# Collect additional grocery items from user input
# Convert all inputs to title case for consistent formatting
food = input("\nType of food to add to the grocery list: ")
grocery_list.append(food.title())
food = input("Type of food to add to the grocery list: ")
grocery_list.append(food.title())
food = input("Type of food to add to the grocery list: ")
grocery_list.append(food.title())

# Display both unsorted and alphabetically sorted list views
print("\nHere is your grocery list:")
print(grocery_list)
grocery_list.sort()
print("Here is your grocery list sorted:")
print(grocery_list)

# Begin shopping simulation sequence
print("\nSimulating grocery shopping...")
print(f"\nCurrent grocery list: {len(grocery_list)} items")
print(grocery_list)

# Process first item purchase and list update
buy_food = input("What food did you just buy: ").title()
grocery_list.remove(buy_food)
print(f"Removing {buy_food} from the list...")

# Process second item purchase and list update
print(f"\nCurrent grocery list: {len(grocery_list)} items")
print(grocery_list)
buy_food = input("What food did you just buy: ").title()
grocery_list.remove(buy_food)
print(f"Removing {buy_food} from the list...")

# Process third item purchase and list update
print(f"\nCurrent grocery list: {len(grocery_list)} items")
print(grocery_list)
buy_food = input("What food did you just buy: ").title()
grocery_list.remove(buy_food)
print(f"Removing {buy_food} from the list...")

# Handle inventory shortage scenario
# Remove unavailable item and get replacement choice
print(f"\nCurrent grocery list: {len(grocery_list)} items")
print(grocery_list)
no_item = grocery_list.pop()
print(f"\nSorry, the store is out of {no_item}.")
new_food = input("What food would you like instead: ").title()
grocery_list.insert(0, new_food)

# Display final list state
print("\nHere is what remains on your grocery list:")
print(grocery_list)
