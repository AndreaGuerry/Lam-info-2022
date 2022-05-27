from funzioni import compare
from funzioni import mutate
import tensorflow as  tf
from funzioni import fitnessFonction
import matplotlib as plt
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model=tf.keras.models.load_model(
    'saved_model/my_model', custom_objects=None, compile=True, options=None
)
def algoritmo():
    n = 0
    ancestor = x_train[0]

    father = ancestor
    son = mutate.mutate(father)
    while n != 1:
        son = mutate.mutate(father)
        father = compare.compare(father, son)
        if fitnessFonction.fitnessFonction(father) < 0 or fitnessFonction.fitnessFonction(son) < 0:
            if fitnessFonction.fitnessFonction(father) < 0:
                succesful_fail = father
            else:
                succesful_fail = son
            n = 1
            return succesful_fail
            break
        else:
            n = 0
            pass