import cv2
import numpy as np
  
#カメラをキャプチャ
cap = cv2.VideoCapture(0)

while(1):
# フレームを取得
    _, frame = cap.read()
# フレームをHSVに変換
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
# 取得する色の範囲を指定する
    lower_light_pink = np.array([168, 100, 100])
    upper_light_pink = np.array([188, 255, 255])
# 指定した色に基づいたマスク画像の生成
    mask = cv2.inRange(hsv, lower_light_pink, upper_light_pink)

    m = cv2.countNonZero(mask)
    h, w = mask.shape
    per = round(100*float(m)/(w * h),1)
    print("Moment[px]:",m)
    print("Percent[%]:", per)

    if per  >=  10:
        print("\007")

#画面表示
    cv2.imshow('mask',mask)

#escを押すと終了
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()