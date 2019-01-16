from functions import read_image, show_image, convert_to_gray_scale, extract_blue_channel

if __name__ == '__main__':
    image = read_image()
    blue_image = extract_blue_channel(image=image)
    show_image(image=blue_image)
    gray_scaled_image = convert_to_gray_scale(image=image)
    show_image(image=gray_scaled_image)
