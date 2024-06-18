#                  Gesture-Controlled Application Launcher
#                  ---------------------------------------


# This project aims to harness the power of MediaPipe and OpenCV to create a system that recognizes hand gestures and uses them to open and control various
# applications. By leveraging machine learning and computer vision techniques, this system interprets specific hand gestures captured through a webcam and
# translates them into commands to open web pages or desktop applications.


import cv2
import mediapipe as mp
import webbrowser
import time


mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.8)
mp_draw= mp.solutions.drawing_utils

app_opened = False
current_app = None
app_open_time = 0

app_urls = {
    1: 'https://www.spotify.com',
    2: 'https://www.gmail.com',
    3: 'https://web.whatsapp.com',
    4: 'https://www.google.com',
    5: 'https://in.indeed.com'
}

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()


    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(image_rgb)
    num_fingers = 0

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            thumb = landmarks[4].x < landmarks[3].x < landmarks[2].x < landmarks[1].x
            index_finger = landmarks[8].y < landmarks[6].y
            middle_finger = landmarks[12].y < landmarks[10].y
            ring_finger = landmarks[16].y < landmarks[14].y
            pinky_finger = landmarks[20].y < landmarks[18].y

            num_fingers = sum([thumb, index_finger, middle_finger, ring_finger, pinky_finger])

            cv2.putText(frame, f"Fingers: {num_fingers}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


            if not app_opened and num_fingers in app_urls:
                webbrowser.open(app_urls[num_fingers])
                app_opened = True
                current_app = num_fingers
                app_open_time = time.time()




    if app_opened and ((time.time() - app_open_time) >10)  :
        app_opened = False
        current_app = None

    cv2.imshow("Hand Gesture Detection", frame)


    if cv2.waitKey(1) == ord("q"):
        break

cv2.destroyAllWindows()
cap.release()
