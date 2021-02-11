import math
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense
from keras.models import Model
from keras.models import Sequential
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection

df = pd.read_csv('stavangerwind.csv')
# df = df.drop('precipitation', 1)

X = df[['temp', 'humidity', 'wind_speed', 'wind_deg']]
y = df[['wind_speed']]

X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.1, random_state=4)

xnorm = StandardScaler()
ynorm = StandardScaler()
X_train = xnorm.fit_transform(X_train)
X_test = xnorm.transform(X_test)
y_train = ynorm.fit_transform(np.array(y_train).reshape(-1, 1))
y_test = ynorm.transform(np.array(y_test).reshape(-1, 1))

model = Sequential()
model.add(Dense(512, input_shape=(4,), activation='relu'))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(64, activation='relu'))
model.add(Dense(32, activation='relu'))
model.add(Dense(16, activation='relu'))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
print(model.summary())
model.fit(X_train, y_train, epochs=10, batch_size=32)
# predictions
trainPredict2 = model.predict(X_train)
testPredict2 = model.predict(X_test)

plt.plot(range(0, y_train.shape[0]), ynorm.inverse_transform(
    y_train), label='y_train')

plt.plot(range(y_train.shape[0], y_train.shape[0]+y_test.shape[0]),
         ynorm.inverse_transform(y_test), label='y_test')
plt.xlabel('Day')
plt.ylabel('Mean Speed')
plt.title('Wind Speed Forecast')
plt.legend()
plt.show()

plt.plot(range(0, y_train.shape[0]), ynorm.inverse_transform(
    y_train), label='y_train')
plt.plot(range(y_train.shape[0], y_train.shape[0]+y_test.shape[0]),
         ynorm.inverse_transform(testPredict2), label='testPredict')

trainingScore = model.evaluate(X_train, y_train)
print('Training Score is : %.3f MSE (%.3f RMSE)' %
      (trainingScore, math.sqrt(trainingScore)))
testingScore = model.evaluate(X_test, y_test)
print('Testing Score is  : %.3f MSE (%.3f RMSE)' %
      (testingScore, math.sqrt(testingScore)))
