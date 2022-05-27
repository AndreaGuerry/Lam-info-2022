from fitnessFonction import *
def compare(father, son):
    fffather=fitnessFonction(father)
    ffson=fitnessFonction(son)
    if ffson<=0:
        return son
    elif fffather<=0:
        return father
    else:
        if ffson<fffather:
            return son
        else:
            return father