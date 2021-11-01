# -*- coding: utf-8 -*-

# Se importa la librería tensorflow
# #!pip install tensorflow
from keras import layers, models
from tensorflow.keras.utils import to_categorical

# Se importa librería para crear servicios HTTP
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib import parse

# Se importa librería para trabajo con vectores y matrices
import numpy as np

# Se importa base de datos de entrenamiento
#!pip install extra_keras_datasets
from extra_keras_datasets import emnist
(train_data, train_labels), (test_data, test_labels) = emnist.load_data(type='balanced')

# Se crea un modelo de Keras
model = models.Sequential()

model.add(layers.Flatten(input_shape=(28, 28)))
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dense(47, activation='softmax'))
model.compile(optimizer='rmsprop', loss='categorical_crossentropy', metrics=['accuracy'])

# Limpieza de datos
x_train = train_data.reshape((112800,28,28))
x_train = x_train.astype('float32')/255

x_test = test_data.reshape((18800,28,28))
x_test = x_test.astype('float32')/255

y_train = to_categorical(train_labels)
y_test = to_categorical(test_labels)

# Entrenar el modelo
model.fit(x_train, y_train, epochs=10, batch_size=128)

# Se crean labels personalizados
class_names = ['Cero', 'Uno', 'Dos', 'Tres', 'Cuatro', 'Cinco', 'Seis', 'Siete', 'Ocho', 'Nueve',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
               'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
               'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
               'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
               'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 
               'y', 'z']

# Creación de servicio Web para exportar las evaluaciones
class HTTPRequestHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        print('Se accedió a la petición POST...')

        # Obtener los datos enviados en la petición
        print('Obteniendo informacion enviada...')
        CONTENT_LENGTH = int(self.headers['Content-Length'])
        data = self.rfile.read(CONTENT_LENGTH)
        data = data.decode().replace('pixeles=', '')
        data = parse.unquote(data)

        #Realizar transformacion para dejar igual que los ejemplos que usa MNIST
        print('Realizando transformación de datos...')
        arr = np.fromstring(data, np.float32, sep=",")
        arr = arr.reshape(28,28)
        arr = np.array(arr)
        arr = arr.reshape(1,28,28,1)

        # Realizar y obtener la prediccion
        print('Realizando prediccion...')
        PREDICTION_VALUES = model.predict(arr) #, batch_size=1
        PREDICTION = np.argmax(PREDICTION_VALUES)
        print("Prediccion final: " + class_names[PREDICTION])

        #Regresar respuesta a la peticion HTTP
        self.send_response(200)

        #Evitar problemas con CORS
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        # Responder la predicción
        self.wfile.write(class_names[PREDICTION].encode())

# Iniciar el servidor en el puerto 8000 para escuchar indefinidamente
# Si se queda colgado, en el administrador de tareas buscar la tarea de python y finalizar la tarea
print("Iniciando el servidor...")
server = HTTPServer(('localhost', 8000), HTTPRequestHandler)
server.serve_forever()