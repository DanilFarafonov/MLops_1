import pandas as pd
from tensorflow import keras


x_test = pd.read_csv('test/x_test_preprocessing.csv')
y_test = pd.read_csv('test/y_test_preprocessing.csv')

model = keras.models.load_model('model')

score = model.evaluate(x_test, y_test)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
