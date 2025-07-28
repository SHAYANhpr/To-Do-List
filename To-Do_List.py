import csv

class Task:
    def __init__(self, name, description, olavit):
        self.name = name          
        self.description = description 
        self.olavit = olavit 

    def to_list(self):
        return [self.name, self.description, self.olavit]
    
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