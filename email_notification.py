# add code here to send email notification when new IFIX is released

import smtplib
from email.mime.text import MIMEText


def send_email(to, subject, message):
    '''
    A function that sends email notifications.
    '''
    msg = MIMEText(message)
    msg['To'] = to
    msg['Subject'] = subject

    # update smtp server and credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    username = '<insert your email address here>'
    password = '<insert your email password here>'

    # create a connection to the server
    server = smtplib.SMTP(smtp_server, smtp_port)

    # start an encrypted session
    server.starttls()

    # log in to your account
    server.login(username, password)

    # send the message
    server.sendmail(username, to, msg.as_string())
    server.quit()
