import cv2

def detect_eyes(eye_cascade, gray_roi):
    return eye_cascade.detectMultiScale(gray_roi)

def track_eye_movement(eye_roi_gray, eye_roi_color, ew, eh):
    _, eye_thresh = cv2.threshold(eye_roi_gray, 50, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(eye_thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if len(contours) > 0:
        pupil = max(contours, key=cv2.contourArea)
        x1, y1, w1, h1 = cv2.boundingRect(pupil)
        center = (int(x1 + w1 / 2), int(y1 + h1 / 2))
        cv2.circle(eye_roi_color, center, 3, (255, 0, 0), -1)

        if center[0] < ew /3:
            return "left"
        elif center[0] > 2 * ew / 3:
            return "right"
        elif center[1] < eh /3:
            return "up"
        elif center[1] > 2 * eh /3:
            return "down"
        else:
            return "center"
    return None