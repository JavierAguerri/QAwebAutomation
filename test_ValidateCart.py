import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# with pytest, you can define a fixture function that sets up and tears down a test environment.
@pytest.fixture
def driver():
    # The browser of choice is Firefox
    selenium = webdriver.Firefox()
    # It is recommended to use implicit waits - a way to set a default wait time for all elements in the script. 
    # The web driver will poll the DOM for a certain amount of time when trying to find any element.
    stdTimeout = 6
    selenium.implicitly_wait(stdTimeout)
    # Code before the yield statement is executed before the test function.
    # Code after the yield statement is executed after the test function.
    yield selenium
    # The browser will be closed after finishing the execution
    selenium.close()

# Each test case can go inside a function. It needs to be prefixed by test_ so pytest understands it is an executable test case
# driver is the Selenium WebDriver instance, and it must match the fixture name
def test_validateCart(driver):
    # Set variables for product name and ASIN (Amazon Product ID)
    productName = "Echo Dot (3.ª generación)"
    productASIN = "B07PHPXHQS"
    
    # Go to Amazon site
    driver.get("https://www.amazon.es/")

    # Accept cookies. It might not show up so wrap it in a try block, so we can continue if not present.
    try:
        driver.find_element(By.ID,"sp-cc-accept").click()
    except:
        pass

    # Input article in the search box.
    driver.find_element(By.ID,"twotabsearchtextbox").send_keys(productName)
    # Click on search
    driver.find_element(By.ID,"nav-search-submit-button").click()

    # Wait for the search results to load. 12 seconds allowed.
    wait = WebDriverWait(driver, 12)
    resultSelector = f'.s-result-item[data-asin="{productASIN}"] .s-image'
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, resultSelector))).click()

    # Click the "Add to Cart" button
    driver.find_element(By.ID,"add-to-cart-button").click()

    # Decline recommendations. It might not show up so wrap it in a try block, so we can continue if not present.
    try:
        driver.find_element(By.CSS_SELECTOR,"#abb-intl-pop-cta .abb-intl-decline").click()
    except:
        pass

    # Confirmation screen
    wait.until(EC.presence_of_element_located((By.ID, "NATC_SMART_WAGON_CONF_MSG_SUCCESS")))

    # We could assume the item has been added already, but let's do a more robust validation by checking the cart page.

    # Go to cart
    driver.find_element(By.ID,"nav-cart").click()

    # Find element added
    cartItemSelector = f'.sc-list-item[data-asin="{productASIN}"]'
    cartItem = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, cartItemSelector)))
    assert cartItem.is_displayed(), f"The item {productASIN} has not been added to the cart!"