def main():
    student = get_student()
    #print (f"{student['name']} from {student['house']}")
    print (f"{student[0]} from {student[1]}")
    
def get_student():
    name = input('Name: ')
    house = input('House: ')
    #dic : return {'name': name, 'house' : house}
    #list : return [name, house]
    #tuple
    return (name, house)

if __name__ == '__main__':
    main()
    
    #dictionaries可以存資料by names, list only by numbers, tuple則直接return不可改變