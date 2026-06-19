import cv2
import mediapipe as mp
import pyautogui as pg

my_hands = mp.solutions.hands.Hands(
    max_num_hands=1,
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)
drawing_utils = mp.solutions.drawing_utils

x1 = y1 = x2 = y2 = 0

webcam = cv2.VideoCapture(0)

while True:
    success , image = webcam.read()
    if not success:
        continue
    image = cv2.flip(image , 1)
    frame_height , frame_width , _ = image.shape
    rgb_image = cv2.cvtColor(image , cv2.COLOR_BGR2RGB)
    output = my_hands.process(rgb_image)
    hands = output.multi_hand_landmarks
    
    if hands:
        for hand_landmarks in hands:
            drawing_utils.draw_landmarks(image , hand_landmarks)
            landmark = hand_landmarks
            
        for id , landmarks in enumerate(hand_landmarks.landmark):
            x = int(landmarks.x * frame_width)
            y = int(landmarks.y * frame_height)

            if id == 4:
               cv2.circle(img= image , center=(x,y), radius=8, color=(255,0,0), thickness=5)
               x1=x
               y1=y
            if id == 8:
               cv2.circle(img= image , center=(x,y), radius=8, color=(255,255,0), thickness=5)
               x2=x
               y2=y
        dist = ((x2-x1)**2 + (y2-y1)**2)**0.5//4
    
        if dist > 30:
         pg.press("volumeup") 
        else:
           pg.press("volumedown")
        
    cv2.imshow("Volunme controll with hand", image)
    key = cv2.waitKey(10)
    if key == 27:
        break

webcam.release()
cv2.destroyAllWindows()