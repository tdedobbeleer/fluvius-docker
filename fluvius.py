from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from flask import Flask, Response

import re

app = Flask(__name__)
ean_regex = r"^[0-9]+$"

@app.route("/api/fluvius/<ean>/status")
def getEanStatus(ean):
    if not re.match(ean_regex, ean):
        return Response("EAN number is faulty", 400)

    #if all is well, it's go time
    try:
        options = webdriver.ChromeOptions()
        options.binary_location = '/usr/bin/chromium'

        driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=options)
        driver.get("https://www.fluvius.be/nl/factuur-en-tarieven/vertraging-energiefactuur")
        
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

        if "De gegevens voor deze EAN-code zitten spijtig genoeg geblokkeerd in de systemen.".lower() in text.lower(): 
            return Response("Blocked in system.", 404)
        else:
            return Response("Ean is found in system.", 200)

    finally:
        driver.quit()
