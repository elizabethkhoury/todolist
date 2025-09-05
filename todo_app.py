import time
import os

TASKS_FILE = "tasks.txt"

# Load tasks from file
def load_tasks():
    tasks = []
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            tasks = [line.strip() for line in f.readlines()]
    return tasks

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("✅ No tasks yet!")
    else:
        print("\nYour tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

# Add a task
def add_task(tasks):
    task = input("Enter a new task: ")
    tasks.append(task)
    save_tasks(tasks)
    print("Task added!")

# Study Timer (Pomodoro)
def start_study_timer():
    try:
        minutes = int(input("Enter study session length in minutes: "))
    except ValueError:
        print("Please enter a valid number.")
        return
    print(f"Starting study session for {minutes} minutes...")
    
    for remaining in range(minutes * 60, 0, -1):
        mins, secs = divmod(remaining, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\rTime left: {timer}", end="")
        time.sleep(1)
    print("\n✅ Study session complete! Take a break.")

# Main program
def main():
    tasks = load_tasks()
    
    while True:
        print("\n--- To-Do + Study App ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Start Study Timer")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            start_study_timer()
        elif choice == "4":
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
