import cv2

img = cv2.imread('veteran.jpg', cv2.IMREAD_COLOR)  # target img
mask = cv2.imread('model_face.jpg', cv2.IMREAD_COLOR)  # mask img
mask_hsv = cv2.cvtColor(mask, cv2.COLOR_BGR2HSV)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


def back_projection():  # Histogram Backprojection
    channels = [0, 1]
    ranges = [0, 180, 0, 256]  # H = 0~180 , S = 0~256
    mask_hist = cv2.calcHist([mask_hsv], channels, None, [180, 256], ranges)  # mask img 's histogram
    cv2.normalize(mask_hist, mask_hist, 0, 255, cv2.NORM_MINMAX)
    dst = cv2.calcBackProject([img_hsv], channels, mask_hist, ranges, 5)  # backprojection
    ret, img_binary = cv2.threshold(dst, 0, 255, cv2.THRESH_BINARY +
                                    cv2.THRESH_OTSU)  # Otsu binarization
    cv2.imshow('Original', img)
    cv2.imshow('Result', img_binary)
    cv2.waitKey(0)


back_projection()
