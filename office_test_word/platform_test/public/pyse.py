#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from public.log import logger


class Pyse(object):
    """
        PYSE框架对于selenium的封装，使其更加方便使用。
    """

    def __init__(self, browser='chrome'):
        """
        初始化方法，默认正确的驱动是Firefox浏览器。
        Chrome浏览器是“chrome”，
        IE浏览器是“internet explorer”或“ie”。
        """
        if browser == "firefox" or browser == "ff":
            br = webdriver.Firefox()
            logger.info("-- browser: firefox")
        elif browser == "chrome":
            executable_path = r"./lib/chromedriver.exe"
            br = webdriver.Chrome(executable_path)
            logger.info("-- browser: chrome")
        elif browser == "internet explorer" or browser == "ie":
            br = webdriver.Ie()
            logger.info("-- browser: internet explorer")
        elif browser == "opera":
            br = webdriver.Opera()
            logger.info("-- browser: opera")
        elif browser == "phantomjs":
            br = webdriver.PhantomJS()
            logger.info("-- browser: phantomjs")
        elif browser == 'edge':
            br = webdriver.Edge()
            logger.info("-- browser: edge")
        try:
            self.driver = br
        except Exception:
            raise NameError("未找到 %s 浏览器,可以输入：'ie', 'ff', 'opera', 'phantomjs', 'edge' or 'chrome'." % browser)

    def element_wait(self, css, secs=5):
        """
        定位方式方法封装

        使用方法:
        driver.element_wait("css=>#el",10)
        """
        if "=>" not in css:
            raise NameError("定位语法错误，缺少 '=>'.")

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
            raise NameError("请输入正确的元素，如：'id','name','class','link_text','xpath','css'.")

    def get_element(self, css):
        """
        判断定位方式，并返回元素
        """
        if "=>" not in css:
            raise NameError("定位语法错误，缺少 '=>'.")

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
            raise NameError("请输入正确的元素，如：'id','name','class','link_text','xpath','css'.")
        return element

    def open(self, url):
        """
        打开网址
        """
        logger.info("-- open: %s" % url)
        self.driver.get(url)

    def max_window(self):
        """
        最大框体
        """
        self.driver.maximize_window()

    def set_window(self, wide, high):
        """
        设置屏幕大小
        """
        logger.info("-- set_window: %s %s" % (wide, high))
        self.driver.set_window_size(wide, high)

    def type(self, css, text):
        """
        输入内容信息
        """
        logger.info("-- type: %s %s" % (css, text))
        self.element_wait(css)
        el = self.get_element(css)
        el.send_keys(text)

    def clear(self, css):
        """
        清空
        """
        logger.info("-- clear: %s" % css)
        self.element_wait(css)
        el = self.get_element(css)
        el.clear()

    def click(self, css):
        """
        点击
        """
        logger.info("-- click: %s" % css)
        self.element_wait(css)
        el = self.get_element(css)
        el.click()

    def right_click(self, css):
        """
        右键点击
        """
        logger.info("-- right_click: %s" % css)
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).context_click(el).perform()

    def move_to_element(self, css):
        """
        鼠标越过元素
        """
        logger.info("-- move_to_element: %s" % css)
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).move_to_element(el).perform()

    def double_click(self, css):
        """
        双击
        """
        logger.info("-- double_click: %s" % css)
        self.element_wait(css)
        el = self.get_element(css)
        ActionChains(self.driver).double_click(el).perform()

    def drag_and_drop(self, el_css, ta_css):
        """
        拖动某个元素到某个距离，然后将其删除。
        """
        logger.info("-- drag_and_drop: %s %s" % el_css, ta_css)
        self.element_wait(el_css)
        element = self.get_element(el_css)
        self.element_wait(ta_css)
        target = self.get_element(ta_css)
        ActionChains(driver).drag_and_drop(element, target).perform()

    def click_text(self, text):
        """
        中文寻找元素位置，进行点击操作
        """
        logger.info("-- click_text: %s" % text)
        self.driver.find_element_by_partial_link_text(text).click()

    def close(self):
        """
        关闭
        """
        self.driver.close()
        logger.info("--  close ")

    def quit(self):
        """
       退出
        """
        self.driver.quit()
        logger.info("--  quit ")

    def submit(self, css):
        """
        提交表单
        """
        logger.info("-- submit: %s" % css)
        self.element_wait(css)
        el = self.get_element(css)
        el.submit()

    def F5(self):
        """
        刷新
        """
        self.driver.refresh()
        logger.info("--  F5 ")

    def js(self, script):
        """
        执行 JavaScript 脚本

        使用方法:
        driver.js("window.scrollTo(200,1000);")
        """
        logger.info("-- js: %s" % script)
        self.driver.execute_script(script)

    def get_attribute(self, css, attribute):
        """
        获取元素属性值

        使用方法:
        driver.get_attribute("css=>#el","type")
        """
        el = self.get_element(css)
        logger.info("-- get_attribute: %s %s" % (css, el.get_attribute(attribute)))
        return el.get_attribute(attribute)

    def get_text(self, css):
        """
        获取元素文本信息
        """
        self.element_wait(css)
        el = self.get_element(css)
        txt = el.text
        logger.info("-- get_text: %s %s" % (css, txt))
        return txt

    def get_display(self, css):
        """
        判断元素是否存在
        """
        self.element_wait(css)
        el = self.get_element(css)
        logger.info("-- get_display: %s" % css)
        return el.is_displayed()

    def get_title(self):
        """
        获取标题
        """
        title = self.driver.title
        logger.info("-- get_title: %s" % title)
        return title

    def get_url(self):
        """
        获取当前页的URL地址
        """
        url = self.driver.current_url
        logger.info("-- get_url: %s" % url)
        return url

    def get_windows_img(self, file_path):
        """
        获取当前窗口截图
        """
        self.driver.get_screenshot_as_file(file_path)
        logger.info("-- get_windows_img: %s" % file_path)

    def wait(self, secs):
        """
        隐性等待页面上的所有元素（秒）
        """
        self.driver.implicitly_wait(secs)
        logger.info("-- wait: %s" % secs)

    def accept_alert(self):
        """
        接受警告框.
        """
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        """
        驳回可用的警报.
        """
        self.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, css):
        """
        切换到指定的frame
        """
        self.element_wait(css)
        iframe_el = self.get_element(css)
        self.driver._switch_to.frame(iframe_el)
        logger.info("-- switch_to_frame: %s" % css)

    def switch_to_frame_out(self):
        """
        从当前的frame退出
        """
        self.driver._switch_to.default_content()
        logger.info("--  switch_to_frame_out ")

    def open_new_window(self, css):
        """
        创建新窗口，并指定到新窗口
        """
        original_windows = self.driver.current_window_handle
        el = self.get_element(css)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver._switch_to.window(handle)
        logger.info("-- open_new_window: %s" % css)

    def element_size(self, css, scss):
        """
        获取表格元素的集合
        :param css:
        :param scss:
        :return:
        """
        x = self.driver.find_element_by_id(css).find_elements_by_tag_name(scss)
        # rowall = [rowall.text for rowall in x]
        logger.info("-- element_size: %s" % x)
        return x


if __name__ == '__main__':
    driver = Pyse("chrome")
