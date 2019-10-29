  
import smtplib
from email.mime.text import MIMEText


def send_mail(tipo, nombre, estado, mail, descripcion):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = '81286f84c678c7'
    password = '401c692d9ee88d'
    message = f"<h3>New Feedback Submission</h3><ul><li>Tipo: {tipo}</li><li>Nombre: {nombre}</li><li>Estado: {estado}</li><li>Mail: {mail}</li><li>Descripcion: {descripcion}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Lexus Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())