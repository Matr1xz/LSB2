from PIL import Image

# Mã hóa chuỗi vào ảnh bằng LSB
def encode_lsb(image_path, output_path, message):
    if len(message) > 10:
        raise ValueError("Chỉ được nhập tối đa 10 ký tự")

    # Thêm ký tự kết thúc để biết khi nào kết thúc message
    message += chr(0)

    # Đọc ảnh
    img = Image.open(image_path)
    pixels = img.load()

    binary_message = ''.join(f"{ord(c):08b}" for c in message)
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
    print(f"Đã giấu thông điệp vào ảnh: {output_path}")


# Giải mã chuỗi từ ảnh
def decode_lsb(image_path):
    img = Image.open(image_path)
    pixels = img.load()

    width, height = img.size
    binary_data = ''
    
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            binary_data += str(r & 1)

    # Chuyển thành ký tự
    chars = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    message = ''
    for byte in chars:
        char = chr(int(byte, 2))
        if char == chr(0):
            break
        message += char
    return message


# Ví dụ sử dụng:
if __name__ == "__main__":
    # Nhập chuỗi muốn giấu
    message = input("Nhập mã sinh viên (tối đa 10 ký tự): ")

    # Dùng ảnh PNG để thử nghiệm
    input_image = input("Nhập đường dẫn ảnh đầu vào:")
    output_image = f'{input_image.split(".")[0]}_encoded.{input_image.split(".")[1]}'

    encode_lsb(input_image, output_image, message)
    extracted = decode_lsb(output_image)
    print("Thông điệp đã giải mã:", extracted)
