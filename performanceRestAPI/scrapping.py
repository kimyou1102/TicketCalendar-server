from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
import os

def scrapping(driver, datas, musician):
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, "html.parser")
    a = soup.find("section")
    divs = a.select('section > div > div > div')

    print('@@@@@@@@@@@@@@@@@@@@  -- 시작 -- @@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    for div in divs:
        articles = a.select('div > div > div > article')
        for a in articles:
            c = a.select_one('article > div > div > div > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div')
            table = str.maketrans('【  】', '    ')
            string = c.get_text().translate(table)
            m = string.replace('#예스24티켓', '').replace('#티켓오픈소식', '').replace('#주요티켓오픈', '').replace('#티켓오픈', '').replace('#YES24티켓', '').replace('#YES24Ticket', '').replace('#오늘자티켓오픈', '').replace('\n', '').strip()
            arr = m.split('티켓')

            title = arr[0].strip()
            date_and_link = arr[1]

            fir = date_and_link.find('2')
            las = date_and_link.find('h')

            date_full = date_and_link[fir:las]

            date = date_full.split('(')[0].replace('-', '.')
            link = date_and_link[las:]

            obj = {'artist': musician, 'title': title, 'date_full': date_full.strip(), 'date':date, 'link': link, 'performance_info':f"{title}-{date}"}

            print('CHECK : ', next((item for item in datas if item.get('date') == date), None))
            date_check = next((item for item in datas if item.get('date') == date), None)

            print('/////////////////////////////////////////////////////////////////////////////////////')
            print('OBJ : ', obj)

            print('NONE_CHECK', date_check == None)

            print('NOT_CHECK', not(obj in datas))
            if(date_check == None):
                print('추가')
                datas.append(obj)


    time.sleep(5)

def load(driver, datas, musician):
    time.sleep(3)

    # 스크롤 내리기
    SCROLL_PAUSE_TIME = 2
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")         
    while True:
        # Scroll down to bottom                                                      
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)                                          
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight-50);") 
        # 내리면서 긁어온다(안그러면 사라짐;) 
        scrapping(driver, datas, musician)

        time.sleep(SCROLL_PAUSE_TIME)
        # Calculate new scroll height and compare with last scroll height            
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:                                                
            break
        last_height = new_height

    print(len(datas))
    for data in datas:
        print(data)
        print('--------------------------------------------------------------------------------------')


def getDatas(musician):
    url = f'https://twitter.com/search?q=from%3AYES24TicketOpen%20{musician}&src=typed_query&f=top'
    datas = []
    driver = webdriver.Chrome('chromedriver.exe')
    driver.get(url)
    driver.implicitly_wait(3)
    # 창 뜰 때까지 기다리기
    try:
        # ID가 myDynamicElement인 element가 로딩될 때 까지 10초 대기
        element = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-xr3zp9.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-14lw9ot.r-1867qdf.r-1jgb5lz.r-pm9dpa.r-1ye8kvj.r-1rnoaur.r-13qz1uu")))
        print('성공')
        #나중에 버튼 클릭
        driver.find_element(By.CSS_SELECTOR, '#layers > div:nth-child(2) > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-1kihuf0.r-18u37iz.r-1pi2tsx.r-1777fci.r-1pjcn9w.r-xr3zp9.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-14lw9ot.r-1867qdf.r-1jgb5lz.r-pm9dpa.r-1ye8kvj.r-1rnoaur.r-13qz1uu > div > div.css-1dbjc4n.r-1awozwy.r-16y2uox > div > div.css-1dbjc4n.r-98ikmy.r-hvns9x > div.css-1dbjc4n.r-13qz1uu > div.css-18t94o4.css-1dbjc4n.r-1niwhzg.r-1ets6dv.r-sdzlij.r-1phboty.r-rs99b7.r-1wzrnnt.r-19yznuf.r-64el8z.r-1ny4l3l.r-1dye5f7.r-o7ynqc.r-6416eg.r-lrvibr').click()
        load(driver, datas, musician)
    # 안뜬다면 그냥
    except TimeoutException:
        print('실패')
        time.sleep(3)
        load(driver, datas, musician)

    return datas


# getDatas('lucy')