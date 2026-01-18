import os, logging
from email.message import EmailMessage
from smtplib import SMTP, SMTP_SSL
from src.utils import get_curr_month

def create_message(file_path, sender, receiver):
    month = get_curr_month()
    msg = EmailMessage()
    msg['Subject'] = 'Boleto de Internet - ' + month
    msg['From'] = sender
    msg['To'] = receiver
    msg.set_content("Olá! Segue o boleto da internet desse mês de " + month)

    with open(file_path, 'rb') as file:
        pdf_data = file.read()
        file_name = "Boleto Internet " + month

        msg.add_attachment(
            pdf_data, 
            maintype='application', 
            subtype='pdf', 
            filename=file_name
        )
    
    return msg

def send_mail(file_path):
    sender = os.getenv("EMAIL_REMETENTE")
    password = os.getenv("SENHA_REMETENTE")
    receiver = os.getenv("EMAIL_DESTINATARIO")
    logging.info("Creating email message...")
    message = create_message(file_path, sender, receiver)
    logging.info("Message created successfully. Now attempting to send email...")

    try:
        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password) # type: ignore
            smtp.send_message(message)
        logging.info("Email sent. Now Closing the application.")
    except Exception as e:
        logging.error("Failed to send email. Log: ", exc_info=e)
        raise