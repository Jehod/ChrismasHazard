from random import shuffle

from metier.utils import to_string


def verify(couples, participants):
    """
    test si les associations sont conformes
    :param couples:
    :param participants:
    :return:
    """
    for giver in couples:
        if couples[giver] == giver:
            return False
        elif couples[giver] == participants[giver].exclusion:
            return False

    return True


def mix(participants: dict) -> dict:
    """
    duplique la liste et essaie d'associer les deux jusqu a ce que les contraintes soient respectées
    :param participants:
    :return: les couples
    """

    if not participants:
        return {}

    complete = False
    couples = None
    count = 20
    print("******  Mixage des participants ******")
    while not complete:
        print("mixe...")
        couples = {}
        # on duplique la liste pour pouvoir associer l'une a l'autre

        parts = list(participants.keys())
        recipients = parts.copy()
        shuffle(recipients)

        rank = 0

        for x in parts:
            couples[parts[rank]] = recipients[rank]
            rank += 1

        complete = verify(couples, participants)

        count -= 1
        if count < 0:
            print(f"!!! Apres 20 essaies, aucune solution n'a été trouvée. Est ce que les régles "
                  f"d'exclusions ne rendent pas les combinaisons impossibles? ")
            print(f"Votre liste: {to_string(participants)}")
            retry = input("voulez vous retenter cette liste? o/n")
            if retry == 'o':
                count = 20
            else:
                return {}

    return couples
