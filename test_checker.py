import time
import unittest
from selenium import webdriver

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.PhantomJS()
        self.base_url = "http://www.ksrtc.in/oprs-web/"

    def test_title(self):
        self.driver.get(self.base_url)

        from_place = self.driver.find_element_by_name("fromPlaceName")
        from_place.send_keys("BANGALORE")
        time.sleep(1)
        item = self.driver.find_elements_by_id("ui-id-3")[0]
        item.click()
        time.sleep(1)

        going_to = self.driver.find_element_by_name("toPlaceName")
        going_to.send_keys("PUNE")
        time.sleep(1)
        item = self.driver.find_elements_by_id("ui-id-6")[0]
        item.click()

        date_of_departure = self.driver.find_element_by_name("txtJourneyDate")
        date_of_departure.click()
        time.sleep(1)
        date = self.driver.find_element_by_xpath('//*[@id="ui-datepicker-div"]/table/tbody/tr[5]/td[6]/a')
        date.click()

        self.driver.execute_script("""
        var form = document.getElementById('bookingsForm');
        validateBookingSearch(form, '/oprs-web/avail/services.do');
        """)
        time.sleep(5)

        error_message = self.driver.find_element_by_id("errorMsg")

        assert error_message and\
               "Advanced reservation date is invalid. Please book tickets before" in error_message.text

    def tearDown(self):
        self.driver.close()
