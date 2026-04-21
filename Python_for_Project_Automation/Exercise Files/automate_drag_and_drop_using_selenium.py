# import relevant libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep

# define url
url = "http://dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html"

# Setup headless options for Codespaces
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# instantiate webdriver and open a chrome browser
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)

# maximize browser window (Note: in headless this sets the virtual viewport)
driver.maximize_window()

# load the webpage
driver.get(url)

# Add your drag and drop logic below using ActionChains...