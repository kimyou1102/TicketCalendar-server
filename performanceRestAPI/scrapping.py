from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
import os

def getDatas(musician):
    url = 'http://ticket.yes24.com/New/Notice/NoticeMain.aspx'
    # print(getTickets())
    titles = []
    open_dates = []
    datas = []
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(f"{url}")
    driver.implicitly_wait(3)
    driver.find_element(By.ID, 'SearchTextbox').send_keys(musician)
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, '.notice-srch > a').click()
    time.sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    time.sleep(3)

    trs = soup.find_all("tr")
    del trs[0]
    for tr in trs:
        ems = tr.select('td:nth-child(2) > a > em')
        title = ''
        if len(ems) == 2:
            title = ems[1].get_text()
        else:
            title = ems[0].get_text()

        open_date = tr.select_one('td:nth-child(3)').get_text()
        open_date = open_date.replace(' ', '').replace('\n', '')
        # print(open_date)
        if(open_date != ''):
            # datas.append([musician, open_date[0:10], title, open_date[-5:]])
            # open_dates.append(open_date)
            # titles.append(title.replace('안내', ''))
            title = title.replace('안내', '')
            date = open_date[0:10]
            datas.append({'artist': musician, 'title': title.replace('안내', ''), 'date': date, 'time': open_date[-5:], 'performance_info':f"{title}-{date}"})

    return datas

# musician = '검정치마'
# musician = 'surl'
# test(musician)

# print(datas)

# for i in range(len(titles)):
#     print(titles[i])
#     print(open_dates[i])
#     print('#################################')

# 테스트
# test = '2022.12.20(화)19:00'
# print(test[0:10])
# print(test[-5:])

# 값을 입력받고, 