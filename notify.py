import smtplib, ssl
def notify_email(sender, password, receiver):
    smtp_server = 'smtp.gmail.com'
    port = 465

    message = """\
    Subject: Keyword detected!

    Keylogger has detected use of one of the banked keywords. This action has been logged.

    """

    contextt = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtp_server, port, context=contextt) as server:
        server.login(sender, password)
        server.sendmail(sender, receiver, message)