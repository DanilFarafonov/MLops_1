import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

x_train = pd.read_csv("train/x_train_preprocessing.csv")
y_train = pd.read_csv("train/y_train_preprocessing.csv")

model = Sequential()
model.add(Dense(800, input_dim=784, activation="relu"))
model.add(Dense(10, activation="softmax"))
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

print(model.summary())

model.fit(x_train, y_train, 
          batch_size=200, 
          epochs=50,  
          verbose=1)
model.save('model')
print('Обучение модели выполнено')