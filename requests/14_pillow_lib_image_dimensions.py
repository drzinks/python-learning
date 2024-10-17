from PIL import Image

filename = "C:\\Users\\drzin\\Desktop\\mems\\kolo_ch.jpg"
image = Image.open(filename)

print("Wysokość obrazka: ", image.height)
print("Szerokość obrazka: ", image.width)