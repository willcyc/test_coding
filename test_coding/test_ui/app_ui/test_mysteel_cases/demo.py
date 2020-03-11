import pytest
import yaml
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from appium import webdriver
import sys
from os.path import dirname, abspath
current_path = dirname(dirname(abspath(__file__))).replace("\\", "/") + "/test_mysteel_cases"
print(current_path)
sys.path.append(current_path)

# 读取yaml文件
global search_data
search_data = yaml.safe_load(open(current_path + "/search.yaml", "r", encoding='utf-8'))
print("search_data:", search_data)
global testcase_data
testcase_data = yaml.safe_load(open(current_path + "/testcase.yaml", "r", encoding='utf-8'))
print("testcase_data:", testcase_data)


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

    def aa_test_capabilities(self, keyword, expected):
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("android:id/button1").click()
        except Exception:
            pass

        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("android:id/button1").click()
        except Exception:
            pass

        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id("android:id/button1").click()
        except Exception:
            pass
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/turnUpLn").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView[2]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/ok").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/gudie_one").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/go_download").click()
        self.driver.implicitly_wait(10)

        # 显示等待
        def loaded(driver):
            print(datetime.datetime.now())
            if len(self.driver.find_elements_by_id("com.mysteel.android.steelphone:id/md_buttonDefaultNegative")) >= 1:
                self.driver.find_elements_by_id("com.mysteel.android.steelphone:id/md_buttonDefaultNegative").click()
                return True
            else:
                return False
        try:
            WebDriverWait(self.driver, 5).until(loaded)  # 引用显示等待
        except Exception:
            print("no update")

        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/tv_search").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/et").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/et").send_keys(keyword)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text("唐山市场钢坯价格行情")').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/iv_comment").click()
        # 获取toast
        get_toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        print("get_toast:", get_toast)
        assert expected in get_toast

        article_title = self.driver.find_element_by_id("tv_a_title")
        assert "com.mysteel.android.steelphone" in article_title.get_attribute("package")
        assert "tv_a_title" in article_title.get_attribute("resource-id")

        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/iv_back").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/iv_f").click()
        self.driver.implicitly_wait(10)

        # webview上下文切换
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/img_meeting").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/tv_titlet").click()
        time.sleep(10)
        print("当前上下文：", self.driver.current_context)
        all_contexts = self.driver.contexts
        print("all_contexts:", all_contexts)
        time.sleep(3)
        # print(all_contexts[1])
        # self.driver.switch_to.context("WEBVIEW_com.huawei.browser")
        time.sleep(3)
        print("当前上下文：", self.driver.current_context)
        # self.driver.find_element_by_accessibility_id("").click()  # webview_api27版本、或真机，使用content-desc进行定位
        # WebDriverWait(self.driver, 20).until(excepted_conditions.visibility_of_element_located(By.xpth,"/html/body/div[6]/div[2]/ul/li[2]/a"))
        # self.driver.find_element_by_xpath("/html/body/div[6]/div[2]/ul/li[2]/a").click()
        time.sleep(3)
        """
        # 异常处理

        def find_element(self, locator):
            print(locator)
            try:
                return self.driver.find_element(*locator)
            except:
                self.handle_exception()
                return self.driver.find_element(*locator)

        def find_element_and_click(self, locator):
            print("click")
            try:
                self.find_element(locator).click()
            except:
                self.handle_exception()
                self.find_element(locator).click()

        _black_list = []  # 异常元素列表

        def handle_exception(self):
            self.driver.implicitly_wait(10)
            for locator in _black_list:
                print(locator)
                elements = self.driver.find_elements(*locator)
                if len(elements) >= 1:
                    elements[0].click
                else:
                    print(str(locator) + " not found")
            self.driver.implicitly_wait(10)
        """

    def bb_test_capabilities(self):
        TestCase(current_path + "/testcase.yaml").run(self.driver)
        # self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("android:id/button1").click()
        # self.driver.implicitly_wait(10)
        # try:
        #     self.driver.find_element_by_id("android:id/button1").click()
        # except Exception:
        #     pass

        # self.driver.implicitly_wait(10)
        # try:
        #     self.driver.find_element_by_id("android:id/button1").click()
        # except Exception:
        #     pass
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("com.mysteel.android.steelphone:id/turnUpLn").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[1]/android.widget.ImageView[2]").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/androidx.recyclerview.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView[2]").click()
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("com.mysteel.android.steelphone:id/ok").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/gudie_one").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/go_download").click()
        self.driver.implicitly_wait(10)

        # 显示等待
        def loaded(driver):
            print(datetime.datetime.now())
            if len(self.driver.find_elements_by_id("com.mysteel.android.steelphone:id/md_buttonDefaultNegative")) >= 1:
                self.driver.find_elements_by_id("com.mysteel.android.steelphone:id/md_buttonDefaultNegative").click()
                return True
            else:
                return False
        try:
            WebDriverWait(self.driver, 5).until(loaded)  # 引用显示等待
        except Exception:
            print("no update")

        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/tv_search").click()
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("com.mysteel.android.steelphone:id/et").click()
        self.driver.implicitly_wait(10)
        # self.driver.find_element_by_id("com.mysteel.android.steelphone:id/et").send_keys(keyword)
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.GridView/android.widget.RelativeLayout[1]/android.widget.TextView").click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_android_uiautomator('text("5日全国钢坯市场收市盘点")').click()
        self.driver.implicitly_wait(10)
        self.driver.find_element_by_id("com.mysteel.android.steelphone:id/iv_comment").click()
        # 获取toast
        get_toast = self.driver.find_element_by_xpath("//*[@class='android.widget.Toast']").text
        print("get_toast:", get_toast)
        # assert expected in get_toast

        # article_title = self.driver.find_element_by_id("tv_a_title")
        # assert "com.mysteel.android.steelphone" in article_title.get_attribute("package")
        # assert "tv_a_title" in article_title.get_attribute("resource-id")

    # 获取cpu、内存、磁盘、网络
    def cc_test_performance(self):
        print("123456")
        print("123:", self.driver.get_performance_data_types())
        for p in self.driver.get_performance_data_types():
            print(p)
            print("123456:", self.driver.get_performance_data("com.mysteel.android.steelphone", p, 5))
            print("===========")

    def dd_test_xpath(self):
        self.aa_test_capabilities()
        self.driver.find_element_by_xpath("//*[@text='资讯' and contains(@resource-id,'tv_menu')]").click()  #返回首页

    @pytest.mark.parametrize(
        "keyword, expected",
        [
            ("螺纹钢", "还没有其他人评论哟"),
            ("线材", "还没有其他人评论哟")
        ]
    )
    def ee_test_toast(self, keyword, expected):    # 获取toast
        self.aa_test_capabilities(keyword, expected)

    # 读取yaml文件
    @pytest.mark.parametrize(
        "keyword, expected", search_data
    )
    def test_toast_from_yaml(self, keyword, expected):
        self.aa_test_capabilities(keyword, expected)

    def teardown(self):
        self.driver.quit()


class TestCase:
    def __init__(self, path):
        file = open(path, "r", encoding='utf-8')
        self.steps = yaml.safe_load(file)
        print("steps:", self.steps)

    def run(self, driver: WebDriver):
        for step in self.steps:
            element = None
            if isinstance(step, dict):
                if "id" in step.keys():
                    element = driver.find_element_by_id(step["id"])
                elif "xpath" in step.keys():
                    element = driver.find_element_by_xpath(step["xpath"])
                else:
                    print(step.keys())

            if "input" in step.keys():
                element.send_keys(step["input"])
            elif "get" in step.keys():
                text_ = element.get_attribute(step["get"])
                print(text_)
            else:
                element.click()
