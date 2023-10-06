import cv2
import numpy as np
# import threading

Fire_Report = 0

def main():
    vid = cv2.VideoCapture('vid_file') # If you want access to webcam or any external camera use indices like 0 and 1

    while True:
        grabbed, frame = vid.read()
        
        if not grabbed:
            break

        frame = cv2.resize(frame, (640, 480))

        blur_frame = cv2.GaussianBlur(frame, (21, 21), 0)
        hsv_frame = cv2.cvtColor(blur_frame, cv2.COLOR_BGR2HSV)

        lower_value = [18, 50, 50]
        upper_value = [37, 255, 255]
        lower_value = np.array(lower_value, dtype="uint8")
        upper_value = np.array(upper_value, dtype="uint8")

        mask_frame = cv2.inRange(hsv_frame, lower_value, upper_value)

        output = cv2.bitwise_and(frame, hsv_frame, mask=mask_frame)

        no_red = cv2.countNonZero(mask_frame)

        if int(no_red) > 15000:
            Fire_Report = Fire_Report + 1

        cv2.imshow('System Output', output)

        if Fire_Report >= 1:
            print("FIRE DETECTED!!!")

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cv2.destroyALLwindows()
    vid.release()

if __name__ == "__main__":
    main()