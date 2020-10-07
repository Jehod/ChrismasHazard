from random import shuffle

from entity.participant import Participant
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


def see_possibilities(participants):
    """
    methode pour prevoir les cas irresolvables
    :param participants:
    :return: boolean
    """
    exclusions = []
    names = []

    # on recupere les exclusions ( et les names en passant)
    for part in participants:

        current: Participant = participants[part]
        if current.exclusion:
            exclusions.append(current.exclusion)
        names.append(current.name)
        if current.exclusion and not current.exclusion in participants:
            print(f"!!! l'exclusion {current.exclusion} ne correspond à aucun participant")
            return False

    if not exclusions:
        return True

    for name in names:

        if exclusions.count(name) > (len(names) - 2):
            print(f"!!! le participant {name} est trop exclu et ne pourra etre attribué")
            return False

        # cas particulier croisé du 3
        if len(names) == 3 and len(exclusions) > 1:
            excl = participants[name].exclusion

            if participants[excl].exclusion == name:
                print(f"!!! {name} et {excl} sont en exclusion croisée et rendront les associations impossibles.")
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

    if not see_possibilities(participants):
        return {}

    complete = False
    couples = None
    count = 50
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
                count = 50
            else:
                return {}

    return couples
