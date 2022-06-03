from funzioni import algoritmo
import matplotlib.pyplot as plt
import numpy
fail=algoritmo.algoritmo(0)
print(fail)
img = fail.reshape((28, 28))
plt.title('Label is ')
plt.imshow(img, cmap='gray')
plt.savefig('risultati/fail1.png')
numpy.save('risultati/array.npy', fail)