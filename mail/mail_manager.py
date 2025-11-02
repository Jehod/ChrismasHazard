import smtplib
from email.message import EmailMessage
from mail import mail_constant, mail_technical_constant
from mail.mail_constant import ENDING_MAIL
from mail.mail_technical_constant import mail_user, password_mail, server_SMTP, port_SMTP, server_relay


def mailing(result: dict, participants):
    for parts in result:
        send_mail(participants[parts].mail, parts, result[parts])


def send_mail(candidate_mail, candidate, target):
    print("Sending mail")

    if mail_user is None or password_mail is None:
        print('User or password_mail is missing')

    toaddrs = candidate_mail  # On peut mettre autant d'adresses que l'on souhaite separe d'une virgule
    msg = EmailMessage()
    msg['Subject'] = mail_constant.SUBJECT
    msg['From'] = mail_constant.FROM
    msg['To'] = toaddrs
    msg.set_content("Bonjour " + candidate + mail_constant.CONTENT + target + ENDING_MAIL)

    try:
        with smtplib.SMTP_SSL(host=server_relay,
                              port=port_SMTP) as server:  # Avec TLS, on utilise SMTP()

            #server.set_debuglevel(1)  # Décommenter pour activer le debug

            server.connect(server_SMTP, port_SMTP)  # On indique le port TLS
            # (220, 'toto ESMTP Postfix') # Réponse du serveur
            server.ehlo()  # On utilise la commande EHLO
            # Réponse du serveur
            # (250, 'toto\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nSTARTTLS\nENHANCEDSTATUSCODES\n8BITMIME\nDSN')
            # (220, '2.0.0 Ready to start TLS') # Réponse du serveur
            server.login(mail_user, password_mail)
            # (235, '2.7.0 Authentication successful') # Réponse du serveur
            server.send_message(msg=msg)

    except Exception as e:
        print(e)
    # {} # Réponse du serveur

    # (221 2.0.0 closing connection e13sm9566633wre.60 - gsmtp)
    print("mailing finish")
