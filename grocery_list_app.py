# Import datetime library
import datetime
time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)
# Initialize grocery list with meat and cheese
grocery_list = ["meat","cheese"]
# Welcome message and current date/time display functions  # Format: mm/dd hh:mm
print("Welcome to my Grocery List App")
print(f"Current Date and time {month}/{day} {hour}:{minute}")
# Display current items in list
print(f"You currently have {grocery_list[0].title()} and {grocery_list[1].title()} in your list")

# Function to get three new items from user
# Remember to title case the input

# Display and sort the grocery list

# Shopping simulation
# - Show list length and current items
# - Get purchased item (case insensitive)
# - Remove items
# - Repeat 3 times

# Handle out of stock scenario
# - Remove last item
# - Get replacement
# - Add to beginning of list

# Display final list

