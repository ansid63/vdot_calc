from pages.main_page import MainPage
from pages.instraction_page import InstructionPage
import logging
import datetime


log = logging.getLogger("app")
log.addHandler(logging.FileHandler(filename="test_result.log", mode="w"))
log.setLevel(logging.INFO)


def test_positive_value(browser):
    link = "https://runsmartproject.com/calculator/"
    profile_page = MainPage(browser, link)
    profile_page.open()
    log.info(str(datetime.datetime.now()) + " Browser started")

    # input info about user
    profile_page.fill_value_positive()
    log.info(str(datetime.datetime.now()) + " Added positive values")

    # submit data
    profile_page.submit_data()
    log.info(str(datetime.datetime.now()) + " Data submitted")

    # check data in training fields
    profile_page.check_data_in_training()
    log.info(str(datetime.datetime.now()) + " Data vitrified")

    # check video on instruction page
    profile_page.go_to_instruction()
    instruction_page = InstructionPage(browser, browser.current_url)
    instruction_page.check_video_on_page()
    log.info(str(datetime.datetime.now()) + " Went to second page and check content")


