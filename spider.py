from selenium import webdriver
from selenium.webdriver import ActionChains
import time as t
import traceback


def broswer(url, location, next_page_xpath, content_xpath, callback, debug):
    # 打开浏览器,到达指定网站
    option = webdriver.ChromeOptions()
    if len(location) > 0:
        option.binary_location = location
    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=option)
    driver.get(url)

    t.sleep(2)
    # 分页爬取信息
    job_names = []
    job_hrefs = []
    next_page = driver.find_element_by_xpath(next_page_xpath)
    try:
        while next_page is not None:
            t.sleep(1)
            contents = driver.find_elements_by_xpath(content_xpath)
            for content in contents:
                print(content.text)
                job_names.append(content.text)
                print(content.get_attribute("href"))
                job_href = content.get_attribute("href")
                job_hrefs.append(job_href)
            t.sleep(0.5)
            next_page_buttons = driver.find_elements_by_xpath(next_page_xpath)
            if debug or next_page_buttons is None or callback(next_page_buttons):
                break
            ActionChains(driver).move_to_element(next_page_buttons[0]).click(next_page_buttons[0]).perform()

        return job_names, job_hrefs
    except Exception:
        print(traceback.print_exc())
