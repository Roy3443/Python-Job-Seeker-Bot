from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3921824145&geoId=102713980&keywords"
           "=python%20developer&location=India&origin=JOB_SEARCH_PAGE_LOCATION_AUTOCOMPLETE&refresh=true")

ACCOUNT_EMAIL = "YOUR_EMAIL"
ACCOUNT_PASSWORD = "YOUR_PASSWORD"
PHONE = "YOUR_PHONE_NUMBER"

sign_in = driver.find_element(By.LINK_TEXT, value="Sign in")
sign_in.click()

email = driver.find_element(By.ID, value="username")
email.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, value="password")
password.send_keys(ACCOUNT_PASSWORD)
submit = driver.find_element(By.CSS_SELECTOR, value=".login__form_action_container button")
submit.click()

time.sleep(2)
easy_apply = driver.find_element(By.XPATH, value='/html/body/div[5]/div[3]/div[4]/section/div/section/div/div/div/ul/li[7]/div/button')
easy_apply.click()



# driver.quit()
