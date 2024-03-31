import cv2 as cv
import sys

cap=cv.VideoCapture(0, cv.CAP_DSHOW)

if not cap.isOpened():
  sys.exit('카메라 연결 실패')

while True:
  ret, frame = cap.read()

  if not ret:
    print('프레임 휙득에 실패하여 루프를 나갑니다.')
    break

  cv.imshow('frame', frame)

  key=cv.waitKey(1)
  if key==ord('q'):
    break

cap.release()
cv.destroyAllWindows()