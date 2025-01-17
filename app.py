from PIL import Image

path = input("enter picture path:")
img = Image.open(path)
# icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64)]
icon_sizes = [(256, 256)]
img.save(path+".ico", sizes=icon_sizes)
