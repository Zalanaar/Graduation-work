import csv
import numpy as np
from nolearn.dbn import DBN

#создадим просто персептрон
net = DBN([784,300,10], #количество входов и нейронов в каждом слое
          learn_rates=0.3, #скорость обучения
          learn_rate_decays=0.9, #множитель, задающий изменение скорости обучение на каждом шаге итерации
          epochs=10, #количество итераций
          verbose=1) #флаг вывода отчета обучения


#выбираем данные из файла
with open('train.csv', 'rb') as f:
    date = list(csv.reader(f))

train_date = np.array(date[1:])
labels = train_date[:, 0].astype('float')
train_date = train_date[:,1].astype('float')/255.0

net.fit(train_date, labels)
