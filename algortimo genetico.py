from funzioni import algoritmo
import matplotlib as plt
fail=algoritmo.algoritmo()
img = father.reshape((28, 28))
plt.title('Image error ')
plt.imshow(img, cmap='gray')
plt.savefig('fail.png')
