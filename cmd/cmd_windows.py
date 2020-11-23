from IHM.root_window import RootWindow
from entity.participant import Participant


def manual_entry():
    """
    serie de input pour que l'utilisateur donne les participants
    :return:
    """
    nbr_participants = 0
    succes = False
    participants = {}
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
        elif nom in participants.keys():
            print("!!! Ce nom a déjà été donné.")
        else:
            exclusion = input("Si ce participant ne peut etre associé à une personne, nommez la."
                              " Sinon appuyez sur Entrée")

            par = Participant(nom, exclusion)
            participants[nom] = par
            print(par.__str__())
            nbr_participants = nbr_participants - 1
    return participants


def opening():
    """
    serie de message d'entree et de choix primaire
    :return:
    """
    print(" *********** Bienvenue dans le ChrismasHazard ***************")
    print("")
    root_window = RootWindow()
    root_window.run()

    ok = False
    mode = '1'
    while not ok:
        mode = input("Voulez-vous entrer les participants manuellement (1) ou avez-vous une liste en csv(2) ?  1 ou 2")
        if mode == '1' or mode == '2':
            ok = True
        else:
            print("!!!  veuillez repondre par 1 (saisie manuelle)  ou 2 (liste en csv)")

    return mode
