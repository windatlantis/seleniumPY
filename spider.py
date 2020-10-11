from selenium import webdriver
from selenium.webdriver import ActionChains
import time as t
import traceback
import seleniumPY.baseconfig as base


def getDriver():
    """
    获取驱动器
    :return:
    """
    option = webdriver.ChromeOptions()
    location = base.location
    if len(location) > 0:
        option.binary_location = location
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
    return driver


def broswer_pack(company, callback, debug):
    """
    参数封装到dict
    :param company:
    :param callback:
    :param debug:
    :return:
    """
    return broswer(company["url"], company["next_page_xpath"], company["content_xpath"], company["href_xpath"], company["type_xpath"], callback, debug)


def broswer(url, next_page_xpath, content_xpath, href_xpath, type_xpath, callback, debug):
    """
    浏览页面获取数据
    :param url:
    :param next_page_xpath:
    :param content_xpath:
    :param href_xpath:
    :param type_xpath:
    :param callback:
    :param debug:
    :return:
    """
    # 打开浏览器,到达指定网站
    driver = getDriver()
    driver.get(url)

    t.sleep(2)
    # 分页爬取信息
    job_names = []
    job_hrefs = []
    job_types = []
    i = 1
    try:
        while True:
            t.sleep(0.5)
            contents = driver.find_elements_by_xpath(content_xpath)
            print("第 {0} 页".format(i))
            if href_xpath is not None and len(href_xpath) > 0:
                # 内容+链接
                for content in contents:
                    print(content.text, end=',')
                    job_names.append(content.text)
                print()
                hrefs = driver.find_elements_by_xpath(href_xpath)
                for href in hrefs:
                    print(href.get_attribute("href"), end=',')
                    job_hrefs.append(href.get_attribute("href"))
                print()
            else:
                # 内容+链接
                for content in contents:
                    print(content.text, content.get_attribute("href"), sep=',')
                    job_names.append(content.text)
                    job_hrefs.append(content.get_attribute("href"))
            # 类型
            types = driver.find_elements_by_xpath(type_xpath)
            for jtype in types:
                print(jtype.text, end=',')
                job_types.append(jtype.text)
            print()
            t.sleep(0.5)
            # 下一页
            next_page_buttons = driver.find_elements_by_xpath(next_page_xpath)
            if debug or next_page_buttons is None or callback(driver):
                break
            ActionChains(driver).move_to_element(next_page_buttons[0]).click(next_page_buttons[0]).perform()
            i = i + 1

        return job_names, job_hrefs, job_types
    except Exception:
        print(traceback.print_exc())
