from PIL import Image, ImageDraw, ImageFont

width, height = 300, 200
image = Image.new("RGB", (width, height), color="lightblue")

draw = ImageDraw.Draw(image)
draw.text((10, 10), "Test Image", fill="black")
image.save("test_image.bmp", "BMP")
image.save("test_image.png", "PNG")
image.save("test_image.jpg", "JPEG")

print("da tao xong anh BMP, PNG va JPEG.")
