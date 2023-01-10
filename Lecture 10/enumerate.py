students = ['Jet', 'Sabrina', 'Alsion']

for i,student in enumerate(students):
    print(i + 1, student)
    
taipei = {student:'Taipei' for student in students}
print(taipei)