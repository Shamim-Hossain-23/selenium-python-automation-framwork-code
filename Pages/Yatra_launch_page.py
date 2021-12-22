import logging
import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from Base.Base_Driver import BaseDriver
from Pages.Search_flight_results_page import SearchFlightResults
from Utilities.Utils import Utils


class LaunchPage(BaseDriver):
    log = Utils.custom_logger()

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locations
    DEPART_FROM_FIELD = "//input[@id='BE_flight_origin_city']"
    GOING_TO_FIELD = "//input[@id='BE_flight_arrival_city']"
    GOING_TO_RESULTS_LIST = "//div[@class='viewport']//div//div//div"
    DEPARTURE_DATE_FIELD = "//input[@id='BE_flight_origin_date']"
    ALL_DATES = "//div[@id='monthWrapper']//tbody//td"
    SEARCH_FLIGHTS_BUTTON = "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']"

    def get_depart_from_field(self):
        return self.driver.find_element(By.XPATH, self.DEPART_FROM_FIELD)

    def get_going_to_field(self):
        return self.driver.find_element(By.XPATH, self.GOING_TO_FIELD)

    def get_going_to_results(self):
        return self.driver.find_elements(By.XPATH, self.GOING_TO_RESULTS_LIST)

    def get_departure_date_field(self):
        return self.driver.find_element(By.XPATH, self.DEPARTURE_DATE_FIELD)

    def all_dates_field(self):
        return self.driver.find_elements(By.XPATH, self.ALL_DATES)

    def get_search_button_field(self):
        return self.driver.find_element(By.XPATH, self.SEARCH_FLIGHTS_BUTTON)

    def enter_depart_from_location(self, depart_location):
        self.get_depart_from_field().click()
        time.sleep(2)
        self.get_depart_from_field().send_keys(depart_location)
        time.sleep(2)
        self.get_depart_from_field().send_keys(Keys.ENTER)
        time.sleep(2)
    # def depart_from(self, depart_from_location):
    #     time.sleep(2)
    #     # depart_from = self.driver.find_element_by_xpath("//input[@id='BE_flight_origin_city']")
    #     depart_from = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_city']")
    #     depart_from.click()
    #     time.sleep(2)
    #     depart_from.send_keys(depart_from_location)
    #     time.sleep(2)
    #     depart_from.send_keys(Keys.ENTER)
    #     time.sleep(2)

        # Actual way to solve this problem
        # Auto suggest drop down

        # 2. provide going from location
    def enter_going_to_location(self, send_key_value, going_to_location):
        time.sleep(2)
        self.get_going_to_field().click()
        time.sleep(4)
        self.get_going_to_field().send_keys(send_key_value)
        time.sleep(4)
        search_results = self.get_going_to_results()
        for result in search_results:
            self.log.info(result.text)
            if going_to_location in result.text:
                time.sleep(2)
                result.click()
                time.sleep(2)
                break

    # def going_to(self, send_key, going_to_location):
    #     time.sleep(2)
    #     # going_to = self.driver.find_element_by_xpath("//input[@id='BE_flight_arrival_city']")
    #     going_to = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_arrival_city']")
    #     going_to.click()
    #     time.sleep(2)
    #     going_to.send_keys(send_key)
    #     # search_results = self.driver.find_elements_by_xpath("//div[@class='viewport']//div//div//div")
    #     search_results = self.driver.find_elements(By.XPATH, "//div[@class='viewport']//div//div//div")
    # 
    #     # 3. provide going from location
    #     for results in search_results:
    #         print(results.text)
    #         if going_to_location in results.text:
    #             time.sleep(2)
    #             results.click()
    #             time.sleep(2)
    #             break

    def enter_departure_date(self, departure_date):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.DEPARTURE_DATE_FIELD).click()
        time.sleep(2)
        all_dates = self.driver.find_elements(By.XPATH, self.ALL_DATES)
        time.sleep(2)
        for date in all_dates:
            if date.get_attribute("data-date") == departure_date:
                time.sleep(2)
                date.click()
                time.sleep(2)
                break

    # def select_date(self, search_date):
    #     origin = self.driver.find_element(By.XPATH, "//input[@id='BE_flight_origin_date']")
    #     time.sleep(2)
    #     origin.click()
    #     time.sleep(2)
    #     all_dates = self.driver.find_elements(By.XPATH, "//div[@id='monthWrapper']//tbody//td")
    #     time.sleep(2)
    #     for date in all_dates:
    #         print(date.get_attribute("data-date"))
    #         if date.get_attribute("data-date") == search_date:
    #             time.sleep(4)
    #             date.click()
    #             time.sleep(4)
    #             break

    # 5. Click on the flight search button
    def click_search_flight_button(self):
        time.sleep(2)
        self.driver.find_element(By.XPATH, self.SEARCH_FLIGHTS_BUTTON).click()
        time.sleep(4)

    # def click_search(self):
    #     time.sleep(4)
    #     self.driver.find_element(By.XPATH, "//div[@class='ripple-parent search-height demo-icon icon-go']//input[@id='BE_flight_flsearch_btn']").click()

    def search_flight(self, depart_location, send_key_value, going_to_location, departure_date):
        self.enter_depart_from_location(depart_location)
        self.enter_going_to_location(send_key_value, going_to_location)
        self.enter_departure_date(departure_date)
        self.click_search_flight_button()
        search_flight = SearchFlightResults(self.driver)
        return search_flight

