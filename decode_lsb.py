from PIL import Image
def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    binary_data = ''
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)

    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in chars:
        char = chr(int(byte, 2))
        if char == chr(0):
            break
        if char.isprintable():
            message += char
    return message

image_path = input("nhap duong dan anh dau vao:")
message = decode_lsb(image_path)
print("thong diep trong anh {}: {}".format(image_path.split(".")[1],message))