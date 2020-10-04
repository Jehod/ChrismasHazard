from entity import participant


def to_string(dico):
    """
    affiche le dico plus lisible
    :param dico:
    :return:
    """
    ts = ''
    el: participant

    for el in dico:
        ts = ts + dico[el].__str__() + " // "
    return ts
