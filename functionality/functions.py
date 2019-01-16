import cv2 as openCV
from lib.data_location import PICTURE_LOCATION
from lib.data_location import VIDEO_LOCATION


# it'll read and return test image RGB function
def read_image():
    return openCV.imread(PICTURE_LOCATION, 1)


# it'll be filled in future
def read_video():
    pass


# it'll show the image passed to it and will wait for a key to be pressed by user to exit
def show_image(image):
    openCV.imshow("image", image)  # the title and path to image
    openCV.waitKey(0)  # Waits for the next key to be pressed
    openCV.destroyAllWindows()


def convert_to_gray_scale(image):
    return openCV.cvtColor(image, openCV.COLOR_BGR2GRAY)
