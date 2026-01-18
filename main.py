import os, sys, logging
from dotenv import load_dotenv
from src.scraper import download_boleto
from src.mailer import send_mail
from src.utils import set_download_path, empty_downloads, configure_logging

def main():
    load_dotenv()
    cpf = os.getenv('CPF_PROVEDOR')
    download_path = set_download_path()
    empty_downloads(download_path)
    configure_logging()

    try:
        logging.info("Starting application...")
        final_boleto_path = download_boleto(download_path, cpf)
        logging.info("Internet bill succesfully downloaded and saved.")
        send_mail(final_boleto_path)
    except Exception as e:
            logging.error("Application failed to start. Log: ", exc_info=e)
            sys.exit(1)

if __name__ == "__main__":
    main()