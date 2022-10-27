from cmd import cmd_windows
from cmd.cmd_windows import opening
from constants import misc
from file_reader.csv_manager import read
from mail.mail_manager import mailing
from metier.ender import generate
from metier.mixer import mix
from metier.utils import to_string


def incorporate(mode) -> dict:
    """
    methode pour recuperer toute les participants
    :return: la liste des participants avec les eventuelles exclusions associées
    """
    if mode == '2':
        participants = read(misc.CSV_NAME)
    else:
        participants = cmd_windows.manual_entry()

    print(f"** Recapitulatif: {to_string(participants)}")

    return participants


def communicate(result, participants, mail):
    if mail:
        mailing(result, participants)
    else:
        generate(result)


if __name__ == "__main__":

    mode_op = opening()
    all_participants = incorporate(mode_op)
    result = mix(all_participants)
    communicate(result, all_participants, True)

    print("")
    print("Merci d'avoir participé.")
