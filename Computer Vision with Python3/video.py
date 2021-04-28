import cv2


def show_video():  # 비디오 재생
    capture = cv2.VideoCapture('gizmo.mp4')  # 동영상 파일 불러오기

    while True:
        if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(
                cv2.CAP_PROP_FRAME_COUNT):  # cv.CAP_PROP_POS_FRAMES 현재 프레임 수 cv.AP_PROP_FRAME_COUNT 총 프레임 수를 받아옴
            capture.set(cv2.CAP_PROP_POS_FRAMES, 0)  # 동영상 초기화
        ret, frame = capture.read()  # 재생되는 비디오를 한 프레임씩 읽어냄 제대로 읽었다면 True 를 반환
        cv2.imshow("VideoFrame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): # q 키를 누르면 종료
            break

    capture.release()  # 파일을 닫고 메모리 해제
    cv2.destroyAllWindows()


show_video()
