import cv2
import time
import numpy as np
from lib.data_location import PICTURE_LOCATION
from lib.data_location import VIDEO_LOCATION
from lib.data_location import CASCADE_CLASSIFIER_LOCATION


# it'll read and return test image RGB function
def read_image():
    return cv2.imread(PICTURE_LOCATION, 1)


# it'll capture test video's frames
def read_video(location=VIDEO_LOCATION):
    return cv2.VideoCapture(location)


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


# apply gaussian filter on image to smooth it
def apply_gaussian_filter(image):
    return cv2.GaussianBlur(image, (5, 5), 0)


# rotate image with desired degree
def rotate_image(image, degrees):
    # get image height, width
    (h, w) = image.shape[:2
             ]
    # calculate the center of the image
    center = (w / 2, h / 2)
    scale = 1.0

    # Perform the counter clockwise rotation holding at the center
    # 90 degrees
    M = cv2.getRotationMatrix2D(center, degrees, scale)
    return cv2.warpAffine(image, M, (h, w))


# resize image with
def resize_image(image, weight_scale, height_scale):
    return cv2.resize(image, (0, 0), fx=weight_scale, fy=height_scale)


# detect edges in picture with canny edge detection
def edge_detection(image):
    return cv2.Canny(image, 100, 200)


# it'll be filled soon
def segmentation(image):
    gray = convert_to_gray_scale(image=image)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    # noise removal
    kernel = np.ones((3, 3), np.uint8)
    opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)
    # sure background area
    sure_bg = cv2.dilate(opening, kernel, iterations=3)
    # Finding sure foreground area
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(sure_bg, sure_fg)
    # Marker labelling
    ret, markers = cv2.connectedComponents(sure_fg)
    # Add one to all labels so that sure background is not 0, but 1
    markers = markers + 1
    # Now, mark the region of unknown with zero
    markers[unknown == 255] = 0
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 255, 255]
    show_image(image=image)


# detect faces in picture using haarcascade frontal face
def face_detection(image):
    # Create the haar cascade
    face_cascade = cv2.CascadeClassifier(CASCADE_CLASSIFIER_LOCATION)

    # create gray scaled image
    gray_scaled_image = convert_to_gray_scale(image=image)

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        gray_scaled_image,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
        # flags = cv2.CV_HAAR_SCALE_IMAGE
    )
    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Faces found", image)
    cv2.waitKey(0)


# capture first specified frames
def video_framing(number_of_frames=5):
    vid_cap = read_video()
    success = True
    count = 0
    while success and count < number_of_frames:
        success, frame = vid_cap.read()
        cv2.imshow("frame" + str(count), frame)
        cv2.waitKey(500)
        cv2.destroyAllWindows()
        count += 1
