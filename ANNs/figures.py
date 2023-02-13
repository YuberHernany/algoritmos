import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from prepross_iris_data import *

iris = load_iris()
X, y = iris.data, iris.target

X_pet = only_sepal_or_petal(X, kind='petal')
y_ver = label_binary(y, kind='versicolor')

fig, ax = plt.subplots()
ax.scatter(X_pet[:, 0][y_ver==1], X_pet[:, 1][y_ver==1], c='red')
ax.scatter(X_pet[:, 0][y_ver==0], X_pet[:, 1][y_ver==0], c='gray')
ax.set_title("Versicolor and not versicolor respect to petal")
ax.set_xlabel("Petal length")
ax.set_ylabel("Petal width")
plt.legend(['Versicolor', 'Not versicolor'])
plt.savefig('Versicolor_class.png')
# plt.show()

####################################################
# for secong figure
l_mean, w_mean = means_sepal_or_petal(X, kind='petal') # length mean and width mean
X_pet_tras = traslate_data(X_pet, l_mean, w_mean)
X_pet_tras_squared = np.square(X_pet_tras)

fig, ax = plt.subplots()
ax.scatter(X_pet_tras_squared[:, 0][y_ver==1], X_pet_tras_squared[:, 1][y_ver==1], c='red', label="Versicolor")
ax.scatter(X_pet_tras_squared[:, 0][y_ver==0], X_pet_tras_squared[:, 1][y_ver==0], c='gray', label="Not Versicolor")
ax.set_title("New representation of petals")
ax.set_xlabel("Petal squared length traslated")
ax.set_ylabel("Petal squared width traslated")
plt.legend()
plt.savefig('Versicolor_separable.png')
# plt.show()

####################################################
# for third figure about ann

import tensorflow as tf
from tensorflow import keras

model_pet = keras.models.Sequential()
model_pet.add(keras.layers.Flatten(input_shape=[2]))
model_pet.add(keras.layers.Dense(32, activation='relu'))
model_pet.add(keras.layers.Dense(32, activation='relu'))
model_pet.add(keras.layers.Dense(1, activation='sigmoid'))

model_pet.compile(loss="BinaryCrossentropy",
                optimizer='sgd',
                metrics=['accuracy'])

model_pet.fit(X_pet_tras, y_ver, epochs=100)

Lengths, Widths = meshgrid_petal_or_sepal(X, kind='petal')
points = full_points_petal_or_sepal(X, kind='petal')
points_tras = traslate_data(points, l_mean, w_mean)
preds = (model_pet.predict(points_tras) >= 0.5).astype(int)
type_iris = preds.reshape(Lengths.shape)

fig, ax = plt.subplots()
plt.contourf(Lengths, Widths, type_iris, cmap="Blues", alpha=0.4)
ax.scatter(X_pet[:, 0][y_ver==1], X_pet[:, 1][y_ver==1], c='red', label='Versicolor')
ax.scatter(X_pet[:, 0][y_ver==0], X_pet[:, 1][y_ver==0], c='gray', label='Not Versicolor')
ax.set_title("ANN versicolor deterctor")
ax.set_xlabel("Petal length")
ax.set_ylabel("Petal width")
plt.legend()
plt.savefig('Versicolor_ann.png')
# plt.show()