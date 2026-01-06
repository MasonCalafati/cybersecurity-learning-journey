import os

def load_todos():
    """Load todos from file"""
    if os.path.exists("todos.txt"):
        with open("todos.txt", "r") as file:
            todos = []
            for line in file:
                todos.append(line.strip())
            return todos
    return []

def save_todos(todos):
    """Save todos to file"""
    with open("todos.txt", "w") as file:
        for todo in todos:
            file.write(todo + "\n")

def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def main():
    todos = load_todos()
    
    while True:
        show_menu()
        choice = input("\nChoose an option: ")
        
        if choice == "1":
            if todos:
                print("\nYour tasks:")
                for i, todo in enumerate(todos, 1):
                    print(f"{i}. {todo}")
            else:
                print("\nNo tasks yet!")
        
        elif choice == "2":
            task = input("Enter new task: ")
            todos.append(task)
            save_todos(todos)
            print("Task added!")
        
        elif choice == "3":
            if todos:
                for i, todo in enumerate(todos, 1):
                    print(f"{i}. {todo}")
                num = int(input("Enter task number to remove: "))
                if 1 <= num <= len(todos):
                    removed = todos.pop(num - 1)
                    save_todos(todos)
                    print(f"Removed: {removed}")
            else:
                print("No tasks to remove!")
        
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
