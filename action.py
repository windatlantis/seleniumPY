import seleniumPY.spider as spider
import seleniumPY.baseconfig as base
import seleniumPY.writefile as wf


def callback(next_page_buttons):
    return next_page_buttons[0].get_attribute("class") == "disable"


url = 'https://job.alibaba.com/zhaopin/positionList.htm?spm=a2obv.11410909.0.0.55af73210YgHzd'
next_page_xpath = '//*[@id="J-pagination"]/div/ul/li[last()]/a'
content_xpath = '//*[@id="J-list-box"]/tr/td/span/a'
result = spider.broswer(url, base.location, next_page_xpath, content_xpath, callback, False)
wf.writeExcel(result[0], result[1])
