import cv2

# cv2.cv.CV_FOURCC
def cv_fourcc(c1, c2, c3, c4):
    return (ord(c1) & 255) + ((ord(c2) & 255) << 8) + \
        ((ord(c3) & 255) << 16) + ((ord(c4) & 255) << 24)

    # カメラ映像取得
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # 保存ビデオファイルの準備
    end_flag, c_org = cap.read()
    height, width, channels = c_org.shape
    rec = cv2.VideoWriter(GAUSSIAN_FILE_NAME, \
                          cv_fourcc('X', 'V', 'I', 'D'), \
                          30, \
                          (width, height), \
                          True)

    # ウィンドウの準備
    cv2.namedWindow(org)
    cv2.namedWindow(gaussian)
    
    
    
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=50,param2=30,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    
    
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)

  
        key = cv2.waitKey(1)
        if key == 27:
            break

        # 次のフレーム読み込み
        end_flag, c_org = cap.read()

    # 終了処理
    cv2.destroyAllWindows()
    cap.release()
    rec.release()