# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service as ChromeService
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
# from time import sleep

# # 1. Configuration (Mandatory for Codespaces/Headless Linux)
# chrome_options = Options()
# chrome_options.add_argument("--headless")
# chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument("--disable-dev-shm-usage")

# # 2. Initialize the Driver ONCE with options
# driver = webdriver.Chrome(
#     service=ChromeService(ChromeDriverManager().install()), 
#     options=chrome_options
# )

# # 3. Setting a wait time for elements to appear
# driver.implicitly_wait(10)

# try:
#     # Define URL
#     url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"

#     # Load the webpage (Do NOT re-initialize the driver here)
#     driver.get(url)
#     print(f"Navigated to: {driver.title}")

#     # find the first name field 
#     first_name = driver.find_element(By.XPATH, '//*[@id="input-firstname"]')
#     # fill out the first name field
#     first_name.send_keys("Kelechi")

#     # find the last name field 
#     last_name = driver.find_element(By.XPATH, '//*[@id="input-lastname"]')
#     # find the last name field 
#     last_name.send_keys("Okoroigwe")

#     # find the email field 
#     email = driver.find_element(By.XPATH, '//*[@id="input-email"]')
#     # fill in the email field 
#     email.send_keys("your@email.com")

#     # find the telephone field 
#     telephone = driver.find_element(By.XPATH, '//*[@id="input-telephone"]')
#     # fill in the telephone field 
#     telephone.send_keys("+44123456789")

#     # find the password field 
#     password = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')
#     # fill in the password field 
#     password.send_keys("yourpassword")  #copy Xpath

#     # find the password confirm field 
#     password_confirm = driver.find_element(By.XPATH, '//*[@id="input-confirm"]')
#     # fill in the password confirm field 
#     password_confirm.send_keys("yourpassword")  #copy Xpath

#     # find the desired response to the newsletter subscribe field
#     newsletter_subscribe = driver.find_element(By.XPATH, '//*[@id="content"]/form/fieldset[3]/div/div/div[2]/label')
#     # click on it 
#     newsletter_subscribe.click()

#     # find the checkbox for agreeing to the terms 
#     agree = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/div/label')
#     # click on the agree checkbox
#     agree.click()

#     # find the continue button
#     continue_button = driver.find_element(By.XPATH, '//*[@id="content"]/form/div/div/input')
#     # click on the continue button
#     continue_button.click()

#     # scroll down by 200 units to view the lower part of the page
#     driver.execute_script("window.scrollTo(0, window.scrollY + 200)")
#     print("Form submitted successfully!")
#     # pause the program for 5 seconds to view the results
#     sleep(5)

# except Exception as e:
#     print(f"An error occurred: {e}")

# finally:
#     # 5. Always close the browser
#     driver.quit()


from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# 1. Setup Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--window-size=1920,1080") # Set a standard screen size

driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()), 
    options=chrome_options
)

driver.implicitly_wait(10)

try:
    url = "https://ecommerce-playground.lambdatest.io/index.php?route=account/register"
    driver.get(url)
    
    # CRITICAL: Wait for the page to settle
    sleep(3) 
    print(f"Page loaded: {driver.title}")

    # Use clear() before send_keys to ensure the field is ready
    def fill_field(xpath, value):
        element = driver.find_element(By.XPATH, xpath)
        element.clear()
        element.send_keys(value)
        return element

    # Fill fields
    fill_field('//*[@id="input-firstname"]', "Kelechi")
    fill_field('//*[@id="input-lastname"]', "Okoroigwe")
    fill_field('//*[@id="input-email"]', "kelechi_test_auto@mail.com")
    fill_field('//*[@id="input-telephone"]', "07123456789")
    
    # Fixed the Password vs Confirm Password XPATH mismatch
    fill_field('//*[@id="input-password"]', "Password123!")
    fill_field('//*[@id="input-confirm"]', "Password123!")

    # Interactions
    driver.find_element(By.CSS_SELECTOR, "label[for='input-newsletter-no']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='input-agree']").click()
    
    # Take a screenshot BEFORE clicking continue to verify fields are full
    driver.save_screenshot("form_filled.png")
    print("Screenshot saved: form_filled.png - Check this file to see the filled fields!")

    # Click Continue
    driver.find_element(By.XPATH, "//input[@value='Continue']").click()
    
    sleep(2)
    driver.save_screenshot("after_submit.png")
    print("Form submission attempted.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    driver.quit()