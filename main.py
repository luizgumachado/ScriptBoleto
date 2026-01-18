import os, sys
from dotenv import load_dotenv
from src.scraper import set_download_path, download_boleto
from src.mailer import send_mail

def main():
    load_dotenv()
    cpf = os.getenv('CPF_PROVEDOR')
    download_path = set_download_path()

    try:
        final_boleto_path = download_boleto(download_path, cpf)
        if final_boleto_path:
            send_mail(final_boleto_path)
        else:
            print("Falha ao salvar o arquivo no disco.")
    except Exception as e:
            print(f"Ocorreu um erro durante a execução: {e}")
            sys.exit(1)

if __name__ == "__main__":
    main()