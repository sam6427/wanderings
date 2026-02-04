import sys, os
from PIL import Image

#as an exercise, I also wrote this version 
#which uses os rather than pathlib

current_folder = sys.argv[1]
new_folder = sys.argv[2]

if not os.path.exists(new_folder):
	os.mkdir(new_folder)

dir_list = os.listdir(current_folder)

for image in dir_list:
	f, e = os.path.splitext(image)
	outfile = f + ".png"
	try:
		with Image.open(current_folder + image) as im:
			im.save(new_folder + outfile)
	except OSError:
		print('cannot convert', image)

