import cv2

img = cv2.imread('veteran.jpg', cv2.IMREAD_COLOR)
mask = cv2.imread('model_face.jpg', cv2.IMREAD_GRAYSCALE)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def histogram():
    channels = [0,1,2]
    ranges = [0, 256, 0, 256]
    hist = cv2.calcHist([img_hsv], channels, mask, [128, 128], ranges)
    hist_norm = cv2.normalize(cv2.log(hist + 1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
