import cv2
import mediapipe as mp
import numpy as np
import PoseModule as pm

cap = cv2.VideoCapture(1)
detector = pm.poseDetector()
count = 0
direction = 0
form = 0
feedback = "Fix Form"


while cap.isOpened():
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
        
        #Percentage of success of pushup
        per = np.interp(right_elbow, (90, 160), (0, 100))
        
        #Bar to show Pushup progress
        bar = np.interp(right_elbow, (90, 160), (380, 50))

        if right_shoulder < 15:
            right_shoulder_previous = right_shoulder
            print("starting")
        else:
            print("")

        '''
        #Check for full range of motion for the pushup
        if form == 1:
            if per == 0:
                if right_elbow <= 90 and right_hip > 160:
                    feedback = "Up"
                    if direction == 0:
                        count += 0.5
                        direction = 1
                else:
                    feedback = "Fix Form"
                    
            if per == 100:
                if right_elbow > 160 and right_shoulder > 40 and right_hip > 160:
                    feedback = "Down"
                    if direction == 1:
                        count += 0.5
                        direction = 0
                else:
                    feedback = "Fix Form"
                        # form = 0
                        '''
        #print(count)

        cv2.rectangle(img, (580, 50), (600, 380), (0, 255, 0), 3)
        cv2.rectangle(img, (580, int(bar)), (600, 380), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, f'{int(per)}%', (565, 430), cv2.FONT_HERSHEY_PLAIN, 2,
                    (255, 0, 0), 2)
        
        #Pushup counter
        cv2.rectangle(img, (0, 380), (100, 480), (0, 255, 0), cv2.FILLED)
        cv2.putText(img, str(int(count)), (25, 455), cv2.FONT_HERSHEY_PLAIN, 5,
                    (255, 0, 0), 5)
        
        #Feedback 
        cv2.rectangle(img, (500, 0), (640, 40), (255, 255, 255), cv2.FILLED)
        cv2.putText(img, feedback, (500, 40 ), cv2.FONT_HERSHEY_PLAIN, 2,
                    (0, 255, 0), 2)
        
    cv2.imshow('Workout Detector', img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
        
cap.release()
cv2.destroyAllWindows()