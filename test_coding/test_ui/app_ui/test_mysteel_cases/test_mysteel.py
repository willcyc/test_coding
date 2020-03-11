# -*- coding: utf-8 -*-
import unittest
import sys
from os.path import dirname, abspath
BASH_PATH = dirname(dirname(abspath(__file__)))
sys.path.append(BASH_PATH)
from common.app_start import App_start


class TestMysteel(App_start):
    def test_login(self):
        pass


if __name__ == '__main__':
    unittest.main()
