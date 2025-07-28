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