from pages.base_page import BasePage
from pages.locators import BasePageLocators
from selenium.webdriver.support.ui import Select
import re


class MainPage(BasePage):
    def fill_value_positive(self):
        # Insert data for activity, hours, minutes and seconds
        action = Select(self.browser.find_element_by_id("cEvent"))
        action.select_by_visible_text("10K")

        fill_hours = self.browser.find_element(*BasePageLocators.TIME_HOUR)
        fill_hours.click()
        fill_hours.send_keys(*BasePageLocators.HOURS_FACT)

        fill_min = self.browser.find_element(*BasePageLocators.TIME_MIN)
        fill_min.click()
        fill_min.send_keys(*BasePageLocators.MIN_FACT)

        fill_sec = self.browser.find_element(*BasePageLocators.TIME_SEC)
        fill_sec.click()
        fill_sec.send_keys(*BasePageLocators.SEC_FACT)

    def submit_data(self):
        # Submit button click
        submit_button = self.browser.find_element(*BasePageLocators.SUBMIT)
        submit_button.click()

    def check_data_in_training(self):
        # Open data field and take text from easy pace
        data = self.browser.find_element(*BasePageLocators.TRAINING)
        data.click()
        data_easy_pace = self.browser.find_element(*BasePageLocators.EASY_PACE)
        pace_str = data_easy_pace.text

        # re module for clear data
        pace_arr = re.findall('[0-9]+', pace_str)
        pace_arr = [int(i) for i in pace_arr]
        current_pace = [7, 20]  # current time min, sec

        # check current own pace and recommended pace
        if ((pace_arr[0] * 60) + pace_arr[1]) < ((current_pace[0] * 60) + current_pace[1]) < ((pace_arr[2] * 60) + pace_arr[3]):
            print("Current pace GOOD")
        else:
            print(f'Recommended pace from {pace_arr[0]}:{pace_arr[1]} to {pace_arr[2]}:{pace_arr[3]}')

    def go_to_instruction(self):
        info_page = self.browser.find_element(*BasePageLocators.LINK_TO_INFO_PAGE)
        info_page.click()




#    def fill_value_negative(self):

