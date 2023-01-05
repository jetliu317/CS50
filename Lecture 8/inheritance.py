

class Name:
    def __init__(self, name):
        if not name:
            raise ValueError('Missing name')
        self.name = name
        
class Student(Name):
    def __init__(self, name, house):
        super().__init__(name)
        self.house = house
        
class Professor(Name):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

name = Name('Richard')
student = Student('Jet', 'Wugu')
professor = Professor('Apple', 'Economics')
