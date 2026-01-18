import requests, os, sys, logging
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

def download_boleto(download_path, cpf):
    options = Options()
    options.add_argument("--headless") 
    driver = webdriver.Firefox(options=options)

    logging.info("Attempting to access login page URL...")

    driver.get("https://irm.sgp.net.br/accounts/central/login")
    current_url = driver.current_url
    visited_tabs = []
    visited_tabs.append(driver.current_window_handle)

    logging.info("Login page accessed successfully. Now attempting to login...")

    cpf_field = driver.find_element(By.ID, "cpfcnpj")
    cpf_field.send_keys(cpf)
    cpf_field.send_keys(Keys.RETURN)

    try:
        WebDriverWait(driver, 5).until(EC.url_changes(current_url))
        logging.info("Logged in successfully. Now attempting to access bill page...")
        current_url = driver.current_url
        visited_tabs.append(driver.current_window_handle)
        boleto_elem = driver.find_element(By.CLASS_NAME, "media")
        boleto_name = boleto_elem.find_element(By.CSS_SELECTOR, ".font-size-sm.mb-0").text.replace(" ", "").replace(":","-").replace("/", "-")
        boleto_link = boleto_elem.find_element(By.CSS_SELECTOR, ".btn.btn-xs.btn-primary")
        boleto_link.click()
    except TimeoutException as e:
        logging.info("Couldn't login properly. Log: ", exc_info=e)
        driver.quit()
        sys.exit(1)

    try:
            WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(2))
            for handle in driver.window_handles:
                if handle not in visited_tabs:
                    driver.switch_to.window(handle)
                    break
            WebDriverWait(driver, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".print.no-print")))
            logging.info("Bill page successfully accessed. Now attempting to access PDF file...")
            current_url = driver.current_url
            visited_tabs.append(driver.current_window_handle)
            print_btn_parent = driver.find_element(By.CSS_SELECTOR, ".print.no-print")
            print_btn = print_btn_parent.find_element(By.CSS_SELECTOR, ":first-child")
            print_btn.click()
    except TimeoutException as e:
        logging.error("Couldn't open bill page. Log: ", exc_info=e)
        driver.quit()
        sys.exit(1)

    try:
        WebDriverWait(driver, 5).until(EC.number_of_windows_to_be(3))
        for handle in driver.window_handles:
            if handle not in visited_tabs:
                driver.switch_to.window(handle)
                break
        WebDriverWait(driver, 10).until(EC.url_changes("about:blank"))
        logging.info("PDF accessed successfully. Now attempting to save at 'downloads/'...")
        pdf_url = driver.current_url
        full_path = os.path.join(download_path, f"{boleto_name}.pdf")
        
        try:
            response = requests.get(pdf_url, stream=True)
            response.raise_for_status()

            with open(full_path, "wb") as pdf_file:
                for chunk in response.iter_content(chunk_size=8192):
                    pdf_file.write(chunk)
            
            logging.info(f"Bill saved at: {full_path}.")
            driver.quit()
            return full_path
        except Exception as e:
            logging.error("Error when saving PDF. Log: ", exc_info=e)
    except Exception as e:
        logging.error("Error when accessing PDF. Log: ", exc_info=e)
        driver.quit()
        sys.exit(1)