import requests, os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

driver = webdriver.Firefox()

def set_driver_options():
    download_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    options = Options()
    options.add_argument("--headless")

    download_path = os.path.join(os.getcwd(), "downloads")
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    driver = webdriver.Firefox(options=options)
    return driver, download_path

def download_boleto(driver, download_path):
    driver.get("https://irm.sgp.net.br/accounts/central/login")
    current_url = driver.current_url
    visited_tabs = []
    visited_tabs.append(driver.current_window_handle)
    cpf_field = driver.find_element(By.ID, "cpfcnpj")
    cpf_field.send_keys("06996367522")
    cpf_field.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 5).until(EC.url_changes(current_url))
        current_url = driver.current_url
        visited_tabs.append(driver.current_window_handle)
        boleto_elem = driver.find_element(By.CLASS_NAME, "media")
        boleto_name = boleto_elem.find_element(By.CSS_SELECTOR, ".font-size-sm.mb-0").text.replace(" ", "").replace(":","-").replace("/", "-")
        boleto_link = boleto_elem.find_element(By.CSS_SELECTOR, ".btn.btn-xs.btn-primary")
        boleto_link.click()
    except TimeoutException:
        print(f"Couldn't login properly. Try manually later.")
        driver.quit()

    try:
            WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
            for handle in driver.window_handles:
                if handle not in visited_tabs:
                    driver.switch_to.window(handle)
                    break
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".print.no-print")))
            current_url = driver.current_url
            visited_tabs.append(driver.current_window_handle)
            print_btn_parent = driver.find_element(By.CSS_SELECTOR, ".print.no-print")
            print_btn = print_btn_parent.find_element(By.CSS_SELECTOR, ":first-child")
            print_btn.click()
    except TimeoutException:
        print(f"Couldn't open link. Try manually later.")
        driver.quit()

    try:
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(3))
        for handle in driver.window_handles:
            if handle not in visited_tabs:
                driver.switch_to.window(handle)
                break
        WebDriverWait(driver, 10).until(EC.url_changes("about:blank"))
        pdf_url = driver.current_url
        full_path = os.path.join(download_path, f"{boleto_name}.pdf")
        
        try:
            response = requests.get(pdf_url, stream=True)
            response.raise_for_status()

            with open(full_path, "wb") as pdf_file:
                for chunk in response.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)
            
            print(f"Boleto salvo em: {full_path}")
            return full_path
        except Exception as e:
            print(f"Erro ao baixar o PDF: {e}")
    except:
        print("Something went wrong.")
        driver.quit()

(driver, download_path) = set_driver_options()
download_boleto(driver, download_path)
driver.quit()