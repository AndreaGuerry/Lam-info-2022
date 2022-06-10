from funzioni import algoritmo
import matplotlib.pyplot as plt
import numpy
import tensorflow as tf
settings=open('settings')
count=settings.readline(1)
print(count)
num=0
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
result=y_train[num]
fail=algoritmo.algoritmo(num)
img = fail.reshape((28, 28))
plt.title('Image is not seen as a {result} by the ia'.format(result=result))
plt.imshow(img, cmap='gray')
plt.savefig('risultati/fail{count}.png'.format(count=count))
numpy.save('risultati/array{count}.npy'.format(count=count), fail)