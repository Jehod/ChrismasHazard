import datetime

user = "jehod18@gmail.com"
password = "xhgo hwdw zblw azwy"
##password utilise mot de passe d'application genere depuis la boite mail
year = str(datetime.datetime.now().year)

FROM = "Le père Noël Mystère "

CONTENT = " \r\n MESSAGE AUTOMATIQUE. \r\n Tu as reçu ce mail car tu participes au Noël mystère "+year + ". \r\n \r\n" \
          "Evénement spécial cette année: Noël tombe le 25 décembre à midi! \r\n \r\n"\
          "Félicitation, la personne qui t'a été attribuée est: "

ENDING_MAIL = "\r\n \r\nMerci et Joyeux Noël "+year+" Hohoho"
SUBJECT = "Attribution du père Noël Mystère "+year
