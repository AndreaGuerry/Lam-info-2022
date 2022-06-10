from funzioni import algoritmo
import matplotlib.pyplot as plt
import numpy
import tensorflow as tf
num=0
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
result=y_train[num]
fail=algoritmo.algoritmo(num)
print(fail)
img = fail.reshape((28, 28))
plt.title('Image is not seen as a {result} by the ia"format(label=label)
plt.imshow(img, cmap='gray')
plt.savefig('risultati/fail1.png')
numpy.save('risultati/array.npy', fail)