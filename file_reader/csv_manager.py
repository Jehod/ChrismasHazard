import os
import csv

from entity.participant import Participant
from file_reader import constants

csv_name = "Participants.csv"


def read() -> dict:
    """
    pour extraire les participants du csv
    :return: dico de participant
    """
    if not os.path.exists(csv_name):
        print(f"!!!  Aucun Csv nommé {csv_name} n'a été trouvé")
        return {}

    print(f"Ouverture de {csv_name}")
    participants = {}
    with open(csv_name, newline='') as csv_file:
        all_parts = csv.reader(csv_file, delimiter=',')
        for row in all_parts:
            name = row[0]

            part = Participant(name, row[1], row[2])
            if name in participants:
                print(f"!!! le nom {name} est present plusieurs fois dans le fichier")
                return {}
            participants[name] = part

        if constants.hdr_name in participants:
            participants.pop(constants.hdr_name)

    return participants
