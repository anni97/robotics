import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Our operations on the frame come here
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #defining orange boundaries
    lower_orange = np.array([0,130,130])
    upper_orange = np.array([45,255,255])

    #threshold to get only orange colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)

    #put mask on image
    res = cv2.bitwise_and(frame, frame, mask= mask)

    # Display the resulting frame
    cv2.imshow('frame',hsv)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()