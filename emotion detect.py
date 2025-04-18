from facial_emotion_recognition import EmotionRecognition
import cv2
er=EmotionRecognition(device='cpu')
cam=cv2.VideoCapture(0)
while True:
    success,frame=cam.read()
    frame=er.regognise emotion(frame,return_type='BGR')
    cv2.imshow("Frame",frame)
    key=cv2,WaitKey(1)
    if key==27:
        break
cam.release()
cv2.destroyAllWindows()
