import os
import csv

from entity.participant import Participant
from exception.custom_exception import CustomException
from file_reader import constants


def check_format(all_parts):
    """
    verification basique du format de CSV
    :param all_parts:
    :return:
    """
    if not all_parts:
        raise CustomException("Le fichier est vide")

    first = all_parts[0]
    if first.count(',') < 3:
        raise CustomException("delimiter ")

    if first[0] != constants.hdr_name or first[1] != constants.hdr_exclusion or first[2] != constants.hdr_mail:
        raise CustomException(
            f"le csv doit avoir comme en-tete {constants.hdr_name} {constants.hdr_exclusion} {constants.hdr_mail}")


def check_conformity(row):
    """
    fait une serie de verif sur une row.
    :param row:
    :raise: customException
    """
    if not row:
        raise CustomException("Une ligne est manquante dans le fichier.")
    if not row[0]:
        raise CustomException("Une case de la 1er colonne est vide")
    if len(row) != 3:
        raise CustomException("le nombre de colonnes attendu pour chaque ligne est de 3")


def check_conformity_header(row):
    """
    check le header
    :param row:
    :raise: customException
    """

    if row[0] != constants.hdr_name or row[1] != constants.hdr_exclusion or row[2] != constants.hdr_mail:
        raise CustomException(f"le format d en tete attendu est: {constants.hdr_name}, {constants.hdr_exclusion},"
                              f" {constants.hdr_mail}")


def read(csv_name) -> dict:
    """
    pour extraire les participants du csv
    :return: dico de participant
    """
    try:
        if not os.path.exists(csv_name):
            raise CustomException(f" Aucun Csv nommé {csv_name} n'a été trouvé")

        print(f"Ouverture de {csv_name}")
        participants = {}

        with open(csv_name, newline='') as csv_file:
            all_parts = csv.reader(csv_file, delimiter=',')

            for row in all_parts:
                check_conformity(row)
                if not participants:
                    check_conformity_header(row)

                name = row[0]

                if name in participants:
                    raise CustomException(f" le nom {name} est present plusieurs fois dans le fichier")

                part = Participant(name, row[1], row[2])

                participants[name] = part

            if constants.hdr_name in participants:
                participants.pop(constants.hdr_name)
    except CustomException as ex:
        print(ex)
        return {}

    return participants
