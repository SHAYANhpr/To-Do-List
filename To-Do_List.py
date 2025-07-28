import csv

class Task:
    def __init__(self, name, description, olavit):
        self.name = name          
        self.description = description 
        self.olavit = olavit 

    def to_list(self):
        return [self.name, self.description, self.olavit]    