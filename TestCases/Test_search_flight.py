import pytest
import softest
from Pages.Yatra_launch_page import LaunchPage
from Utilities.Utils import Utils
from ddt import ddt, data, file_data, unpack

# TODO Execute the following test case
# 1. launch the browser and opening the travel website
# 2. Select depart_from location
# 3. provide going from location
# 4. Select the departure date
# 5. Click on the flight search button
# 6. select the filter-1 stop
# 7. verify the filtered results show flights having only 1 stop


@pytest.mark.usefixtures("setup")
@ddt
class TestSearchAndVerifyFilter(softest.TestCase):
    log = Utils.custom_logger()
    
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.launch_page = LaunchPage(self.driver)
        self.util = Utils()

    # First Test Case
    # @data(("New Delhi", "New", "New York (JFK)", "20/12/2021", "1 Stop"), ("BOM", "New", "New York (JFK)", "31/12/2021", "2 Stop"))
    # @unpack
    # @file_data("../TestData/test_data.json")
    @data(*Utils.read_data_from_excel("C:\\Users\\BS238\\PycharmProjects\\AutomationFramework\\TestData\\test_data.xlsx", "Sheet"))
    @unpack
    def test_search_flight_using_1_stop(self, going_from, going_to, search_to,  date, stops):
        # Manage all object in one line
        search_flight = self.launch_page.search_flight(going_from, going_to, search_to, date)
        # Dynamic scroll the full page
        self.launch_page.page_scroll()
        # 6. select the filter-1 stop
        search_flight.filter_flight_by_stop(stops)
        # 7. verify the filtered results show flights having only 1 stop
        all_stop1 = search_flight.get_search_flight_results()
        self.log.info(all_stop1)
        self.util.assert_list_item_text(all_stop1, stops)


