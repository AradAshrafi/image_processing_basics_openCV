import cv2
import numpy as np
from lib.data_location import PICTURE_LOCATION
from lib.data_location import VIDEO_LOCATION


# it'll read and return test image RGB function
def read_image():
    return cv2.imread(PICTURE_LOCATION, 1)


# it'll be filled in future
def read_video():
    pass


# it'll show the image passed to it and will wait for a key to be pressed by user to exit
def show_image(image):
    cv2.imshow("image", image)  # the title and path to image
    cv2.waitKey(0)  # Waits for the next key to be pressed
    cv2.destroyAllWindows()


# extract blue channel of image
def extract_blue_channel(image):
    blue, green, red = cv2.split(image)
    green[:] = 0
    red[:] = 0
    return cv2.merge([blue, green, red])


# convert image to gray scale
def convert_to_gray_scale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)
