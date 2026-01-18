import datetime, locale, os
from email.message import EmailMessage
from smtplib import SMTP, SMTP_SSL

def get_curr_month():
    try:
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_TIME, 'Portuguese_Brazil')
        except locale.Error:
            print("Locale 'pt_BR.UTF-8' ou 'Portuguese_Brazil' não encontrado. Usando locale padrão.")

    now = datetime.datetime.now()
    return now.strftime('%B')

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
    message = create_message(file_path, sender, receiver)

    try:
        with SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(sender, password) # type: ignore
            smtp.send_message(message)
        print("E-mail enviado com sucesso.")
    except Exception as e:
        print(f"Falha ao enviar e-mail: {e}")
        raise