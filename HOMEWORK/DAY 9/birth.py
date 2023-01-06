import datetime
import inflect

class birth:
    def __init__(self, birthday):
        self.birthday = birthday
        
    def __str__(self):
        return (self.birthday)
        
    @classmethod   
    def get(cls):
        birthday = input('Date of birth: ')
        return cls(birthday)
    
    @property
    def birthday(self):
        return self._birthday
    @birthday.setter
    def birthday(self, birthday):
        y, m, d = birthday.split('-')
        if int(y)>2023 or int(m)>12 or int(d)>31:
            raise ValueError("Invalid date")
        self._birthday = birthday

def main():
    lifetime = birth.get()
    today = datetime.date.today()
    time1= datetime.datetime.strptime(f'{lifetime}', '%Y-%m-%d').date()
    time2= datetime.datetime.strptime(f'{today}', '%Y-%m-%d').date()
    mins = int((time2-time1).days) * 24 * 60 
    p = inflect.engine()
    output = p.number_to_words(mins)
    print(output.capitalize(), 'minutes')

if __name__ == "__main__":
    main()