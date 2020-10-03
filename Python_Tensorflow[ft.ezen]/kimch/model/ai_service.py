import tensorflow.compat.v1 as tf
tf.disable_v2_behavior()
import numpy as np
from flask_restful import reqparse
class AiService:
    def service(self):
        X = tf.placeholder(tf.float32, shape=[None, 4])
        Y = tf.placeholder(tf.float32, shape=[None, 1])
        W = tf.Variable(tf.random_normal([4, 1]), name='weight')
        b = tf.Variable(tf.random_normal([1]), name='bias')
        hyothesis = tf.matmul(X, W) + b
        saver = tf.train.Saver()
        model = tf.global_variables_initializer()
        parser = reqparse.RequestParser()
        #year,avgTemp,minTemp,maxTemp,rainFall,avgPrice
        parser.add_argument('avgTemp', required=True, type=float)
        parser.add_argument('minTemp', required=True, type=float)
        parser.add_argument('maxTemp', required=True, type=float)
        parser.add_argument('rainFall', required=True, type=float)
        args = parser.parse_args()
        avgTemp = float(args['avgTemp'])
        minTemp = float(args['minTemp'])
        maxTemp = float(args['maxTemp'])
        rainFall = float(args['rainFall'])

        with tf.Session() as sess:
            sess.run(model)
            saver.restore(sess,'model/saved_model/model.ckpt')
            data = ((avgTemp,minTemp,maxTemp,rainFall),)
            arr = np.array(data, dtype =np.float32)
            x_data = arr[0:4]
            dict = sess.run(hyothesis, {X: x_data})
            print(dict[0])
        return int(dict[0])

