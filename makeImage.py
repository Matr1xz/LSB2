from PIL import Image, ImageDraw, ImageFont

# Tạo một ảnh RGB đơn giản
width, height = 300, 200
image = Image.new("RGB", (width, height), color="lightblue")

# Vẽ một số nội dung lên ảnh để dễ kiểm tra
draw = ImageDraw.Draw(image)
draw.text((10, 10), "Test Image", fill="black")

# Lưu ảnh ở các định dạng khác nhau
image.save("test_image.bmp", "BMP")
image.save("test_image.png", "PNG")
image.save("test_image.jpg", "JPEG")

print("Đã tạo xong ảnh BMP, PNG và JPEG.")
