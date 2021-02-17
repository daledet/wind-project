import math
from sklearn.preprocessing import StandardScaler
from keras.layers import Dense
from keras.models import Model
from keras.models import Sequential
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import model_selection

df = pd.read_csv('consumption-no-areas_2020_hourly_MWh.csv')
# df = df.drop('precipitation', 1)

X = df[['temp', 'humidity', 'wind_speed', 'wind_deg', 'NO']]
y = df[['NO']]

X_train, X_test, y_train, y_test = model_selection.train_test_split(
    X, y, test_size=0.1, random_state=4)

xnorm = StandardScaler()
ynorm = StandardScaler()
X_train = xnorm.fit_transform(X_train)
X_test = xnorm.transform(X_test)
y_train = ynorm.fit_transform(np.array(y_train).reshape(-1, 1))
y_test = ynorm.transform(np.array(y_test).reshape(-1, 1))

model = Sequential()
model.add(Dense(10, input_shape=(5,), activation='relu'))
model.add(Dense(10, activation='relu'))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
print(model.summary())
model.fit(X_train, y_train, epochs=30, batch_size=32)
# predictions
trainPredict = model.predict(X_train)
testPredict = model.predict(X_test)

plt.plot(range(0, y_train.shape[0]), ynorm.inverse_transform(
    y_train), label='y_train')

plt.plot(range(y_train.shape[0], y_train.shape[0]+y_test.shape[0]),
         ynorm.inverse_transform(y_test), label='y_test')
plt.xlabel('Hours')
plt.ylabel('Mean Consumption')
plt.title('Consumption Forecast Norway - MWh')
plt.legend()
plt.show()

trainingScore = model.evaluate(X_train, y_train)
print('Training Score is : %.3f MSE (%.3f RMSE)' %
      (trainingScore, math.sqrt(trainingScore)))
testingScore = model.evaluate(X_test, y_test)
print('Testing Score is  : %.3f MSE (%.3f RMSE)' %
      (testingScore, math.sqrt(testingScore)))
