# ------------------------------------------------------------
# Project Title : Daily Calorie Tracker
# Author        : Harsh Yadav
# Date          : 13-11-2025
# Description   :
#   This simple Python program helps you record meals and 
#   their calories, calculate total and average intake, 
#   compare it with a daily limit, and optionally save logs.
# ------------------------------------------------------------

from datetime import datetime

def show_menu():
    print("\n--------------------------------------------")
    print("        DAILY CALORIE TRACKER")
    print("--------------------------------------------")
    print("1. Start calorie tracker")
    print("2. View saved logs")
    print("3. Exit\n")

def get_float(prompt):
    """A small function to handle numeric input safely"""
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Calories can't be negative, try again.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

def log_meals():
    meals = []
    calories = []

    try:
        n = int(input("How many meals would you like to record today? "))
    except ValueError:
        print("Please enter a valid number of meals.")
        return

    for i in range(n):
        print(f"\nMeal {i+1} of {n}")
        name = input("Enter meal name (e.g., Breakfast, Lunch, Snack): ").strip()
        cal = get_float(f"Enter calories for {name}: ")
        meals.append(name)
        calories.append(cal)

    daily_limit = get_float("\nEnter your daily calorie limit: ")
    total = sum(calories)
    average = total / len(calories)

    print("\n---------------- DAILY REPORT ----------------")
    print(f"{'Meal Name':<15} Calories")
    print("----------------------------------------------")
    for i in range(len(meals)):
        print(f"{meals[i]:<15} {calories[i]}")
    print("----------------------------------------------")
    print(f"Total:   {total}")
    print(f"Average: {average:.2f}\n")

    if total > daily_limit:
        print("⚠️  You have exceeded your daily calorie limit.")
    else:
        print("✅ You are within your daily calorie limit!")

    # Ask user if they want to save
    choice = input("\nSave this record to file? (yes/no): ").lower()
    if choice == "yes":
        save_log(meals, calories, total, average, daily_limit)
    else:
        print("Record not saved.\n")

def save_log(meals, calories, total, average, daily_limit):
    with open("calorie_log.txt", "a") as f:
        f.write("---- Daily Calorie Tracker Log ----\n")
        f.write(f"Date & Time: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}\n")
        for i in range(len(meals)):
            f.write(f"{meals[i]:<15} {calories[i]}\n")
        f.write("-----------------------------------\n")
        f.write(f"Total: {total}\n")
        f.write(f"Average: {average:.2f}\n")
        f.write(f"Daily Limit: {daily_limit}\n")
        if total > daily_limit:
            f.write("Status: Exceeded Limit ⚠️\n")
        else:
            f.write("Status: Within Limit ✅\n")
        f.write("-----------------------------------\n\n")
    print("Data saved successfully to calorie_log.txt\n")

def view_logs():
    try:
        with open("calorie_log.txt", "r") as f:
            data = f.read()
            if data.strip() == "":
                print("\nNo logs found yet.\n")
            else:
                print("\n----------- SAVED LOGS -----------")
                print(data)
    except FileNotFoundError:
        print("\nNo log file found. Try saving a session first.\n")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == "1":
            log_meals()
        elif choice == "2":
            view_logs()
        elif choice == "3":
            print("\nThank you for using the Calorie Tracker. Goodbye!\n")
            break
        else:
            print("Invalid choice, please try again.\n")

if __name__ == "__main__":
    main()
