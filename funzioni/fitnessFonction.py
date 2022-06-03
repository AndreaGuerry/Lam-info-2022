import numpy
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model=tf.keras.models.load_model(
    'saved_model/my_model', custom_objects=None, compile=True, options=None
)

def fitnessFonction(imagine, numero):
    predictionson=model(imagine.reshape(1, 28, 28)).numpy()
    risultatogiusto=predictionson[0, numero]
    risultatopredetto=numpy.argmax(predictionson)
    risultatosecondo=numpy.argmax(numpy.delete(predictionson, risultatopredetto))
    ff=risultatogiusto-risultatosecondo
    return ff