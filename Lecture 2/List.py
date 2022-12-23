#List
# students = ["Jet", "Sabrina", "Alison"]
# house = ["Liu", "Huang", "Gao"]
# for student in students:
# for i in range(len(students)):
#     print(i + 1, students[i])

students = {
    "Sabrina" : "Huang",
    "Jet" : "Liu",
    "Alison" : "Gao"
}

for student in students:
    print(student, students[student])   
    
    
def main():
    print_square(3)
    
def print_square(size):
    for i in range(size):
        # for j in range(size):
        #     print("x", end = "")
        # print()           
        print("x" * size)
main()
     