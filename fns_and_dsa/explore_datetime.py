# explore_datetime.py
# You're now a time traveler!

from datetime import datetime, timedelta   # We need these two magic spells

# PART 1: Show the current date and time
def display_current_datetime():
    current_date = datetime.now()   # This gets the EXACT time right now!
    
    # Make it look pretty: 2025-11-26 14:30:25
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    
    print(f"Current date and time: {formatted_date}")

# PART 2: Travel to the future!
def calculate_future_date():
    # Ask how many days into the future
    days = int(input("Enter the number of days to add to the current date: "))
    
    current_date = datetime.now()           # Get today
    future_date = current_date + timedelta(days=days)  # MAGIC TIME TRAVEL!
    
    # Only show the date, no time
    nice_future = future_date.strftime("%Y-%m-%d")
    
    print(f"Future date: {nice_future}")

# RUN BOTH FUNCTIONS
print("Time Wizard Activated!")
display_current_datetime()
calculate_future_date()