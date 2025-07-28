import csv

class Task:
    def __init__(self, name, description, Priority):
        self.name = name          
        self.description = description 
        self.Priority = Priority 

    def to_list(self):
        return [self.name, self.description, self.Priority]
    
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
        else:
            print("The number entered is invalid.")

    def show_tasks(self):
        if not self.tasks:
            print("The task list is empty.")
        else:
            print("\n To-do list:")
            for i, task in enumerate(self.tasks):
                print(f"{i}. name: {task.name} | description: {task.description} | Priority: {task.Priority}")

    def save_to_csv(self, filename):
        with open(filename, mode='w', encoding='utf-8') as file:
            writer = csv.writer(file)
            for task in self.tasks:
                writer.writerow(task.to_list())
        print("The list was saved to the file.")

    def load_from_csv(self, filename):
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                self.tasks = []
                for row in reader:
                    if len(row) == 3:
                        name, description, Priority = row
                        self.tasks.append(Task(name, description, Priority))
            print("List loaded from file.")
        except FileNotFoundError:
            print("File not found --> New list created!")

def main():
    todo = ToDoList()
    filename = "result.csv"  
    todo.load_from_csv(filename)

    while True:
        print("\n=== To-do list management ===")
        print("1.Add task")
        print("2.Remove task")
        print("3.Show tasks")
        print("4.Save list")
        print("5.Exit")

        Choice = input("Enter the desired number: ")

        if Choice == '1':
            name = input(" Name task: ")
            description = input(" Description task: ")
            Priority = input(" Priority (high, medium, low): ")
            task = Task(name, description, Priority)
            todo.add_task(task)
            print(" Task added successfully.")

        elif Choice == '2':
            todo.show_tasks()
            try:
                index = int(input(" Task number to delete: "))
                todo.remove_task(index)
            except ValueError:
                print(" Please enter a number.")

        elif Choice == '3':
            todo.show_tasks()

        elif Choice == '4':
            todo.save_to_csv(filename)

        elif Choice == '5':
            todo.save_to_csv(filename)
            print(" Successfully registered")
            break

        else:
            print(" Invalid option! Enter a number between 1 and 5")

if __name__ == "__main__":
    main()