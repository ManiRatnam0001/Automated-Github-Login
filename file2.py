from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
import time as ti


def login_github():
        usrnm=input("usrnm:")
        pswrd=input("pswrd:")
        firefox_options = Options()

        driver = webdriver.Edge(options=firefox_options)

        wait = WebDriverWait(driver, 20)
        driver.get("https://github.com/login")

        LOCATOR_USERNAME = (By.ID, 'login_field')
        LOCATOR_PSWD = (By.ID, 'password')
        Login = (By.NAME, 'commit')
        OTP = (By.NAME, 'otp')
        Vfctn = (By.XPATH, 'submit')
        shw_mr = (By.XPATH, "submit")
        try:
            wait.until(EC.presence_of_element_located(LOCATOR_USERNAME)).send_keys(usrnm)
        except:
            print("error in finding username field")
        try:
            wait.until(EC.presence_of_element_located(LOCATOR_PSWD)).send_keys(pswrd)
        except:
            print("error in password field")
        try:
            wait.until(EC.element_to_be_clickable(Login)).click()
        except:
            print("error in finding login field")


        if bool(driver.get("https://github.com/sessions/verified-device"))==True:
            mail_otp = input("Enter the OTP")
            try:
                wait.until(EC.presence_of_element_located(OTP)).send_keys(mail_otp)
            except:
                print("OTP slot not found")
            try:
                wait.until(EC.element_to_be_clickable(Vfctn)).click()
            except:
                 print("Verification failed")

        else :
            print("Verification hata diya babu bhaiyya")
            driver.get("https://github.com")

login_github()


