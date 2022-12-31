import sys
import PIL
from PIL import Image

images = []

for arg in sys.argv[1:]:
    image = Image.open(arg)
    images.append(image)
    
images[0].save(
    'costumes.gif', save_all=True,append_images=[images[1]],durations=200,loop=0
)