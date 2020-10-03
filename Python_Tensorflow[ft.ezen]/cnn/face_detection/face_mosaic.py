import cv2
import matplotlib.pyplot as plt
from cnn.face_detection.mosaic import execute

face_file = "./data/haarcascade_frontalface_alt.xml"
casecade = cv2.CascadeClassifier(face_file)
img = cv2.imread('./data/family.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


#얼굴인식하기
face_list = casecade.detectMultiScale(img_gray, minSize=(150, 150))
#결과 확인하기
if len(face_file) == 0:
    print('실패')
    quit()

#모자이크 처리
for (x,y,w,h) in face_list:
    img = execute(img, (x, y, x+w, y+h), 10)
#이미지 출력
#이미지 출력하기
cv2.imwrite('./data/family_face.png', img)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()