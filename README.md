ToDo App (Text-Based Task Manager with XP and Levels)

This is a simple Python-based To-Do application that runs in the terminal. It allows users to create, view, complete, and delete tasks. The app includes a basic gamification system where completing tasks rewards XP and levels.

⸻

Features

1. Task List

Users can view all tasks in a numbered list. Each task shows whether it is completed or not.

2. Add Task

Users can enter a task name, and it will be added to the task list as incomplete.

3. Finish Task

Users can mark tasks as completed by selecting the task number.
Completing a task gives 50 XP.
When XP reaches 100, the user levels up and XP resets to 0.

4. Delete Task

Users can delete any task by selecting the task number from the list.

5. Player Stats

The app shows the player’s level and XP at the start of every loop.

6. Quit

Users can exit the app at any time by choosing option 5.

⸻

How It Works

The app runs in an infinite loop until the user chooses to quit.
At each iteration, the following menu is shown:

1. See list
2. Add task
3. Finish task
4. Delete task
5. Quit

The user types a number to choose an action.

Task Storage

The tasks list stores each task as a dictionary:

{"name": <task name>, "done": <True/False>}

XP and Level System
	•	Completing a task gives 50 XP.
	•	When XP reaches 100 or more:
	•	Level increases by 1.
	•	XP resets to 0.

⸻

Running the Program
	1.	Install Python 3 on your system.
	2.	Save the script in a .py file.
	3.	Open a terminal and run:

python3 filename.py

	4.	Follow the on-screen menu.

⸻

Example Interaction

PLAYER STATS
Level: 0
XP: 0/100
1. See list
2. Add task
3. Finish task
4. Delete task
5. Quit
