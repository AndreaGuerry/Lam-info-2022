from funzioni import fitnessFonction


def compare(father, son, numero):
    fffather = fitnessFonction.fitnessFonction(father, numero)
    ffson = fitnessFonction.fitnessFonction(son, numero)
    if ffson <= 0:
        return son
    elif fffather <= 0:
        return father
    else:
        if ffson < fffather:
            return son
        else:
            return father
