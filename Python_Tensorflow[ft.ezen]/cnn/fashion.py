import tensorflow as tf
from tensorflow import keras
import matplotlib.pyplot as plt
import numpy as np
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']
class Fashion:
    def modeling(self) -> object:
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) \
            = fashion_mnist.load_data()
        '''
        print('트레인 행 : %d, 열 : %d, ' % (train_images.shape[0], train_images.shape[1]))
        print('테스트 행 : %d, 열 : %d, ' % (test_images.shape[0], test_images.shape[1]))
        실행결과
        트레인 행 : 60000, 열 : 28, 
        테스트 행 : 10000, 열 : 28, 
        plt.figure()
        plt.imshow(train_images[3])
        plt.colorbar()
        plt.grid(False)
        plt.show()
        '''
        train_images / 255.0
        test_images / 255.0
        plt.figure(figsize=(10,10))
        for i in range(25):
            plt.subplot(5,5, i + 1)
            plt.xticks([])
            plt.ylabel([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(class_names[train_labels[i]])
        # plt.show()
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=(28, 28)),
            keras.layers.Dense(128, activation='relu'),
            keras.layers.Dense(10, activation='softmax')
        ])
        """        
        relu ( Recitified Linear Unit 정류한 선형 유닛)        
        미분 가능한 0과 1사이의 값을 갖도록 하는 알고리즘        
        softmax        
        nn (neural network )의 최상위층에서 사용되며 
        classfication 을 위한 function        
        결과를 확률값으로 해석하기 위한 알고리즘        
        """
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        # 모델 학습
        model.fit(train_images, train_labels, epochs=5)
        # 모델 평가
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
        print('테스트 정확도 : ', test_acc)
        # 테스트 정확도 :  0.8075
        # 모델 예측
        predictions = model.predict(test_images)
        print(predictions[0])
        '''
        [3.0462004e-11 1.9878127e-10 2.8517895e-26 5.5107477e-16 2.5601745e-17
        2.6590964e-01 1.6214647e-14 3.0300125e-02 1.4937678e-08 7.0379025e-01]
        '''
def plot_image(i, predictions_array, true_label, img):
    predictions_array, true_label, img = predictions_array[i], true_label[i], img[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    plt.imshow(img, cmap=plt.cm.binary)
    predicted_label = np.argmax(predictions_array)
    if predicted_label == true_label:
        color = 'blue'
    else:
        color = 'red'
    plt.xlabel("{} {:2.0f}% ({})".format(class_names[predicted_label],
                                100*np.max(predictions_array),
                                class_names[true_label]),
                                color=color)
def plot_value_array(i, predictions_array, true_label):
    predictions_array, true_label = predictions_array[i], true_label[i]
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])
    thisplot = plt.bar(range(10), predictions_array, color="#777777")
    plt.ylim([0, 1])
    predicted_label = np.argmax(predictions_array)
    thisplot[predicted_label].set_color('red')
    thisplot[true_label].set_color('blue')
if __name__ == '__main__':
    f = Fashion()
    f.modeling()
