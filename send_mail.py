import smtplib
from email.mime.text import MIMEText


def send_mail(username, password, name, lastName):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '9cb44998915205'
    password = 'ca6c93f8c8c65b'
    message = f"<h3>New new user Submission</h3><ul><li>Username: {username}</li><li>Password: {password}</li><li>Name: {name}</li><li>LastName: {lastName}</li></ul>"
    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'p1-web'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())