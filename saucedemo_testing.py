from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

class SauceDemoTest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome()  # Path to your ChromeDriver executable
        self.driver.maximize_window()  # Maximize the browser window

    def tearDown(self):
        self.driver.quit()  # Close the browser

    def test_login_and_checkout(self):
        self.driver.get('https://www.saucedemo.com/')  # Open Sauce Demo homepage

        # Login
        username_input = self.driver.find_element(By.ID, 'user-name')  # Find the username input field
        password_input = self.driver.find_element(By.ID, 'password')  # Find the password input field
        login_button = self.driver.find_element(By.CSS_SELECTOR, '.btn_action')  # Find the login button

        username_input.send_keys('standard_user')  # Enter the username
        password_input.send_keys('secret_sauce')  # Enter the password
        login_button.click()  # Click on the login button
        sleep(2)
        
        # Add items to the cart
        product_elements = self.driver.find_elements(By.CSS_SELECTOR,  '.inventory_item')  # Find all product elements
        add_to_cart_buttons = self.driver.find_elements(By.CSS_SELECTOR,  '.btn_inventory')  # Find all "Add to Cart" buttons
        sleep(2)

        for button in add_to_cart_buttons:
            button.click()  # Click on each "Add to Cart" button
        sleep(2)
        
        # Verify cart items count
        cart_count = self.driver.find_element(By.ID, 'shopping_cart_container')  # Find the cart items count
        self.assertEqual(int(cart_count.text), len(add_to_cart_buttons))  # Assert that the cart items count is correct
        sleep(2)
        
        # Go to the cart
        cart_link = self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link')  # Find the cart link
        cart_link.click()  # Click on the cart link
        sleep(2)

        # Checkout
        checkout_button = self.driver.find_element(By.CSS_SELECTOR, '.btn_action.checkout_button')  # Find the checkout button
        checkout_button.click()  # Click on the checkout button
        sleep(2)

        # Provide checkout information
        first_name_input = self.driver.find_element(By.ID,'first-name')  # Find the first name input field
        last_name_input = self.driver.find_element(By.ID,'last-name')  # Find the last name input field
        postal_code_input = self.driver.find_element(By.ID,'postal-code')  # Find the postal code input field
        sleep(2)

        first_name_input.send_keys('Rifky')  # Enter the first name
        sleep(1)
        last_name_input.send_keys('Kurniawan')  # Enter the last name
        sleep(1)
        postal_code_input.send_keys('123456')  # Enter the postal code
        sleep(1)

        continue_button = self.driver.find_element(By.CSS_SELECTOR, '.btn_primary.cart_button')  # Find the continue button
        continue_button.click()  # Click on the continue button

        # Verify the checkout summary
        item_total = self.driver.find_element(By.CSS_SELECTOR, '.summary_subtotal_label')  # Find the item total element
        self.assertTrue(item_total.is_displayed())  # Assert that the item total is displayed

if __name__ == '__main__':
    unittest.main()
