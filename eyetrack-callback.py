import tobii_research as tr
import sys
import time

# アイトラッカーを見つける．偽なら終わり
eyetrackers = tr.find_all_eyetrackers()
if len(eyetrackers) >= 1 :
    eyetracker = eyetrackers[0]
else:
    print "Error: Not Found EyeTracker"
    sys.exit()


# プロダクトキー読み込み
license_file_path = "license_key_00414084_-_SJU_IS404-100107812654"
f = open(license_file_path, "rb")
license = f.read()
eyetracker.apply_licenses(license)


# 左右の目の視線情報をコールバック
def MyCallBack(gaze_data):
    time_stamp = gaze_data.device_time_stamp
    left_point = gaze_data.left_eye.gaze_point.position_on_display_area
    right_point = gaze_data.right_eye.gaze_point.position_on_display_area
    print "Time:" + str(time_stamp)
    print "Left Eye:" + str(left_point[0]) + " " + str(left_point[1])
    print "Right Eye:" + str(right_point[0]) + " " + str(right_point[1])


# コールバックしたのものを登録
eyetracker.subscribe_to(tr.EYETRACKER_GAZE_DATA, MyCallBack, as_dictionary=False)
time.sleep(2)
eyetracker.unsubscribe_from(tr.EYETRACKER_GAZE_DATA, MyCallBack)
