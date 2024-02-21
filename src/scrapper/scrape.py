import random
import re
import uuid

from selenium import webdriver
from selenium import webdriver
from selenium.common import ElementNotInteractableException, StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

import time

SEARCH_BOX = ""
contact = "Name"
text = "Hey, this message was sent using Selenium"
driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com")


# def get_chats():
#     '''Traverses the WhatsApp chat-pane via keyboard input and collects chat information such as person/group name, last chat time and msg'''
#
#     print("Loading your chats...", end="\r")
#
#     # Wrap entire function in a retryable try/catch because chat-pane DOM changes frequently due to users typing, sending messages, and occasional WhatsApp notifications
#     retry_attempts = 0
#     while retry_attempts < 3:
#         retry_attempts += 1
#
#         # Try traversing the chat-pane
#         try:
#             contactSpan = f'//span[@title="{contact}"]'
#             selected_contact = driver.find_element(By.XPATH, contactSpan)
#             selected_contact.click()
#
#             chats = []
#
#             # Descend through the chats
#             while True:
#
#                 # Get the time (xpath == div element that holds last chat time e.g. 'Wednesday' or '1/1/2021')
#                 last_chat_time = selected_contact.find_element(By.XPATH,
#                                                             "./div/div[2]/div/div[2]").text
#                 print(last_chat_time)
#                 # Get the last message (xpath == div element that holds a span w/ title attribute set to last chat message)
#                 last_chat_msg_element = selected_contact.find_element(By.XPATH,
#                                                                    "./div/div[2]/div[2]/div")
#                 last_chat_msg = last_chat_msg_element.find_element_by_tag_name(
#                     'span').get_attribute('title')
#                 print(last_chat_msg)
#
#                 # Strip last message of left-to-right directional encoding ('\u202a' and '\u202c') if it exists
#                 if '\u202a' in last_chat_msg or '\u202c' in last_chat_msg:
#                     last_chat_msg = last_chat_msg.lstrip(
#                         u'\u202a')
#                     last_chat_msg = last_chat_msg.rstrip(
#                         u'\u202c')
#
#                 # Check if last message is a group chat and if so prefix the senders name to the message
#                 last_chat_msg_sender = last_chat_msg_element.find_element_by_tag_name(
#                     'span').text
#                 if '\n: \n' in last_chat_msg_sender:
#                     # Group have multiple spans to separate sender, colon, and msg contents e.g. '<sender>: <msg>', so we take the first item after splitting to capture the senders name
#                     last_chat_msg_sender = last_chat_msg_sender.split('\n')[
#                         0]
#
#                     # Prefix the message w/ senders name
#                     last_chat_msg = f"{last_chat_msg_sender}: {last_chat_msg}"
#
#                 # Store chat info within a dict
#                 chat = {"name": name_of_chat,
#                         "time": last_chat_time, "message": last_chat_msg}
#                 chats.append(chat)
#
#             # Navigate back to the top of the chat list
#             chat_search.click()
#             chat_search.send_keys(Keys.DOWN)
#
#             print("Success! Your chats have been loaded.")
#             break
#
#         # Catch errors related to DOM changes
#         except (StaleElementReferenceException, ElementNotInteractableException) as e:
#             if retry_attempts == 3:
#                 # Make sure we grant user option to exit if DOM keeps changing while scanning chat list
#                 print("This is taking longer than usual...")
#                 while True:
#                     response = input(
#                         "Try loading chats again (y/n)? ")
#                     if response.strip().lower() in {'n', 'no'}:
#                         print(
#                             'Error! Aborting chat load by user due to frequent DOM changes.')
#                         if type(e).__name__ == 'StaleElementReferenceException':
#                             raise StaleElementReferenceException
#                         else:
#                             raise ElementNotInteractableException
#                     elif response.strip().lower() in {'y', 'yes'}:
#                         retry_attempts = 0
#                         break
#                     else:
#                         continue
#             else:
#                 pass
#
#     return chats
#

print("Scan QR Code, And then Enter")
input()
print("Logged In")
inp_xpath_search = "//div[@title='Search input textbox']"
TEXT_SPAN_CLASS = "_11JPr selectable-text copyable-text"
# Wait for the element to be visible
driver.implicitly_wait(15)
input_box_search = driver.find_element(By.XPATH, inp_xpath_search)

input_box_search.click()
time.sleep(2)
input_box_search.send_keys(contact)
time.sleep(2)
contactSpan = f'//span[@title="{contact}"]'
selected_contact = driver.find_element(By.XPATH, contactSpan)
selected_contact.click()
driver.implicitly_wait(10)
# Find all the divs with the specified class using XPath
elements = driver.find_elements(By.XPATH, '//div[contains(@class, "cm280p3y to2l77zo n1yiu2zv c6f98ldp ooty25bp oq31bsqd")]')
print(elements)
# Extract the date and message from each div and store in a dictionary
messages_dict = {}
for element in elements:
    # Extract the date from the data-pre-plain-text attribute
    date_text = element.get_attribute('data-pre-plain-text')

    # Extract the message text
    message_text = element.find_element(By.XPATH, './/span[contains(@class, "_11JPr selectable-text copyable-text")]').text
    print(message_text)
    # Generate a random ID
    message_id = random.randint(1000,  9999)
    id = uuid.uuid4()
    # Store the date and message in the dictionary
    messages_dict[str(id)] = {
        'id': message_id,
        'text': message_text
    }
# get_chats(driver)
# inp_xpath = '//div[@class="_2S1VP copyable-text selectable-text"][@contenteditable="true"][@data-tab="1"]'
# input_box = driver.find_element(By.XPATH, inp_xpath)
# time.sleep(2)
# input_box.send_keys(text + Keys.ENTER)
# time.sleep(2)
# driver.quit()
