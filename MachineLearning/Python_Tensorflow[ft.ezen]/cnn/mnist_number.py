import  tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
import cv2
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


model = tf.keras.models.Sequential([
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(512,activation=tf.nn.relu),#덴스는 은닉층 , 512는 최적의? 층?
    tf.keras.layers.Dropout(0.2),
    tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])
model.compile(optimizer='adam',
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])
model.fit(x_train, y_train, epochs=5)
score = model.evaluate(x_test, y_test)
gray = cv2.imread("/Users/donut/Desktop/스크린샷 2020-05-23 오전 10.16.00.png",cv2.IMREAD_GRAYSCALE)#흑백의 범위
plt.imshow(gray)
plt.show()

gray = cv2.resize(255 - gray, (28,28))
test_num = gray.flatten() / 255.0
test_num = test_num.reshape(-1,28,28,1)
print('The Answer is : ' , model.predict_classes(test_num))


