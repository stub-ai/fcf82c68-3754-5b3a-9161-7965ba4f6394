from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def send_slack_message(user, message):
    # Initialize the Chrome driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Open the Slack workspace
    driver.get("https://app.slack.com/client")

    try:
        # Wait for the workspace to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "search_terms"))
        )

        # Find the search box, enter the user's name, and hit ENTER
        search_box = driver.find_element_by_name("search_terms")
        search_box.send_keys(user + Keys.RETURN)

        # Wait for the user's chat to load
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//div[@data-qa="message_input"]'))
        )

        # Find the message input box, enter the message, and hit ENTER
        message_input = driver.find_element_by_xpath('//div[@data-qa="message_input"]')
        message_input.send_keys(message + Keys.RETURN)

    finally:
        # Close the driver
        driver.quit()

# Replace 'username' and 'Hello, World!' with the recipient's username and your message
send_slack_message('username', 'Hello, World!')