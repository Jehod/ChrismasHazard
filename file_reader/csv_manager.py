import os
import csv
import re

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

    if first[0] != constants.HEADER_NAME or first[1] != constants.HEADER_EXCLUSION or first[2] != constants.HEADER_MAIL:
        raise CustomException(
            f"le csv doit avoir comme en-tete {constants.HEADER_NAME} {constants.HEADER_EXCLUSION} {constants.HEADER_MAIL}")


def check_mail_format(mail):
    """
    test le format simple d'un mail
    :param mail:
    :raise: CustomException
    """
    mail_format = "[^@]+@[^@]+\.[^@]+"
    if not re.match(mail_format, mail):
        raise CustomException(f"l'adresse mail {mail} n'est pas dans un format valide")


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
    if row[2]:
        check_mail_format(row[2])


def check_conformity_header(row):
    """
    check le header
    :param row:
    :raise: customException
    """
    if not row:
        raise CustomException("Une ligne d en tete est manquante.")

    if len(row) != 3 or row[0] != constants.HEADER_NAME or row[1] != constants.HEADER_EXCLUSION or row[
        2] != constants.HEADER_MAIL:
        raise CustomException(f"le format d en tete attendu est: {constants.HEADER_NAME}, {constants.HEADER_EXCLUSION},"
                              f" {constants.HEADER_MAIL}")


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

                if not participants:
                    check_conformity_header(row)
                else:
                    check_conformity(row)

                name = row[0]

                if name in participants:
                    raise CustomException(f" le nom {name} est present plusieurs fois dans le fichier")

                part = Participant(name, row[1], row[2])

                participants[name] = part

            if constants.HEADER_NAME in participants:
                participants.pop(constants.HEADER_NAME)
    except CustomException as ex:
        print(ex)
        return {}

    return participants
