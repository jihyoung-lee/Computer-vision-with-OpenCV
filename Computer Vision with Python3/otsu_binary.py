import cv2

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)


def otsu_threshold():  # 오츄의 알고리즘
    cv2.namedWindow('Otsu Threshold')
    ret, thresh1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY +
                                 cv2.THRESH_OTSU)
    cv2.imshow('Otsu Threshold', thresh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


otsu_threshold()
