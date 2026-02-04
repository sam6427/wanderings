from PIL import Image

moutain_view = Image.open('oskar-kadaksoo-pkCbhmBdNGA-unsplash.jpg')

print(moutain_view.format)
print(moutain_view.size)
print(moutain_view.mode)

moutain_view.show()

