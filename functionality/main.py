from functions import read_image, show_image, convert_to_gray_scale, extract_blue_channel, apply_gaussian_filter, \
    rotate_image, resize_image

if __name__ == '__main__':
    user_command_for_operation = int(input("enter number between 1 to 10\n"
                                           "1 for showing original image\n"
                                           "2 for blue channel of image\n"
                                           "3 for gray scaled image\n"
                                           "4 for gaussian blurred image\n"
                                           "5 for rotating 90 degree\n"
                                           "6 for resizing image\n"
                                           "7 for edge detection\n"))

    image = read_image()
    # show original test image
    if user_command_for_operation == 1:
        show_image(image=image)
    # show blue channel of test image
    if user_command_for_operation == 2:
        blue_image = extract_blue_channel(image=image)
        show_image(image=blue_image)
    # show gray scaled image
    if user_command_for_operation == 3:
        gray_scaled_image = convert_to_gray_scale(image=image)
        show_image(image=gray_scaled_image)
    # show gaussian blurred image
    if user_command_for_operation == 4:
        gaussian_blurred_image = apply_gaussian_filter(image=image)
        show_image(image=gaussian_blurred_image)
    # show 90 degree(or any degrees) rotated image
    if user_command_for_operation == 5:
        rotated_img = rotate_image(image=image, degrees=120)
        show_image(rotated_img)
    if user_command_for_operation == 6:
        resize_image = resize_image(image=image, weight_scale=0.5, height_scale=2)
        show_image(resize_image)

