import csv
name = input('What\'s your name?' )

students = []

with open('name.csv','a') as file:
    file.write(f"{name}\n")
    
with open('name.csv') as file:
    for line in file:
        first, last = line.rstrip().split(',')
        student = {'first':first, 'last':last}
        # student['first'] = first
        # student['last'] = last
        students.append(student)
        
# def get_name(student):
#     return student['first']
        
for student in sorted(students, key = lambda student :student['first']):
    print(f"{student['first']} {student['last']}")