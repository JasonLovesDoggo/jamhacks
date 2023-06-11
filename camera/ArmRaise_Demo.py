import cv2
import PoseModule as pm
import streamlit as st

cap = cv2.VideoCapture(1)
detector = pm.poseDetector()
armCounter = 0
counter_display = 0
direction = 0
form = 0
points = 0
feedback = "N/A"

frame_placeholder = st.empty()
stop_button_pressed = st.button("Stop")

while cap.isOpened() and not stop_button_pressed:
    ret, img = cap.read() #640 x 480

    scale_percent = 180 # percent of original size
    width = int(img.shape[1] * scale_percent / 100)
    height = int(img.shape[0] * scale_percent / 100)
    dim = (width, height)

    #Flips the image horizontally and rescales it
    img = cv2.flip(img, -1)
    img = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

    #Determine dimensions of video - Help with creation of box in Line 43
    width  = cap.get(3)  # float `width`
    height = cap.get(4)  # float `height`
    # print(width, height)
    
    if not ret:
        st.write("Video Capture has ended")
        break

    img = detector.findPose(img, False)
    lmList = detector.findPosition(img, False)
    # print(lmList)
    if len(lmList) != 0:
        left_elbow = detector.findAngle(img, 11, 13, 15)
        left_shoulder = detector.findAngle(img, 13, 11, 23)
        eft_hip = detector.findAngle(img, 11, 23,25)

        right_elbow = detector.findAngle(img, 12, 14, 16)
        right_shoulder = detector.findAngle(img, 14, 12, 24)
        right_hip = detector.findAngle(img, 12, 24, 26)

        #Check for starter position
        if right_shoulder < 30 and form != 1:
            form = 1
            feedback = "down"
        
        #During the arm workout
        if form == 1:
            if right_shoulder > 75 and right_shoulder < 105 and feedback == "down":
                if right_shoulder > 85 and right_shoulder < 95:
                    points += 10
                elif right_shoulder > 80 or right_shoulder < 100:
                    points += 7
                else:
                    points += 5
                armCounter += 0.5
                feedback = "up"
            elif feedback == "up" and right_shoulder < 30:
                armCounter += 0.5
                feedback = "down"
        
        #Lateral arm raise counter counter
        cv2.rectangle(img, (0, 0), (100, 100), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(armCounter)), (25, 75), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)
        
    cv2.imshow('Arm Raise', img)

    if int(armCounter) != counter_display:
        counter_display = int(armCounter)
        st.write(counter_display)

    if cv2.waitKey(10) & 0xFF == ord('q') or stop_button_pressed:
        print(points)
        break
        
cap.release()
cv2.destroyAllWindows()