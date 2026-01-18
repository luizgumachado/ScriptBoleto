import os, datetime, locale, logging

def set_download_path():
    download_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    download_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return download_path

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

def empty_downloads(folder_path):
    if os.path.exists(folder_path):
        for file in os.listdir(folder_path):
            full_path = os.path.join(folder_path, file)
            try:
                if os.path.isfile(full_path):
                    os.unlink(full_path)
            except Exception as e:
                print(f"Couldn't delete {full_path}: {e}")

def configure_logging():
    if not os.path.exists('logs'):
        os.makedirs('logs')

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler("logs/execution.txt", encoding='utf-8'),
            logging.StreamHandler()
        ]
    )