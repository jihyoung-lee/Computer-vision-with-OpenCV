import cv2 as cv

img = cv.imread('chess.jpg', cv.IMREAD_GRAYSCALE)


# onChange :  트랙바 이벤트를 처리 할 콜백 함수

def onChange(dst):  # 적응적 이진화 콜백함수
    blockSize = cv.getTrackbarPos('blockSize', 'Adaptive')
    c = cv.getTrackbarPos('c', 'Adaptive')
    if blockSize % 2 == 1:  # blockSize % 2 == 1 & blockSize > 1
        # ADAPTIVE_THRESH_MEAN_C
        # adaptive = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, blockSize, c)
        # ADAPTIVE_THRESH_GAUSSIAN_C
        adaptive = cv.adaptiveThreshold(img, 255, cv. ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, blockSize, c)
        cv.imshow('Adaptive', adaptive)


def Adaptive():  # 적응적 이진화
    cv.namedWindow('Adaptive')
    cv.createTrackbar('blockSize', 'Adaptive', 3, 255, onChange)
    cv.createTrackbar('c', 'Adaptive', 0, 255, onChange)
    cv.imshow('Adaptive', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def onChange2(dst):  # 이진화 콜백함수
    low = cv.getTrackbarPos('threshold', 'binarization')  # 트랙바의 현재값을 가져와 임계값으로 사용할 수 있도록 함
    ret, img_binary = cv.threshold(img, low, 255, cv.THRESH_BINARY_INV)  # THRESH_BINARY_INV : 반전된 마스크 이미지
    cv.imshow('binarization', img_binary)


def binarization():  # 이진화
    cv.namedWindow('binarization')
    cv.createTrackbar('threshold', 'binarization', 0, 255, onChange2)  # 트랙바 생성
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_show():
    img2 = cv.imread('chess.jpg', cv.IMREAD_GRAYSCALE)  # Grayscale
    cv.imshow('window', img)
    cv.waitKey(0)
    cv.destroyAllWindows()


def img_show2():
    cv.namedWindow('binarization')
    img = cv.imread('chess.jpg')
    img2 = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imshow('Original', img)
    cv.imshow('Gray', img2)
    cv.waitKey(0)
    cv.destroyAllWindows()


Adaptive()
