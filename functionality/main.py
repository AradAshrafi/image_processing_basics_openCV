from functions import read_image, show_image, convert_to_gray_scale

if __name__ == '__main__':
    image = read_image()
    gray_scaled_image = convert_to_gray_scale(image)
    show_image(gray_scaled_image)
