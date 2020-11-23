from asyncio import constants

from cmd import cmd_windows
from cmd.cmd_windows import opening
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
        participants = read(constants.csv_name)
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
    result = None
    all_participants = None

    mode_op = opening()
    all_participants = incorporate(mode_op)
    result = mix(all_participants)
    communicate(result, all_participants, False)

    print("")
    print("Merci d'avoir participé.")
