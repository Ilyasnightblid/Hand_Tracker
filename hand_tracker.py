import cv2
import mediapipe as mp


cap= cv2.VideoCapture(0)
mpHands =mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
while True:
  success, img =cap.read()
  img=cv2.flip(img,1)
  imgRGb =cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

  results = hands.process(imgRGb)

  if results.multi_hand_landmarks:
    print("Hand detect")

  cv2.imshow('Hand Tracker',img)
  if cv2.waitKey(5) & 0xff==27:
    break

cap.release()
cv2.destroyAllWindows()