import numpy as np
import cv2
# 模式参数
dir_path = "C:\opencv-3.0.0\sources\data\haarcascades" # 配置OpenCV路径
filename = "haarcascade_frontalface_default.xml" # 识别模式文件
filename2= "haarcascade_eye.xml" # 识别模式文件
filename3= "haarcascade_smile.xml" # 这个模式有毒 orz
model_path = dir_path + "/" + filename
#人脸识别
def gface(image):
	# 创建 classifier
	clf = cv2.CascadeClassifier(model_path)
	# 设定灰度
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	# 识别面部
	faces = clf.detectMultiScale(
		gray,
		scaleFactor=1.1,
		minNeighbors=5,
		minSize=(30, 30),
		flags=cv2.CASCADE_SCALE_IMAGE
	)
	#print("Found {0} faces!".format(len(faces)))
	# 画方框
	for (x, y, w, h) in faces:
		cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
	return image
#获取视频
def gvideo():
    cap = cv2.VideoCapture(0) # 从摄像头中取得视频
    # 获取视频播放界面长宽
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) + 0.5)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) + 0.5)
    # 定义编码器 创建 VideoWriter 对象
    fourcc = cv2.VideoWriter_fourcc(*'mp4v') # Be sure to use the lower case
    out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (width, height))
    
    while(cap.isOpened()):
            #读取帧摄像头
            ret, frame = cap.read()
            if ret == True:
                    #输出当前帧
                    frame=gface(frame)
                    out.write(frame)
                    cv2.imshow('My Camera',frame)
                    #键盘按 Q 退出
                    if (cv2.waitKey(1) & 0xFF) == ord('q'):
                            break
            else:
                    break


    # 释放资源
    out.release()
    cap.release()
    cv2.destroyAllWindows()

if __name__=='__main__':
    gvideo()
