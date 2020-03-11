import unittest
from appium import webdriver
import sys
from os.path import dirname, abspath
BASE_PATH = dirname(dirname(abspath(__file__)))
print(BASE_PATH)
sys.path.append(BASE_PATH)
from app_config import mysteel_app


class App_start(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", mysteel_app)
        self.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(self):
        self.driver.quit()
