import tensorflow as tf
import numpy
import random
import matplotlib.pyplot as plt
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0
model=tf.keras.models.load_model(
    'saved_model/my_model', custom_objects=None, compile=True, options=None
)

def mutate(imagine):
    coordinatex = random.randrange(0, 27)
    coordinatey = random.randrange(0, 27)
    variation = random.randrange(-50, 50)
    variation = variation / 100
    imagine[coordinatex, coordinatey]=imagine[coordinatex, coordinatey]+variation
    if imagine[coordinatex, coordinatey]<0:
        imagine[coordinatex, coordinatey]=0
    elif imagine[coordinatex, coordinatey]>1:
        imagine[coordinatex, coordinatey]=1
    return imagine

def fitnessFonction(imagine):
    predictionson=model(imagine.reshape(1, 28, 28)).numpy()
    risultatopredetto=numpy.argmax(predictionson)
    risultatosecondo=numpy.argmax(numpy.delete(predictionson, risultatopredetto))
    ff=risultatopredetto-risultatosecondo
    return ff

def compare(father, son):
    fffather=fitnessFonction(father)
    ffson=fitnessFonction(son)
    if ffson<=0:
        return son
    elif fffather<=0:
        return father
#partie experimentale

    else:
        if ffson<fffather:
            return son
        else:
            return father
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
#print(imagine)
print(algoritmo())
imagine=x_train[:1]
print(imagine.reshape(1, 28, 28).shape)
print(x_train[:1].shape)