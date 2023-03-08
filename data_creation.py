import os
import tensorflow as tf
import pandas as pd


# загрузка данных
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.fashion_mnist.load_data()


# создание директорий
os.mkdir("train")
os.mkdir("test")


# запись numpy.ndarray в pandas.dataframe
df_x_train = pd.DataFrame(x_train.reshape(60000, 784))
df_y_train = pd.DataFrame(y_train)
df_x_test = pd.DataFrame(x_test.reshape(10000, 784))
df_y_test = pd.DataFrame(y_test)


# запись полученных датафреймов в .csv
df_x_train.to_csv("train/x_train.csv")
df_y_train.to_csv("train/y_train.csv")
df_x_test.to_csv("test/x_test.csv")
df_y_test.to_csv("test/y_tes.csv")


print("Данные успешно загружены!")
