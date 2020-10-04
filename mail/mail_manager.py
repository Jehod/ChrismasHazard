import smtplib
from email.message import EmailMessage
from mail import mail_constant


def send_mail(target):
    print("Sending mail")
    user = mail_constant.user
    password = mail_constant.password

    server = smtplib.SMTP(host="smtp-relay.gmail.com", port=587)  # Avec TLS, on utilise SMTP()
    # server.set_debuglevel(1)  # Décommenter pour activer le debug
    server.connect('smtp.gmail.com', 587)  # On indique le port TLS
    # (220, 'toto ESMTP Postfix') # Réponse du serveur
    server.ehlo()  # On utilise la commande EHLO
    # Réponse du serveur
    # (250, 'toto\nPIPELINING\nSIZE 10240000\nVRFY\nETRN\nSTARTTLS\nENHANCEDSTATUSCODES\n8BITMIME\nDSN')
    server.starttls()  # On appelle la fonction STARTTLS
    # (220, '2.0.0 Ready to start TLS') # Réponse du serveur
    server.login(user, password)
    # (235, '2.7.0 Authentication successful') # Réponse du serveur

    toaddrs = target  # On peut mettre autant d'adresses que l'on souhaite separe d'une virgule

    msg = EmailMessage()
    msg['Subject'] = mail_constant.SUBJECT
    msg['From'] = mail_constant.FROM
    msg['To'] = toaddrs
    msg.set_content(mail_constant.CONTENT)
    try:
        server.send_message(msg=msg)
    except smtplib.SMTPException as e:
        print(e)
    # {} # Réponse du serveur
    server.quit()
    # (221 2.0.0 closing connection e13sm9566633wre.60 - gsmtp)
    print("mailing finish")