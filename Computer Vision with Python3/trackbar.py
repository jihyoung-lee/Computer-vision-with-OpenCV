import cv2 as cv


# 트랙바 이벤트를 처리 할 콜백 함수
def onChange(pos):
    pass


def img_show():
    img = cv.imread('chess.jpg', cv.IMREAD_GRAYSCALE)  # Grayscale
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


# 트랙바 함수
def trackbar():
    img = cv.imread('chess.jpg')
    cv.namedWindow('binarization')
    cv.createTrackbar('threshold', 'binarization', 0, 255, onChange)  # 트랙바 생성
    while True:
        low = cv.getTrackbarPos('threshold', 'binarization')  # 트랙바의 현재값을 가져와 임계값으로 사용할 수 있도록 함
        ret, img_binary = cv.threshold(img, low, 255, cv.THRESH_BINARY_INV)  # THRESH_BINARY_INV : 반전된 마스크 이미지
        cv.imshow('binarization', img_binary)
        if cv.waitKey(1) & 0xFF == 27:  # esc 누르면 닫음
            break
    cv.destroyAllWindows()


trackbar()
