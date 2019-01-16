import cv2 as openCV
from functionalities.read_media import read_media
from lib.data_location import PICTURE_LOCATION
from lib.data_location import VIDEO_LOCATION

if __name__ == '__main__':
    image = read_media(media_location=PICTURE_LOCATION, openCV_read_function=openCV.imread)
