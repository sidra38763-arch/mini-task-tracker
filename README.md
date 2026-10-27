# Mini Task Tracker

A simple menu-based task manager written in Python. Tasks are saved in a JSON file (`tasks.json`), so they are still there when the program is run again.

## Project Goal

To practise Python basics (lists, dictionaries, functions, loops, file handling, JSON and error handling) by building a small, useful command-line application.

## Features

- **Add** a task (stored as Pending)
- **View** all tasks as a numbered list with Pending / Done status
- **Complete** a task by its number
- **Delete** a task by its number
- **Save and load** tasks automatically using `tasks.json`
- **Menu** keeps showing until the user chooses Exit
- **Error handling** for empty titles, invalid menu choices, invalid task numbers and a missing JSON file

## How to Run

1. Make sure Python 3 is installed (or open the file in Google Colab).
2. Download `mini_task_tracker.py`.
3. Run it from a terminal:

   ```
   python mini_task_tracker.py
   ```

4. Choose an option from the menu (1 to 5).

## Example

```
--- TASK TRACKER ---
1. Add 2. View 3. Complete 4. Delete 5. Exit
Choice: 1
Task title: Read notes
Task added.
Choice: 2
1. Read notes [Pending]
Choice: 3
Task number: 1
Task completed.
Choice: 2
1. Read notes [Done]
```

## Files

- `mini_task_tracker.py` - main program
- `tasks.json` - created automatically when you add your first task
- `README.md` - project description

## Author

Sidra Rani - AI Engineering, Week 1
