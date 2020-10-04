from IHM import cmd_windows
from file_reader.csv_manager import read
from metier.ender import generate
from metier.mixer import mix
from metier.utils import to_string


def incorporate(mode) -> dict:
    """
    methode pour recuperer toute les participants
    :return: la liste des participants avec les eventuelles exclusions associées
    """
    if mode == '2':
        participants = read()
    else:
        participants = cmd_windows.manual_entry()

    print(f"** Recapitulatif: {to_string(participants)}")

    return participants


def opening():
    print(" *********** Bienvenue dans le ChrismasHazard ***************")
    print("")
    ok = False
    mode = '1'
    while not ok:
        mode = input("Voulez-vous entrer les participants manuellement (1) ou avez-vous une liste en csv(2) ?  1 ou 2")
        if mode == '1' or mode == '2':
            ok = True
        else:
            print("!!!  veuillez repondre par 1 (saisie manuelle)  ou 2 (liste en csv)")

    return mode


if __name__ == "__main__":
    mode_op = opening()
    all_participants = incorporate(mode_op)
    result = None
    if all_participants:
        result = mix(all_participants)
    generate(result)

    print("")
    print("Merci d'avoir participé.")
