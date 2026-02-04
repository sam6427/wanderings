import sys
from PIL import Image
from pathlib import Path

#this version uses pathlib rather than os

#python3 JPGtoPNGconverter.py arg1 arg2
#arg1 : folder name, e.g pokedex/
#arg2 : folder we want to create, e.g new/

current_folder = Path(sys.argv[1])
new_folder = Path(sys.argv[2])

if not new_folder.is_dir():
	new_folder.mkdir()

for image in current_folder.iterdir():
	image_name = image.stem
	new_image_name = image_name + '.png'
	new_image_path = new_folder / new_image_name
	try:
		with Image.open(image) as im:
			im.save(new_image_path)
	except OSError:
		print('cannot convert', image)

