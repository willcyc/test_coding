# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.remote.webdriver import WebDriver
import time
from appium import webdriver
from selenium.webdriver.common.by import By


class TestDemo:

    def setup(self):
        caps = {}
        caps["platformName"] = "Android"
        caps["deviceName"] = "GUWCEMV8CYRGS85P"
        caps["appPackage"] = "com.mysteel.android.steelphone"
        caps["appActivity"] = "com.mysteel.android.steelphone.ui.activity.IntroActivity"
        # caps["appPackage"] = "io.appium.android.apis"
        # caps["appActivity"] = ".ApiDemos"
        caps["autoGrantPermissions"] = "true"

        self.driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        self.driver.implicitly_wait(10)

    def test_login(self):
        self.allow01 = "android:id/button1"
        flag = True
        while flag:
            if len(self.driver.find_elements(By.ID, self.allow01)) >= 1:
                self.driver.find_element(By.ID, self.allow01).click()
            else:
                flag = False
                break

        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/iv_banner").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/ok").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/gudie_one").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/go_download").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/img_personcenter").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/gudie_one").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/tv_personname").click()
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/etPhone").send_keys("19100000002")
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/etVerificationCode").send_keys("0018")
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/btnLogin").click()
        time.sleep(3)

    def teardown(self):
        self.driver.quit()
