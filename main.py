import cv2
from hand_tracking import handDetector


if __name__ == "__main__":
  # For webcam input:
  cap = cv2.VideoCapture(0)

  hands = handDetector(mode = False, maxHands = 1, detectionCon= 0.7, trackCon = 0.7)

  tipIds = [4, 8, 12, 16, 20]
  while cap.isOpened():
      success, image = cap.read()
      image = hands.findHands(image)
      landmarksList = hands.findPosition(image)
      
      if not success:
        print("Ignoring empty camera frame.")
        # If loading a video, use 'break' instead of 'continue'.
        continue

      if len(landmarksList) != 0:
          if landmarksList[8][2] < landmarksList[4][2]:
              print("Index finger open")
          else:
              print("Finger closed")


      cv2.imshow('MediaPipe Hands', image)
      if cv2.waitKey(5) & 0xFF == 27:
        break

  cap.release()