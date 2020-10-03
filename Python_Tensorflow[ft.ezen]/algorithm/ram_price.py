from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import mglearn
class Ramprice:
    def time_series_chart(self):
        ram_price = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH,"ram_price.csv"))
        plt.semilogy(ram_price.date, ram_price.price)
        plt.xlabel('년')
        plt.ylabel('가격')
        plt.show()
        data_train = ram_price[ram_price['date']<2000]
        data_test = ram_price[ram_price['date']>=2000]
        x_train = data_train['date'][:,np.newaxis]
        y_train = np.log(data_train['price'])
        classfier = DecisionTreeRegressor()
        tree = classfier.fit(x_train, y_train)
        lr = LinearRegression().fit(x_train, y_train)
        #test는 모든 데이터 (1960~2010)에 대해 적용한다.
        x_all = ram_price['date'].values.reshape(-1, 1)
        pred_tree = tree.predict(x_all)
        pred_tree = np.exp(pred_tree)
        pred_lr = lr.predict(x_all)
        price_lr = np.exp(pred_lr)

        plt.semilogy(ram_price['date'], pred_tree, label='Tree Predic', ls = '-', dashes=(2,1))
        plt.semilogy(ram_price['date'], pred_lr, label='Linear Predic', ls = ':')
        plt.semilogy(data_train['date'], data_train, label='Train Data', alpha=0.4)
        plt.semilogy(data_test['date'], data_test, label='Test Data')
        plt.legend(loc =1 )

        plt.xlabel('year', size=15)
        plt.ylabel('price', size=15)
        plt.show()




if __name__ == '__main__':
    this = Ramprice()
    this.time_series_chart()

