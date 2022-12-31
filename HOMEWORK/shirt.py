#DAY 7-4
import sys
from PIL import Image
from PIL import ImageOps

def main():
    command()
    imagefile = Image.open(sys.argv[1])
    shirtfile = Image.open('shirt.png')
    size = shirtfile.size
    muppet = ImageOps.fit(imagefile, size)
    muppet.paste(shirtfile,shirtfile)
    muppet.save(sys.argv[2])
    
def command():
    if len(sys.argv) < 3:
        return sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        return sys.exit("Too many command-line arguments")
    elif '.jpg' not in sys.argv[1] and '.jpeg' not in sys.argv[1] and '.png' not in sys.argv[1]:
        return sys.exit("Not a image.")
    elif '.jpg' not in sys.argv[2] and '.jpeg' not in sys.argv[2] and '.png' not in sys.argv[2]:
        return sys.exit("Not a image.")
    else:
        try:
            with open(sys.argv[1]) as file:
                pass
        except FileNotFoundError:
            return sys.exit('File doesn\'t exist')
        
if __name__ == '__main__':
    main()