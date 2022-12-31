import csv
first_name = input('What\'s your first name?' )
last_name = input('What\'s your last name?' )

students = []

with open('name.csv','a') as file:
    writer = csv.DictWriter(file, fieldnames = ['first','last'])
    writer.writerow({'first':first_name, 'last':last_name})
    
with open('name.csv') as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({'first':row['first'], 'last':row['last']})
        
for student in sorted(students, key = lambda student :student['first']):
    print(f"{student['first']} {student['last']}")