from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from flask import Flask

import os

app = Flask(__name__)

@app.route("/api/v1/fluvius/delay")
def getFluviusDelay():

    try:
        driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub", options=webdriver.ChromeOptions())
        driver.get("https://www.fluvius.be/nl/factuur-en-tarieven/vertraging-energiefactuur")

        #Get EAN number from ENV
        ean = os.environ["EAN"]
        
        btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fluv-cookies-button-accept-all"))
        )

        btn.click()

        element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "edit-ean"))
        )

        element.send_keys(ean)

        driver.find_element(By.ID, "edit-submit").click()

        result = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, ".lookup-result__content > p:nth-child(1)"))
        )

        text = result.text

        if "De gegevens voor deze EAN-code zitten spijtig genoeg geblokkeerd in de systemen.".lower() not in text.lower(): 
            return 404
        else:
            return 200

    except KeyError: 
        return 406
    finally:
        driver.quit()
