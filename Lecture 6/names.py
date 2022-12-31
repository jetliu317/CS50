name = input('What\'s your name?' )

with open('name.txt', 'a') as file :
    file.write(f"{name}\n")
    #file.close()
    
# name = []    
with open('name.txt', 'r') as file:
    for line in sorted(file):
        print(f'Hello, {line.rstrip()}')
# for name in sorted(name):
#     print(f'Hello, {name}')