import time
import logging

from selenium.webdriver.common.by import By

from Base.Base_Driver import BaseDriver
from Utilities.Utils import Utils


class SearchFlightResults(BaseDriver):
    log = Utils.custom_logger(logLevel = logging.WARNING)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locator
    FILTER_BY_1_STOP_ICON = "//p[normalize-space()='1']"
    FILTER_BY_2_STOP_ICON = "//p[normalize-space()='2']"
    FILTER_BY_NON_STOP_ICON = "//p[normalize-space()='0']"
    SEARCH_FLIGHT_RESULTS = "//span[contains(text(), 'Non Stop') or contains(text(), '1 Stop') or contains(text(), '2 Stop') ]"

    def get_filter_by_1_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_1_STOP_ICON)

    def get_filter_by_2_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_2_STOP_ICON)

    def get_filter_by_non_stop_icon(self):
        return self.driver.find_element(By.XPATH, self.FILTER_BY_NON_STOP_ICON)

    def get_search_flight_results(self):
        return self.driver.find_elements(By.XPATH, self.SEARCH_FLIGHT_RESULTS)

    def filter_flight_by_stop(self, by_stop):
        if by_stop == "1 Stop":
            self.get_filter_by_1_stop_icon().click
            self.log.warning("Selected filter with 1 stop")
            time.sleep(2)
        elif by_stop == "2 Stop":
            self.get_filter_by_2_stop_icon().click
            self.log.warning("Selected filter with 2 stop")
            time.sleep(2)
        elif by_stop == "Non Stop":
            self.get_filter_by_non_stop_icon().click
            self.log.warning("Selected filter with Non stop")
            time.sleep(2)
        else:
            print("Please provide valid filter options")


    # def filter_flight(self):
    #     # 6. select the filter-1 stop
    #     all_stop = self.driver.find_elements(By.XPATH,
    #                                          "(//span[@class='dotted-borderbtm'][normalize-space()='1 Stop'])")
    #     self.driver.find_element(By.XPATH, "//p[normalize-space()='1']").click()
    #     print(len(all_stop))
