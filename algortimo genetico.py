import matplotlib

from funzioni import algoritmo
import matplotlib as plt
fail=algoritmo.algoritmo()
print(fail)
img = fail.reshape((28, 28))
plt.title('Label is ')
plt.imshow(img, cmap='gray')
plt.savefig('fail.png')

