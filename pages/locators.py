from selenium.webdriver.common.by import By


class BasePageLocators():
    # locators for values
    TIME_HOUR = (By.ID, "hr")
    TIME_MIN = (By.ID, "min")
    TIME_SEC = (By.ID, "sec")

    # locator for button
    SUBMIT = (By.ID, "btnCalculate")

    # race data
    HOURS_FACT = "0"
    MIN_FACT = "60"
    SEC_FACT = "1"
    CURRENT_PACE = (7 * 60) + 55  # hours * 60 + sec

    # open training fields
    TRAINING = (By.ID, "ui-id-2")
    EASY_PACE = (By.XPATH, "//div[1]/div/div[3]/div[2]/table/tbody/tr[1]/td[4]")

    # Information page
    LINK_TO_INFO_PAGE = (By.XPATH, "//a[contains(text(), 'Full Instructions')]")
    VIDEO_FRAME = (By.XPATH, "//iframe")







