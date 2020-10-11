import seleniumPY.spider as spider
import seleniumPY.writefile as wf


def runTest(company, callback):
    """
    主方法
    :param company:
    :param callback:
    :return:
    """
    result = spider.broswer_pack(company, callback, False)
    wf.writeExcel(result[0], result[1], result[2])


ali = {
    "url": 'https://job.alibaba.com/zhaopin/positionList.htm?spm=a2obv.11410909.0.0.55af73210YgHzd',
    "next_page_xpath": '//*[@id="J-pagination"]/div/ul/li[last()]/a',
    "content_xpath": '//*[@id="J-list-box"]/tr/td/span/a',
    "type_xpath": '//*[@id="J-list-box"]/tr/td[2]/span'
}


def alicallback(driver):
    nextbtn = driver.find_elements_by_xpath('//*[@id="J-pagination"]/div/ul/li[last()]')
    return nextbtn is not None and nextbtn[0].get_attribute("class") == "disabled"


bili = {
    "url": 'https://app.mokahr.com/apply/bilibili/1022#/jobs',
    "next_page_xpath": '//span[@class="_3mGiw _2q4zI"]',
    "content_xpath": '//div[@class="title-20V7ljm-Id"]',
    "type_xpath": '//span[@class="status-item-1_w5ygMyMO"]',
    "href_xpath": '//div[@class="link-2tgd22te-3"]/a'
}


def bilicallback(driver):
    nextbtn = driver.find_elements_by_xpath('//div[@class="results-1cfVpxNSQJ"]/div[last()]/div/span[last()]')
    return nextbtn is not None and "disabled" in nextbtn[0].get_attribute("class")


runTest(bili, bilicallback)
