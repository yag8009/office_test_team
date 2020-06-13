#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import logging.config
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

# logging.config.fileConfig("log.conf")
# logger = logging.getLogger("dxt")
# from public.log import logger


class Pyse(object):
    """
        Pyse framework for the main class, the original
    selenium provided by the method of the two packaging,
    making it easier to use.
    """

    def __init__(self, browser='chrome'):
        """
        Run class initialization method, the default is proper
        to drive the Firefox browser. Of course, you can also
        pass parameter for other browser, Chrome browser for the "Chrome",
        the Internet Explorer browser for "internet explorer" or "ie".
        """
        if browser == "firefox" or browser == "ff":
            br = webdriver.Firefox()
        elif browser == "chrome":
            executable_path = "chromedriver.exe"
            br = webdriver.Chrome(executable_path)
        elif browser == "internet explorer" or browser == "ie":
            br = webdriver.Ie()
        elif browser == "opera":
            br = webdriver.Opera()
        elif browser == "phantomjs":
            br = webdriver.PhantomJS()
        elif browser == 'edge':
            br = webdriver.Edge()
        try:
            self.driver = br
        except Exception:
            raise NameError("Not found %s browser,You can enter 'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def element_wait(self, css, secs=5):
        """
        Waiting for an element to display.

        Usage:
        driver.element_wait("css=>#el",10)
        """
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.ID, value)))
        elif by == "name":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.NAME, value)))
        elif by == "class":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CLASS_NAME, value)))
        elif by == "link_text":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.LINK_TEXT, value)))
        elif by == "xpath":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.XPATH, value)))
        elif by == "css":
            WebDriverWait(self.driver, secs, 1).until(EC.presence_of_element_located((By.CSS_SELECTOR, value)))
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):
        """
        Judge element positioning way, and returns the element.
        """
        if "=>" not in css:
            raise NameError("Positioning syntax errors, lack of '=>'.")

        by = css.split("=>")[0]
        value = css.split("=>")[1]

        if by == "id":
            element = self.driver.find_element_by_id(value)
        elif by == "name":
            element = self.driver.find_element_by_name(value)
        elif by == "class":
            element = self.driver.find_element_by_class_name(value)
        elif by == "link_text":
            element = self.driver.find_element_by_link_text(value)
        elif by == "xpath":
            element = self.driver.find_element_by_xpath(value)
        elif by == "css":
            element = self.driver.find_element_by_css_selector(value)
        else:
            raise NameError("Please enter the correct targeting elements,'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        """
        open url.

        Usage:
        driver.open("https://www.baidu.com")
        """
        self.driver.get(url)
        # logger.info(u"打开网址：", url)

    def max_window(self):
        """
        Set browser window maximized.

        Usage:
        driver.max_window()
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        Set browser window wide and high.

        Usage:
        driver.set_window(wide,high)
        """
        self.driver.set_window_size(wide, high)
        # logger.info(u"设置屏幕大小")

    def type(self, css, text):
        """
        Operation input box.

        Usage:
        driver.type("css=>#el","selenium")
        """
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)
        # logger.info(u"获取：", css, "信息：", text)

    def clear(self, css):
        """
        Clear the contents of the input box.

        Usage:
        driver.clear("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()
        # logger.info(u"清空位置：", css)

    def click(self, css):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.click("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        el.click()
        # logger.info(u"点击 : ", css)

    def right_click(self, css):
        """
        Right click element.

        Usage:
        driver.right_click("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()
        # logger.info(u"右键点击：", css)

    def move_to_element(self, css):
        """
        Mouse over the element.

        Usage:
        driver.move_to_element("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        """
        Double click element.

        Usage:
        driver.double_click("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()
        # logger.info(u"双击位置：", css)

    def drag_and_drop(self, el_css, ta_css):
        """
        Drags an element a certain distance and then drops it.

        Usage:
        driver.drag_and_drop("css=>#el","css=>#ta")
        """
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()
        # logger.info(u"将元素：", el_css, u"拖到：", ta_css)

    def click_text(self, text):
        """
        Click the element by the link text

        Usage:
        driver.click_text("新闻")
        """
        self.driver.find_element_by_partial_link_text(text).click()
        # logger.info(u"点击：", text)

    def close(self):
        """
        Simulates the user clicking the "close" button in the titlebar of a popup
        window or tab.

        Usage:
        driver.close()
        """
        self.driver.close()
        # logger.info(u"关闭")

    def quit(self):
        """
        Quit the driver and close all the windows.

        Usage:
        driver.quit()
        """
        self.driver.quit()
        # logger.info(u"关闭")

    def submit(self, css):
        """
        Submit the specified form.

        Usage:
        driver.submit("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()
        # logger.info(u"提交表格：", css)

    def F5(self):
        """
        Refresh the current page.

        Usage:
        driver.F5()
        """
        self.driver.refresh()
        # logger.info(u"刷新页面")

    def js(self, script):
        """
        Execute JavaScript scripts.

        Usage:
        driver.js("window.scrollTo(200,1000);")
        """
        self.driver.execute_script(script)
        # logger.info("js:", script)

    def get_attribute(self, css, attribute):
        """
        Gets the value of an element attribute.

        Usage:
        driver.get_attribute("css=>#el","type")
        """
        el = self.get_element(css)
        # logger.info(u"获取元素属性的值:", attribute)
        return el.get_attribute(attribute)

    def get_text(self, css):
        """
        Get element text information.

        Usage:
        driver.get_text("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        # logger.info(u"获取元素文本信息:", el.text)
        return el.text

    def get_display(self, css):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("css=>#el")
        """
        self.element_wait(css)
        el = self.get_element(css)
        # logger.info(u"判断元素:", el.is_displayed())
        return el.is_displayed()

    def get_title(self):
        """
        Get window title.

        Usage:
        driver.get_title()
        """
        # logger.info(u"获取标题:", self.driver.title)
        return self.driver.title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        # logger.info(u"获取URL:", self.driver.current_url)
        return self.driver.current_url

    def get_windows_img(self, file_path):
        """
        Get the current window screenshot.

        Usage:
        driver.get_windows_img()
        """
        # logger.info(u"当前窗口截图:", file_path)
        self.driver.get_screenshot_as_file(file_path)

    def wait(self, secs):
        """
        Implicitly wait.All elements on the page.

        Usage:
        driver.wait(10)
        """
        # logger.info(u"隐式等待:", secs)
        self.driver.implicitly_wait(secs)

    def accept_alert(self):
        """
        接受警告框.

        Usage:
        driver.accept_alert()
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        驳回可用的警报.

        Usage:
        driver.dismiss_alert()
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        """
        Switch to the specified frame.

        Usage:
        driver.switch_to_frame("css=>#el")
        """
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver._switch_to.frame(iframe_el)
        # logger.info(u"切换frame:", css)

    def switch_to_frame_out(self):
        """
        Returns the current form machine form at the next higher level.
        Corresponding relationship with switch_to_frame () method.

        Usage:
        driver.switch_to_frame_out()
        """
        self.driver._switch_to.default_content()
        # logger.info(u"退出当前frame")

    def open_new_window(self, css):
        """
        Open the new window and switch the handle to the newly opened window.

        Usage:
        driver.open_new_window()
        """
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)
        # logger.info(u"切换窗口")


if __name__ == '__main__':
    driver = Pyse("chrome")
