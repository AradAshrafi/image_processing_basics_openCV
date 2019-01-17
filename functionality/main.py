from functions import read_image, show_image, convert_to_gray_scale, extract_blue_channel, apply_gaussian_filter, \
    rotate_image, resize_image, edge_detection, segmentation, face_detection, video_framing

if __name__ == '__main__':
    # going through whole functionality first
    image = read_image()
    # show original test image
    show_image(image=image)
    # show blue channel of test image
    blue_image = extract_blue_channel(image=image)
    show_image(image=blue_image)
    # show gray scaled image
    gray_scaled_image = convert_to_gray_scale(image=image)
    show_image(image=gray_scaled_image)
    # show gaussian blurred image
    gaussian_blurred_image = apply_gaussian_filter(image=image)
    show_image(image=gaussian_blurred_image)
    # show 90 degree(or any degrees) rotated image
    rotated_img = rotate_image(image=image, degrees=90)
    show_image(rotated_img)
    # resize image with desired weight and height scale
    resize_image = resize_image(image=image, weight_scale=0.5, height_scale=2)
    show_image(resize_image)
    # detect edges of the image
    edges = edge_detection(image=image)
    show_image(edges)
    # picture segmentation
    segmentation(image=image)
    # detect faces in the picture
    face_detection(image=image)
    # capture first five frames of test video
    video_framing(number_of_frames=5)

    while True:
        user_command_for_operation = int(input("enter number between 0 to 10\n"
                                               "0 to exit\n"
                                               "1 for showing original image\n"
                                               "2 for blue channel of image\n"
                                               "3 for gray scaled image\n"
                                               "4 for gaussian blurred result\n"
                                               "5 for result of 90 degree rotation\n"
                                               "6 for resizing image\n"
                                               "7 for edge detection result\n"
                                               "8 for segmentation result\n"
                                               "9 for face detection result\n"
                                               "10 to show result of 5 first frame of video\n"))
        # 0 command is to end program so ->
        if user_command_for_operation == 0:
            break
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
            rotated_img = rotate_image(image=image, degrees=90)
            show_image(rotated_img)
        # resize image with desired weight and height scale
        if user_command_for_operation == 6:
            resize_image = resize_image(image=image, weight_scale=0.5, height_scale=2)
            show_image(resize_image)
        # detect edges of the image
        if user_command_for_operation == 7:
            edges = edge_detection(image=image)
            show_image(edges)
        # picture segmentation
        if user_command_for_operation == 8:
            segmentation(image=image)
        # detect faces in the picture
        if user_command_for_operation == 9:
            face_detection(image=image)
        # capture first five frames of test video
        if user_command_for_operation == 10:
            video_framing(number_of_frames=5)
