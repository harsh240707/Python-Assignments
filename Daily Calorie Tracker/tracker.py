print("=========================================")
print("         🍎 DAILY CALORIE TRACKER 🍎")
print("=========================================")
print("This tool allows you to record your meals and their calories.")
print("It will calculate your total and average calorie intake,")
print("and tell you whether you stayed within your daily calorie goal.\n")

meals = []
calories = []

meal_count = int(input("How many meals would you like to record today? "))

for i in range(meal_count):
    print(f"\nMeal {i+1} of {meal_count}")
    meal_name = input("Enter meal name (e.g., Breakfast, Lunch, Dinner ): ")
    meal_calories = float(input(f"Enter calories for {meal_name}: "))
    
    
    meals.append(meal_name)
    calories.append(meal_calories)

total_calories = sum(calories)

average_calories = total_calories / len(calories)

daily_limit = float(input("\nEnter your daily calorie limit: "))

print("\n=========================================")
print("            🧾 DAILY REPORT 🧾")
print("=========================================")

print("Meal Name\tCalories")
print("-----------------------------------------")

for i in range(len(meals)):
    print(f"{meals[i]:<15}\t{calories[i]}")

print("-----------------------------------------")

print(f"Total:\t\t{total_calories}")
print(f"Average:\t{average_calories:.2f}\n")

if total_calories > daily_limit:
    print("⚠️  Warning: You have exceeded your daily calorie limit!")
else:
    print("✅ Great job! You're within your daily calorie limit.")

save_option = input("\nWould you like to save this session? (yes/no): ").lower()

if save_option == "yes":

    with open("calorie_log.txt", "a") as file:
        file.write("------ Daily Calorie Tracker Log ------\n")
        for i in range(len(meals)):
            file.write(f"{meals[i]:<15}\t{calories[i]}\n")
        file.write("---------------------------------------\n")
        file.write(f"Total:\t{total_calories}\n")
        file.write(f"Average:\t{average_calories:.2f}\n")
        file.write(f"Daily Limit:\t{daily_limit}\n")

        if total_calories > daily_limit:
            file.write("Status: Exceeded Limit ⚠️\n")
        else:
            file.write("Status: Within Limit ✅\n")
        
        file.write("---------------------------------------\n\n")
    
    print("💾 Session saved successfully to 'calorie_log.txt'.")
else:
    print("Session not saved. Goodbye! 👋")


