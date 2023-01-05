class Student():
    def __init__(self, name, house):
        # if not name:
        #     raise ValueError('Missing name')
        # if not house:
        #     raise ValueError('Missing house')
        self.name = name
        self.house = house
        # self.patronus = patronus
    def __str__(self):
        return f'{self.name} is from {self.house}'
    # def charm(self):
    #     match self.patronus:
    #         case 'Stag':
    #             return '🐴'
    #         case 'Otter':
    #             return '🦦'
    #         case 'Jack Russell Terrier':
    #             return '🐶'
    #         case _:
    #             return '🧹'
    
    #@property is to make arguments immunable(have to make different syntax because the original one is used in __init__ ,EX. self.name -> self._name)
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name
    
    @property
    def house(self):
        return self._house
    @house.setter
    def house(self, house):
        if not house:
            raise ValueError('Missing House')
        self._house = house
        
def main():
    student = get_student()
    print (f'{student}')
    
def get_student():
    name = input('Name: ')
    house = input('House: ')
    # patronus = input('Patronus: ')
    return Student(name, house)

if __name__ == '__main__':
    main()
    
