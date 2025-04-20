from PIL import Image

def encode_lsb(image_path, output_path, message):
    if len(message) > 10:
        raise ValueError("toi da 10 ky tu")

    message += chr(0)

    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ''.join("{:08b}".format(ord(c)) for c in message)
    message_len = len(binary_message)

    width, height = img.size
    data_index = 0

    for y in range(height):
        for x in range(width):
            if data_index >= message_len:
                break
            r, g, b = pixels[x, y]
            r = (r & ~1) | int(binary_message[data_index])  # thay bit LSB của Red
            data_index += 1
            pixels[x, y] = (r, g, b)
        if data_index >= message_len:
            break

    img.save(output_path)
    print("da giau thong diep vao anh: {}".format(output_path))


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
        message += char
    return message


if __name__ == "__main__":
    message = input("nhap msv: ")

    input_image = input("nhap duong dan anh dau vao:")
    # Thay f-string bằng .format()
    output_image = '{}_encoded.{}'.format(input_image.split(".")[0], input_image.split(".")[1])

    encode_lsb(input_image, output_image, message)
    extracted = decode_lsb(output_image)
    print("thong diep da giai: {}".format(extracted))