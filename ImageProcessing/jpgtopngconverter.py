import sys
import os
from PIL import Image

# Grab the first and second path
imageFolder = sys.argv[1]
outputFolder = sys.argv[2]

print(imageFolder, outputFolder)

# If path doesn't exist, create it
if not os.path.exists(outputFolder):
    os.makedirs(outputFolder)

# Grab the list of images
for filename in os.listdir(imageFolder):
    img = Image.open(f'{imageFolder}{filename}')
    newName = os.path.splitext(filename)[0]
    img.save(f'{outputFolder}{newName}.png', 'png')

print('Done processing')

# To run ::: python jpgtopngconverter.py pokedex/ convertedimages/

