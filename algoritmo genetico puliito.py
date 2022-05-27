import tensorflow as tf
import matplotlib.pyplot as plt
from mutate import *
from fitnessFonction import *
from compare import *
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model=tf.keras.models.load_model(
    'saved_model/my_model', custom_objects=None, compile=True, options=None
)


def algoritmo():
        n=0
        ancestor=x_train[0]

        father=ancestor
        son=mutate(father)
        while n!=1:
            son = mutate(father)
            father=compare(father, son)
            if fitnessFonction(father)<0 or fitnessFonction(son)<0:
                if fitnessFonction(father)<0:
                    succesful_fail=father
                else:
                    succesful_fail=son
                n=1
                img = father.reshape((28, 28))
                plt.title('Image error ')
                plt.imshow(img, cmap='gray')
                plt.savefig('fail.png')
                return succesful_fail
                break
            else:
                n=0
                pass
algoritmo()
