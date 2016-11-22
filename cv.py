# import numpy as np
import cv2

cap = cv2.VideoCapture(1)
face_cascade = cv2.CascadeClassifier('/usr/local/opt/opencv3/share/OpenCV/haarcascades/haarcascade_frontalface_default.xml')

prevFace = False
font = cv2.FONT_HERSHEY_PLAIN
font_size = 1

while(True):
    # フレームをキャプチャする
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    display = frame.copy()

    for(x, y, w, h) in faces:
        cv2.rectangle(display, (x - 30, y - 50), (x + w + 30, y + h + 50), (255, 0, 0), 2)
        cv2.imwrite('./rectedPhoto.jpg', frame[y - 50:y + h + 50, x - 30:x + w + 30])

    """
    if len(faces) > 0:
        if len(faces) != prevFace:
            cv2.imwrite('./photo.jpg', frame)
    """

    prevFace = len(faces)

    cv2.putText(display, "The num of faces in this pic " + str(len(faces)), (0, 10), font, font_size, (255, 255, 0))

    # 画面に表示する
    cv2.imshow('frame', display)

    # キーボã¼ド入力待ち
    key = cv2.waitKey(1) & 0xFF

    # qが押された場合は終了する
    if key == ord('q'):
        break
    # sが押された場合は保存する
    if key == ord('s'):
        path = "./photo.jpg"
        cv2.imwrite(path, frame)

# キャプチャの後始末と，ウィンドウをすべて消す
cap.release()
cv2.destroyAllWindows()
