import numpy as np
import cv2

def changeColor(i):
    pass # do nothing

cv2.namedWindow('frame') # create win with win name

# トラックバーの生成
cv2.createTrackbar('R','frame',0,100,changeColor)
cv2.createTrackbar('G','frame',0,100,changeColor)
cv2.createTrackbar('B','frame',0,100,changeColor)

# カメラの読み込み
cap = cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while(True):
    ret, frame = cap.read()
    if not ret: continue

# トラックバーの値を変更する度にRGBを出力する
#トラックバーの値を%で表すために100でわる

    r = cv2.getTrackbarPos('R','frame')/100
    g = cv2.getTrackbarPos('G','frame')/100
    b = cv2.getTrackbarPos('B','frame')/100
#オーバーフローしてしまうので、frameを255でわる
    frame = frame/255
	
    frame[:,:,0] *= b
    frame[:,:,1] *= g
    frame[:,:,2] *= r

 # 画面を表示する
    cv2.imshow('frame', frame) 
    
    k = cv2.waitKey(1)
    if k == ord('q') or k == 27:
        break

cap.release()
cv2.destroyAllWindows()