import time
import openpyxl
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# Function to read phone numbers from Excel file
# Function to read phone numbers from Excel file
def read_phone_numbers(file_path):
    phone_numbers = []
    wb = openpyxl.load_workbook(file_path)
    sheet = wb.active
    for row in sheet.iter_rows(values_only=True):
        if row[0]:  # Assuming phone numbers are in the first column (0-indexed)
            phone_numbers.append(str(row[0]))
    return phone_numbers


# Function to create a WhatsApp group and add members
def create_whatsapp_group(phone_numbers, group_name):
    driver = webdriver.Chrome()
    driver.get("https://web.whatsapp.com/")
    input("Scan the QR code and press Enter after login")

    time.sleep(10)  # Wait for the page to load

    # Click on the new chat button
    new_chat_button = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/header/div[2]/div/span/div[4]/div')
    new_chat_button.click()

    time.sleep(2)  # Wait for the new chat dialog to open

    # Click on 'New Group'
    new_group_button = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[2]/div[1]/span/div/span/div/div[2]/div[1]/div[2]')
    new_group_button.click()

    time.sleep(2)  # Wait for the new group dialog to open

    # Add Participants
    for phone_number in phone_numbers:
        search_box = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"]')
        search_box.send_keys(phone_number)
        time.sleep(2)
        search_box.send_keys(Keys.RETURN)
        time.sleep(2)

    # Enter Group Name and Create Group
    group_name_input = driver.find_element_by_xpath('//div[@class="_3FRCZ copyable-text selectable-text"][@contenteditable="true"]')
    group_name_input.send_keys(group_name)
    time.sleep(2)
    create_button = driver.find_element_by_xpath('//span[@class="_3NWy8"]/span[@data-icon="send"]')
    create_button.click()

    time.sleep(5)  # Wait for the group to be created

    driver.quit()

def main():
    excel_file_path = r"C:\Users\hp\Desktop\ML\whatsappkesathchedkahani\Book1.xlsx"  # Path to your Excel file
    group_name = "Interview"  # Name of the WhatsApp group

    phone_numbers = read_phone_numbers(excel_file_path)
    create_whatsapp_group(phone_numbers, group_name)

if __name__ == "__main__":
    main()
