# -*- coding: utf-8 -*-

# Se importa la librería tensorflow
# #!pip install tensorflow
from keras import layers, models
from tensorflow.keras.utils import to_categorical

# Se importa librería para presentar datos
# import matplotlib.pyplot as plt

# Se importa base de datos de entrenamiento
#!pip install extra_keras_datasets
from extra_keras_datasets import emnist
(train_data, train_labels), (test_data, test_labels) = emnist.load_data(type='balanced')

# Se obtiene la información de lo que hay dentro de la variable
# train_data.shape

# Se imprime el primer dato para verificar como está la data
# train_data[0]

# Se muestra en pantalla una muestra de los datos
# plt.imshow(train_data[5])
# plt.show
# train_labels[5]

# Se crea un modelo de Keras
model = models.Sequential()
model.add(layers.Dense(512, activation='relu', input_shape=(28*28,)))
model.add(layers.Dense(47, activation='softmax'))

model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Se cuentan la cantidad de datos en la variable de entrenamiento
# len(train_data)

# Se cuentan la cantidad de datos en la variable de pruebas
# len(test_data)

# Limpieza de datos
x_train = train_data.reshape((112800,28*28))
x_train = x_train.astype('float32')/255

x_test = test_data.reshape((18800,28*28))
x_test = x_test.astype('float32')/255

y_train = to_categorical(train_labels)
y_test = to_categorical(test_labels)

# train_labels[0]
# x_train.shape
# y_train.shape

# Entrenar el modelo
model.fit(x_train, y_train, epochs=5, batch_size=128, validation_data=(x_test, y_test))

# Evaluar el proyecto usando los datos de prueba
model.evaluate(x_test,y_test)

"""https://knowyourdata-tfds.withgoogle.com/#dataset=emnist&tab=STATS&select=kyd%2Femnist%2Flabel"""