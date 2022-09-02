import random

def mutate(imagine):
    coordinatex = random.randrange(0, 27)
    coordinatey = random.randrange(0, 27)
    variation = random.randrange(-20, 20)
    variation = variation / 100
    print(imagine[coordinatex, coordinatey])
    imagine[coordinatex, coordinatey]=imagine[coordinatex, coordinatey]+variation
    print(imagine[coordinatex, coordinatey])
    print("-------")
    if imagine[coordinatex, coordinatey]<0:
        imagine[coordinatex, coordinatey]=0
    elif imagine[coordinatex, coordinatey]>1:
        imagine[coordinatex, coordinatey]=1
    return imagine