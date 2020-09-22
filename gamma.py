import cv2
import numpy as np

def myfunc(x):
    pass

def main():
    cap = cv2.VideoCapture(1)

    cv2.namedWindow(" frame")
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,  640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

#トラックバー を作成
    cv2.createTrackbar("gamma(0.1)", " frame", 1, 50, myfunc)
    cv2.setTrackbarPos("gamma(0.1)", " frame", 10)

    while(1):
        ret, frame = cap.read()

        # ガンマ値取得（0は強制的に0.1相当に引き戻し）
        gamma = cv2.getTrackbarPos("gamma(0.1)", " frame") * 0.1
        if gamma == 0:
            gamma = 0.1
            cv2.setTrackbarPos("gamma(0.1)", " frame", 1)

        # ガンマ補正用ルックアップテーブル
        look_up_table = np.zeros((256, 1), dtype = 'uint8')
        for i in range(len(look_up_table)):
            look_up_table[i][0] = (len(look_up_table)-1) * pow(float(i) / (len(look_up_table)-1), 1.0 / gamma)

        # ルックアップテーブルによるガンマ補正
        gamma_correction_image = cv2.LUT(frame, look_up_table)

        # ウィンドウ表示
        cv2.putText(gamma_correction_image, "gamma:" + str(gamma), (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,0),2)
        cv2.imshow(" frame", gamma_correction_image)

        k = cv2.waitKey(1) 
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
