import datetime
import tkinter as tk
from tkinter import messagebox

# Collect friends' birthdates
birthdays = {
    'Anna': '06/22',
    'John': '09/15',
    'Maria': '09/10'
    # Add more friends here
}

# Function to check today's date against birthdates
def check_birthdays(birthdays):
    today = datetime.datetime.now().strftime("%m/%d")
    for name, date in birthdays.items():
        if date == today:
            return name, date
    return None, None

# Function to show popup using tkinter
def show_popup(name, date):
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Birthday Reminder", f"Today {date} is {name}'s birthday!")
    root.destroy()

# Main function
def main():
    name, date = check_birthdays(birthdays)
    if name:
        show_popup(name, date)

if __name__ == "__main__":
    main()

