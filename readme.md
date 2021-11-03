# Redes Neuronales con imágenes

En este repositorio encontrarás un ejemplo practico de una red neuronal para el reconocimiento de números y letras.

# ¿Cómo Usar?
Para ejecutar esta red neuronal se necesita realizar los siguientes pasos:
- Clonar o descargar este repositorio.
```
git clone https://github.com/dlopezecha/red_neuronal_emnist.git
```
- Ejecutar el servicio en python
```
python ServicioRedNeuronal2.py
```
- Abrir la página web que hará el consumo y te permitirá dibujar los números o letras

# Tecnologías
Estas son las tecnologías usadas para crear este proyecto funcional

- [Python 3.8.8](https://www.python.org/)
- [Tensorflow 2.6.0](https://www.tensorflow.org/)
- Keras 2.6.0
- HTML5
- CSS ([Bootstrap 5.1.3](https://jquery.com/))
- JS
- [Jquery](https://jquery.com/)
  
# DataSets
El set de datos usados para realizar esta red neuronal fue la Extended Keras MNIST (EMNIST) que provee números, letras en mayusculas y letras en minusculas - [Ver Información completa](https://arxiv.org/abs/1702.05373) - [Explorar DataSet](https://knowyourdata-tfds.withgoogle.com/#dataset=emnist&tab=STATS&select=kyd%2Femnist%2Flabel) - [Ver Variantes de la implementación](https://github.com/machinecurve/extra_keras_datasets)

# Tabla de valores del DataSet

|  Tipo |    |    |    |    |    |    |    |    |    |    |    |    |    |    |
|-------|----|----|----|----|----|----|----|----|----|----|----|----|----|----|
| Label | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12 | 13 |
| Clase | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | A  | B  | C  | D  |
| Label | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25 | 26 | 27 |
| Clase | E  | F  | G  | H  | I  | J  | K  | L  | M  | N  | O  | P  | Q  | R  |
| Label | 28 | 29 | 30 | 31 | 32 | 33 | 34 | 35 | 36 | 37 | 38 | 39 | 40 | 41 |
| Clase | S  | T  | U  | V  | W  | X  | Y  | Z  | a  | b  | c  | d  | e  | f  |
| Label | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 50 | 51 | 52 | 53 | 54 | 55 |
| Clase | g  | h  | i  | j  | k  | l  | m  | n  | o  | p  | q  | r  | s  | t  |
| Label | 56 | 57 | 58 | 59 | 60 | 61 |    |    |    |    |    |    |    |    |
| Clase | u  | v  | w  | x  | y  | z  |    |    |    |    |    |    |    |    |

# Librerías Python
Las librerías que fueron utilizadas para crear esta red neuronal son las siguientes:
- tensorflow
- keras
- extra_keras_datasets
- numpy
- urllib
- http.server

# Autores
Se listan a continuación los autores de este repositorio:
- Daniel López Echavarría