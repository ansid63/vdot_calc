from pages.base_page import BasePage
from pages.locators import BasePageLocators
import logging
from selenium.webdriver.support.ui import Select
import re


class InstructionPage(BasePage):
    def check_video_on_page(self):
        video = self.browser.find_element(*BasePageLocators.VIDEO_FRAME)
        video_res = video.get_attribute("src")
        assert video_res == "https://www.youtube.com/embed/bidIUgYg5DQ", "Wrong link"
        logging.info('Right link on video')

