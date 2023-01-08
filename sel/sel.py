from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait

import time

# 웹드라이버 세팅
service = ChromeService(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)

# url 세팅
pageIndex = 98
driver.get(f'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=brd&selUpjong=21&selIndus=&pageUnit=10&pageIndex={pageIndex}')

# 페이지당 표시 개수 선택 (10, 25, 50, 100, 150, 300)
# pageUnit = Select(driver.find_element(By.ID, 'pageUnit'))
# pageUnit.select_by_value(value='10')

# 페이지당 표시 개수 버튼
# pageUnitBtn = driver.find_element(By.XPATH, '//*[@id="frm"]/div[2]/div/a')
# pageUnitBtn.click()

# 업종 선택 (외식, 도소매, 서비스)
# selUpjong = Select(driver.find_element(By.ID, 'selUpjong'))
# selUpjong.select_by_value(value='21')

# 분류 선택 (한식, 분식, 중식 등)
# selIndus = Select(driver.find_element(By.ID, 'selIndus'))
# selIndus.select_by_value(value='C1')

# 업종, 분류 검색 버튼
# SearchBtn = driver.find_element(By.XPATH, '//*[@id="frm"]/div[1]/fieldset/input[2]')
# SearchBtn.click()

# 페이지네이션 처리
while True:
    print(pageIndex)
    # 각각의 row에서 영업표지 선택
    try:
        len_rows = len(driver.find_elements(By.XPATH, '//*[@id="frm"]/table/tbody/tr'))
    except:
        driver.get(f'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=brd&selUpjong=21&selIndus=&pageUnit=10&pageIndex={pageIndex}')
        continue
    for i in range(len_rows):
        try:
            anchor = driver.find_elements(By.XPATH, '//*[@id="frm"]/table/tbody/tr')[i].find_elements(By.TAG_NAME, 'a')[-1]
            name = anchor.text
            anchor.click()

            # 상호 anchor를 선택해서 정보공개서 웹페이지로 넘어감
            # 우선 파일로 저장하고, 나중에 처리
            with open(f"report/{name}.html", "w", encoding='UTF-8') as f:
                f.write(driver.page_source)

            # 뒤로가기
            driver.back()
        except:
            with open(f"error.html", "w", encoding='UTF-8') as f:
                f.write(driver.page_source)
            time.sleep(10)
            driver.get(f'https://franchise.ftc.go.kr/mnu/00013/program/userRqst/list.do?searchCondition=&searchKeyword=&column=brd&selUpjong=21&selIndus=&pageUnit=10&pageIndex={pageIndex}')


    # 다음 페이지 찾아가기
    try:
        pageIndex = int(driver.find_element(By.XPATH, '//*[@id="frm"]/div[3]/div/ul').find_element(By.CLASS_NAME, 'btn_chk').get_attribute('innerText'))
        next_page = driver.find_element(By.XPATH, f'//*[@id="frm"]/div[3]/div/ul/li/a[text()={pageIndex+1}]')
    # 다음 목록으로 넘어가거나 종료하기
    except:
        if pageIndex%10 == 0:
            next_page = driver.find_element(By.XPATH, f'//*[@id="frm"]/div[3]/div/ul/li/a[text()=">"]')
        else:
            break
    next_page.click()