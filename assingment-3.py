from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome webdriver
driverFile = webdriver.Chrome()

# Open the Canadian Tire website
driverFile.get("https://www.canadiantire.ca/en.html")

# Click on the "Hot Sale" link
sale_link = WebDriverWait(driverFile, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//a[@href='/en/promotions/hot-sale.html']"))
)
sale_link.click()

# Wait for the specific product link to be clickable
product_link_main = WebDriverWait(driverFile, 10).until(
    EC.element_to_be_clickable(
        (By.XPATH, "//a[@href='/en/pdp/hoover-onepwr-emerge-jumpstart-cordless-stick-vacuum-kit-0437100p.html#srp']"))
)
product_link_main.click()

# Wait for the "Add to Cart" button to be clickable and click it
add_to_cart = WebDriverWait(driverFile, 10).until(
    EC.element_to_be_clickable((By.ID, "add-to-cart"))
)
add_to_cart.click()

# Wait for the "Continue to Cart" button to be clickable and click it
next_to_cart_button = WebDriverWait(driverFile, 20).until(
    EC.element_to_be_clickable((By.ID, "footer-btn"))
)
next_to_cart_button.click()

# Close the webdriver
driverFile.quit()
