import os
import random
import shutil


def verify(couples, all_participants):
    """
    test si les associations sont conformes
    :param couples:
    :param all_participants:
    :return:
    """
    for giver in couples:
        if couples[giver] == giver:
            return False
        elif couples[giver] == all_participants[giver]:
            return False

    return True


def to_string(dico):
    """
    affiche le dico plus lisible
    :param dico:
    :return:
    """
    str = ''
    for el in dico:
        str = str + "  " + el + " qui exclu " + dico[el] + " // "
    return str


def mix(all_participants: dict) -> dict:
    """
    duplique la liste et essaie d'associer les deux jusqu a ce que les contraintes soient respectées
    :param all_participants:
    :return: les couples
    """
    complete = False
    couples = None
    count = 20
    print("******  Mixage des participants ******")
    while not complete:
        print("mixe...")
        couples = {}
        # on duplique la liste pour pouvoir associer l'une a l'autre

        parts = list(all_participants.keys())
        receveurs = parts.copy()
        random.shuffle(receveurs)

        rank = 0

        for x in parts:
            couples[parts[rank]] = receveurs[rank]
            rank += 1

        complete = verify(couples, all_participants)

        count -= 1
        if count < 0:
            print(f"!!! Apres 20 essaies, aucune solution n'a été trouvée. Est ce que les régles "
                  f"d'exclusions ne rendent pas les combinaisons impossibles? ")
            print(f"Votre liste: {to_string(all_participants)}")
            retry = input("voulez vous retenter cette liste? o/n")
            if retry == 'o':
                count = 20
            else:
                return {}

    return couples


def incorporate() -> dict:
    """
    methode pour recuperer toute les participants
    :return: la liste des participants avec les eventuelles exclusions associées
    """
    nbr_participants = 0
    succes = False
    all_participants = {}
    while not succes:
        nbr_participants = input("Entrer le nombre de participants:")
        if not nbr_participants.isnumeric():
            print("!!! Donner un chiffre ou un nombre")
        elif int(nbr_participants) < 3:
            print("!!! Le nombre de participant doit etre supérieur à 2")
        else:
            succes = True

    nbr_participants = int(nbr_participants)
    while not nbr_participants == 0:
        print("**********")
        print(f"il reste {nbr_participants} participants à nommer.")

        nom: str = input(f"Nommer le nom du participant numéro {nbr_participants}: ")

        if not nom:
            print("!!! le nom ne peut etre vide")
        elif nom in all_participants.keys():
            print("!!! Ce nom a déjà été donné.")
        else:
            exclusion = input("Si ce participant ne peut etre associé à une personne, nommez la."
                              " Sinon appuyez sur Entrée")

            if exclusion == '':
                exclusion = "#"
            all_participants[nom] = exclusion
            print(f"- Participant: {nom}.  Il ne peut etre associé à: {exclusion}")
            nbr_participants = nbr_participants - 1

    print(f"** Recapitulatif: {to_string(all_participants)}")

    return all_participants


def generate(results):
    if not results:
        print("aucun resultat à afficher")
        return
    print("****  Génération des fichiers  ****")
    first_dir = "Resulats"

    if os.path.exists(first_dir):
        shutil.rmtree(first_dir)
        print("retrait de l'ancien dossier")

    os.mkdir(first_dir)
    print("genere...")
    for couple in results:
        sous_dir = first_dir + "/" + couple
        os.mkdir(sous_dir)
        path_fichier = sous_dir + "/" + couple + ".txt"
        with open(path_fichier, "a") as fichier:
            fichier.write(f"Votre personne associée est: {results[couple]}")

    print("Fin")
    print(f"Dans le dossier {first_dir}, chaque participant trouvera un dossier à son nom avec un fichier "
          "ou est inscrit la personne qui lui est associé")

    # main


if __name__ == "__main__":
    participants = incorporate()
    result = mix(participants)
    generate(result)

    print("")
    print("Merci d'avoir participé.")
