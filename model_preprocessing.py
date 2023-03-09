import pandas as pd
import tensorflow as tf


# преобразование файлов .csv в датафреймы
df_x_train = pd.read_csv("train/x_train.csv")
df_y_train = pd.read_csv("train/y_train.csv")
df_x_test = pd.read_csv("test/x_test.csv")
df_y_test = pd.read_csv("test/y_test.csv")


# преобразование pandas.dataframe в numpy.ndarray
x_train = df_x_train.to_numpy()
y_train = df_y_train.to_numpy()
x_test = df_x_test.to_numpy()
y_test = df_y_test.to_numpy()


# нормализация данных
x_train = x_train / 255
x_test = x_test / 255


# преобразование меток в формат one hot encoding
y_train = tf.keras.utils.to_categorical(y_train, 10)
y_test = tf.keras.utils.to_categorical(y_test, 10)


# преобразование numpy.ndarray в pandas.dataframe
df_x_train = pd.DataFrame(x_train)
df_y_train = pd.DataFrame(y_train)
df_x_test = pd.DataFrame(x_test)
df_y_test = pd.DataFrame(y_test)


# запись полученных датафреймов в .csv
df_x_train.to_csv("train/x_train_preprocessing.csv", index=False)
df_y_train.to_csv("train/y_train_preprocessing.csv", index=False)
df_x_test.to_csv("test/x_test_preprocessing.csv", index=False)
df_y_test.to_csv("test/y_test_preprocessing.csv", index=False)


print('Предобработка данных выполнена')
