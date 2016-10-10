from nose_selenium import SeleniumTestCase


class MyTestCase(SeleniumTestCase):

    def test_that_google_opens(self):
        self.wd.get("http://www.ksrtc.in/oprs-web/")
        self.assertEqual(
            self.wd.title,
            "KSRTC Official Website for Online Bus Ticket Booking - KSRTC.in"
        )
