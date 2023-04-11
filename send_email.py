import smtplib
from email.message import EmailMessage


def sendEmail(sender_email, sender_password, recipient_email, subject, message, attachment_path=None):
    # Set up the email message
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg.set_content(message)
    
    # Attach an optional file to the email message
    if attachment_path:
        with open(attachment_path, 'rb') as f:
            file_data = f.read()
            file_name = f.name
        msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)
    
    # Send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)
