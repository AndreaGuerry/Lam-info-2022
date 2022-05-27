from funzioni import fitnessFonction
def compare(father, son):
    fffather=fitnessFonction.fitnessFonction(father)
    ffson=fitnessFonction.fitnessFonction(son)
    if ffson<=0:
        return son
    elif fffather<=0:
        return father
    else:
        if ffson<fffather:
            return son
        else:
            return father