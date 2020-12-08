from pages.main_page import MainPage
from pages.instraction_page import InstructionPage


def test_positive_value(browser):
    link = "https://runsmartproject.com/calculator/"
    profile_page = MainPage(browser, link)
    profile_page.open()

    # input info about user
    profile_page.fill_value_positive()

    # submit data
    profile_page.submit_data()

    # check data in training fields
    profile_page.check_data_in_training()

    # check video on instruction page
    profile_page.go_to_instruction()
    instruction_page = InstructionPage(browser, browser.current_url)
    instruction_page.check_video_on_page()


# def test_negative_value(browser):
#     link = "https://runsmartproject.com/calculator/"
#     new_user = MainPage(browser, link)
#     new_user.open()
#
#     # input info about user
#     new_user.fill_value_negative()
#     time.sleep(5)
#
#     # check field
#     try:
#         new_user.check_numbers()
#     except NoSuchElementException:
#         print('Негативные данные не прошли')
#
#     finally: print('Корректный негативный тест')
