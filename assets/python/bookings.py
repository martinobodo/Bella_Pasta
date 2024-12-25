import calendar
from datetime import datetime, time

# Constants for restaurant operation
OPENING_HOURS = (18, 23)  # 6 PM to 11 PM (24-hour format)
DAYS_OPEN = ["Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Booking data structure
bookings = {}

# Function to check if the restaurant is open on a given date and time
def is_restaurant_open(date, booking_time):
    weekday_name = calendar.day_name[date.weekday()]
    if weekday_name not in DAYS_OPEN:
        return False

    opening_time = time(OPENING_HOURS[0], 0)
    closing_time = time(OPENING_HOURS[1], 0)
    return opening_time <= booking_time <= closing_time

# Function to display a calendar for a given month and year
def display_calendar(year, month):
    print(calendar.month(year, month))

# Function to make a booking
def make_booking():
    try:
        # Get the booking date from the user
        date_input = input("Enter the booking date (YYYY-MM-DD): ")
        booking_date = datetime.strptime(date_input, "%Y-%m-%d").date()
        
        # Get the booking time from the user
        time_input = input("Enter the booking time (HH:MM): ")
        booking_time = datetime.strptime(time_input, "%H:%M").time()

        # Check if the restaurant is open
        if not is_restaurant_open(booking_date, booking_time):
            print("Sorry, the restaurant is closed at this time.")
            return

        # Check if the date already has bookings
        if booking_date not in bookings:
            bookings[booking_date] = []

        # Limit the number of bookings per time slot (example: 5 tables per slot)
        max_tables = 5
        time_slot_bookings = [b for b in bookings[booking_date] if b == booking_time]
        if len(time_slot_bookings) >= max_tables:
            print("Sorry, all tables are booked for this time slot.")
            return

        # Add the booking
        bookings[booking_date].append(booking_time)
        print(f"Booking confirmed for {booking_date} at {booking_time}.")
    except ValueError:
        print("Invalid date or time format. Please try again.")

# Function to view all bookings
def view_bookings():
    if not bookings:
        print("No bookings available.")
        return

    for date, times in bookings.items():
        print(f"Date: {date}")
        for booking_time in times:
            print(f"  - Time: {booking_time}")

# Main menu for the app
def main_menu():
    while True:
        print("\nRestaurant Booking App")
        print("1. View calendar")
        print("2. Make a booking")
        print("3. View all bookings")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            # View calendar
            year = int(input("Enter the year: "))
            month = int(input("Enter the month (1-12): "))
            display_calendar(year, month)
        elif choice == "2":
            # Make a booking
            make_booking()
        elif choice == "3":
            # View bookings
            view_bookings()
        elif choice == "4":
            # Exit the app
            print("Thank you for using the Restaurant Booking App!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main_menu()