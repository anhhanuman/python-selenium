from bot.booking import constants as const
from selenium import webdriver


class Booking(webdriver.Chrome):
    def __init__(self):
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)
