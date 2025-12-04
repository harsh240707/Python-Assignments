🍎 Daily Calorie Tracker — Python CLI Project
🧾 Track your meals, calories, and stay within your daily health goals

📌 Project Overview
The Daily Calorie Tracker is a simple and efficient Python-based command-line tool designed to help users monitor their daily calorie intake. The tool allows users to enter meals and their calorie amounts, calculates total and average calories, compares them with a daily calorie target, and optionally saves the session history into a log file for later review.

This project is perfect for:

Python beginners learning input/output, loops & file handling

Students building academic mini projects

Anyone wanting a lightweight calorie tracking tool

🎯 Features
✔ Key Functionalities

Add multiple meals in a day

Automatically calculate total & average calories

Check whether you exceeded or stayed within your daily calorie limit

Save session summary to calorie_log.txt

Clean, user-friendly formatted terminal layout

Real-world practical utility

🧠 Concepts Used (Topics Covered)
Concept	Use in Program
input()	Taking user entries
for loop	Repeated meal entry
list	Stores meal names and calories
sum()	Calculates total calories
Mathematical average formula	Average calories/day
if-else conditions	Compare with daily limit
with open()	Log session to file
File append mode "a"	Save multiple history logs
f-strings formatting	Neat output table
📦 File Structure
Daily-Calorie-Tracker/
│
├── calorie_tracker.py        # Main application
├── calorie_log.txt           # Auto-generated log file
└── README.md                 # Documentation

🧑‍💻 How To Run
Requirements

Python 3 installed

Terminal / Command Prompt / VS Code / IDE

Running the Program
python calorie_tracker.py

📂 Program Flow Chart
Start
 ↓
Enter number of meals
 ↓
Loop through getting each meal name & calories
 ↓
Calculate total & average
 ↓
Input daily calorie limit
 ↓
Display formatted report
 ↓
Ask if user wants to save session
 ↓
If yes → write to calorie_log.txt
End

🗂 Output Example
=========================================
         🍎 DAILY CALORIE TRACKER 🍎
=========================================

Meal Name        Calories
-----------------------------------------
Breakfast        340
Lunch            480
Snacks           120
-----------------------------------------
Total:           940
Average:         313.33

⚠️ Warning: You have exceeded your daily calorie limit!

💾 Log File Example (calorie_log.txt)
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

🚀 Future Enhancements
Feature	Description
Add date & time auto-stamp	Track history chronologically
Weekly/Monthly Stats	Graphs using matplotlib
Convert to GUI	Tkinter or Kivy version
Export to Excel	Using pandas
Mobile App version	Android/Kivy

🎯 Learning Objectives Achieved
* Understanding basic Python structure
* Real-world file writing and report-style formatting
* Data handling and calculating metrics
* Building interactive programs

🤝 Contribution Guidelines
* Fork the repo
* Create a feature branch
* Commit changes
* Make a pull request

📄 License
* Open-source project — Free to modify and distribute.

👤 Author
Harsh Yadav
Python Developer
