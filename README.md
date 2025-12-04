# **🍎 DAILY CALORIE TRACKER – PYTHON CLI PROJECT**

## **📌 Overview**
The **Daily Calorie Tracker** is a Python-based command line application that enables users to record their daily meals and calorie intake. The program calculates the **total** and **average** calories for the day, compares them with the user’s **daily calorie limit**, and provides a structured summary along with an option to save the session into a text file.

This project is ideal for Python beginners and academic mini-projects, providing practical experience with real-world logic, list manipulation, loops, conditional statements, formatted printing, and file handling.

---

## **🎯 Key Features**
- **Record multiple meals** along with individual calorie values
- **Automatically calculates** total and average calories
- **Checks calorie goal status** (Within Limit / Exceeded)
- **Formatted output table** for better readability
- **Save history** into `calorie_log.txt` for future reference
- **Beginner-friendly architecture** and clean understandable code

---

## **🧠 Concepts & Topics Covered**
| **Python Concept** | **Usage in Program** |
|--------------------|----------------------|
| `input()` | Taking user meal data |
| `for` loop | Repeated meal entry process |
| `lists` | Storing meals and calorie values |
| `sum()` | Calculating total calories |
| Mathematical average formula | Compute per-meal average |
| `if-else` | Decision making (limit exceeded or not) |
| `with open("file", "a")` | File handling & saving logs |
| f-string formatting | Clean structured output |
| CLI interface | Interaction through terminal |

---

## **🧾 Example Output**
=========================================
🍎 DAILY CALORIE TRACKER 🍎
This tool allows you to record your meals and their calories.

Meal Name Calories
Breakfast 340
Lunch 480
Snacks 120
Total: 940
Average: 313.33
⚠️ Warning: You have exceeded your daily calorie limit!
<img width="1390" height="942" alt="Screenshot 2025-12-04 120155" src="https://github.com/user-attachments/assets/c7768aa6-9dd6-4b50-a125-aee8a4fd490f" />


## **📁 File Structure**
Daily-Calorie-Tracker/
│
├── calorie_tracker.py # Main application code
├── calorie_log.txt # Generated history file
└── README.md # Documentation file

yaml
## **▶ How to Run**
### **Requirements**
- Python 3.x installed
- Any terminal (CMD, PowerShell, VS Code terminal, Linux shell, etc.)

### **Run Command**
```
python calorie_tracker.py

---

## **▶ How to Run**
### **Requirements**
- Python 3.x installed
- Any terminal (CMD, PowerShell, VS Code terminal, Linux shell, etc.)

### **Run Command**

python calorie_tracker.py```
📥 Log File Format (Saved Session Example)
markdown
Copy code
------ Daily Calorie Tracker Log ------
Breakfast       340
Lunch           480
Snacks          120
---------------------------------------
Total: 940
Average: 313.33
Daily Limit: 800
Status: Exceeded Limit ⚠️
---------------------------------------
```
🔧 Future Enhancements
* Feature	Improvement Idea
* Add date/time auto entry	Attach timestamp to log
* Weekly/Monthly report	Stats from stored data
* Graph visualization	Plot calories using matplotlib
* GUI Version	Tkinter / Kivy interface
* Export CSV & Excel	Use pandas
* User profile login	Separate logs per user

🎯 Learning Outcomes
* By building this project, users understand:
* Python basics to intermediate level concepts
* Developing an interactive CLI tool
* Handling real-world input validation & reporting
* File management & persistent storage
* Structured formatting for user interface

markdown
1. Fork this repository
2. Create a new branch
3. Commit changes
4. Submit a pull request
📜 License
This project is free to use and modify for personal or educational purposes.

👤 Author
   Harsh Yadav
