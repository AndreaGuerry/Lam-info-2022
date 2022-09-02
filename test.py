import tensorflow as tf
import numpy
set=numpy.load('risultati/array0.npy')

n=1
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model=tf.keras.models.load_model(
    'saved_model/my_model', custom_objects=None, compile=True, options=None
)
labelgiusto=y_train[n]
risultato=model(set.reshape(1, 28, 28)).numpy()
labeltest=numpy.argmax(risultato)
print(labeltest)
print(labelgiusto)
if labeltest!=labelgiusto:
    print("task succesfully failed")
else:
    print("c'è stato un problema")