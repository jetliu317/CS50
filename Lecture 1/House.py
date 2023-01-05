# Match
name = input("What's your name? ").capitalize()

match name:
    case "David":
        print("Griffindor")
    case "Hermione":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case '' :
        print("Who ? ")   
         
    case "David" | "Hermione" | "Ron":
        print("Griffindor")
    case "Draco":
        print("Slythrin")
    case '':
        print("who ? ")    