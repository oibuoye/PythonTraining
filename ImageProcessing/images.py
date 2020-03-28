from PIL import Image, ImageFilter

img = Image.open('./pokedex/astro.jpg')
newImg = img.resize((400, 400))
newImg.save('./pokedex/astro-thumbnail.jpg')