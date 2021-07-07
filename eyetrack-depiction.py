import tobii_research as tr
import sys
import time
import numpy as np
import cv2

# 画面の特定
img = np.zeros((1080,1920,3), np.uint8)
cv2.imshow("MyEyeTrack", img)

# 視線情報をコールバック
def MyCallBack(gaze_data):
    time_stamp = gaze_data.device_time_stamp
    left_point = gaze_data.left_eye.gaze_point.position_on_display_area
    right_point = gaze_data.right_eye.gaze_point.position_on_display_area
    center_x = (int)(((left_point[0] + right_point[0]) / 2) * 1920)
    center_y = (int)(((left_point[1] + right_point[1]) / 2) * 1080) - 50
    global img
    img = cv2.circle(img, (center_x, center_y), 10, (255, 255, 255), -1)


# コールバックを登録
eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, MyCallBack, as_dictionary=False)

# 描画
while(True):
    key = cv2.waitKey(100)
    cv2.imshow("MyEyeTrack", img)

    # if Key is "ESC"
    if key == 27:
        eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, MyCallBack)
        cv2.destroyAllWindows()
        sys.exit()
