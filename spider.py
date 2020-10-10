from selenium import webdriver
from selenium.webdriver import ActionChains
import time as t
import traceback
import xlwings as xl

url='https://jobs.51job.com/all/co123056.html#syzw'

#打开浏览器,到达指定网站
option=webdriver.ChromeOptions()
driver=webdriver.Chrome(executable_path='chromedriver.exe',options=option)
driver.get(url)

t.sleep(3)
#分页爬取信息
job_names=[]
job_hrefs=[]
next_page=driver.find_element_by_xpath('//div[@class="p_in"]/ul/li[@class="bk"]/a')
i=1
try:
    while next_page!=None:
        t.sleep(1)
        contents = driver.find_elements_by_xpath('//div[@class="el"]/p[@class="t1"]/a[@target="_blank"]')
        for content in contents:
            print(content.text)
            job_names.append(content.text)
            print(content.get_attribute("href"))
            job_href=content.get_attribute("href")
            job_hrefs.append(job_href)
        t.sleep(0.5)
        next_page_buttons = driver.find_elements_by_xpath('//div[@class="p_in"]/ul/li[@class="bk"]/a')
        if i==1:
            ActionChains(driver).move_to_element(next_page_buttons[0]).click(next_page_buttons[0]).perform()
        else:
            if len(next_page_buttons) == 1:
                break
            ActionChains(driver).move_to_element(next_page_buttons[1]).click(next_page_buttons[1]).perform()
        i=i+1

except Exception as ex :
    print(traceback.print_exc())

app=xl.App()
wb=app.books.active
ws=wb.sheets.active

ws.range("A1").options(transpose=True).value=job_names
ws.range("B1").options(transpose=True).value=job_hrefs
wb.save(r'{0}.xlsx'.format(t.clock()))

