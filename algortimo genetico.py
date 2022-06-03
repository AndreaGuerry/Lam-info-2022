from funzioni import algoritmo
import matplotlib.pyplot as plt
fail=algoritmo.algoritmo(0)
print(fail)
img = fail.reshape((28, 28))
img = fail.reshape((28, 28))
plt.title('Label is ')
plt.imshow(img, cmap='gray')
plt.savefig('risultati/fail1.png')