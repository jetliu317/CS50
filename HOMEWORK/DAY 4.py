#Fuel Gauge
def main():
    fraction = get_fraction()
    print(get_fraction(fraction))
    
def get_fraction():
    while True:
        try:
            fraction = input("Fraction :")
            x, y = fraction.split("/")
            fraction = int(x) / int(y)
            if fraction == 0.75:
                return "75%"
            elif fraction == 0.50:
                return "50%"
            elif fraction == 0.25:
                return "25%"
            elif fraction >= 0.9:
                return "FULL"
            elif fraction <= 0.1:
                return"EMPTY"
        except (ValueError, ZeroDivisionError) :
            pass
        else:
            break

# main()

#restaurant counter
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    }  

def main():
    item = order()
    
def order():
    total_amount = 0
    while True:
        try:
            item = input("Item :").title()
            if item in menu:
                total_amount += menu[item]
                print("Total : $", total_amount)
            elif item not in menu:
                pass
        except EOFError :
            break    

# main()

#Grocery list


def main():
    item = product()
    
    
def product():
    grocery = {}
    while True:
        try:
            item = input().upper()
            if item in grocery:
                grocery[item] += 1
            else:
                grocery[item] = 1
        except EOFError:
            for item in sorted(grocery.keys()):
                print(grocery[item], item)
            break
    
# main()

#outdated

months = {
    "January" : 1,
    "February" : 2,
    "March" : 3,
    "April" : 4,
    "May" : 5,
    "June" : 6,
    "July" : 7,
    "August" : 8,
    "September" : 9,
    "October" : 10,
    "November" : 11,
    "December" : 12
}

def get_date():
    while True:
            date = input("Date :")
            if "/" in date  :
                month, day, year = date.split("/")
            elif "," in date  :
                date = date.replace(",", "")
                month, day, year = date.split(" ")
                if month.capitalize() in months:
                    month = months[month.capitalize()]
            try:
                if int(month) > 12 or int(day) > 31:
                    continue
                else:
                    break
            except ValueError:
                continue
    print(year, "-", f"{int(month):02}", "-", f"{int(day):02}", sep = "")
        
                
        
# get_date()