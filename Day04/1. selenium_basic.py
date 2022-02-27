
# 셀레늄: 웹 자동화 및 웹의 소스코드를 수집하는 모듈
# cmd -> pip install selenium (셀레늄 라이브러리 다운로드)
# 셀레늄 임포트
from selenium import webdriver # 셀레늄 모들에 있는 클래스 웹드라이버(객체)를 임포트
import time

# 다운로드 받은 크롬 물리드라이버 가동 명령. 경로를 문자열로 작성
driver = webdriver.Chrome('C:/Users/D/Desktop/Java_Web_JDE/python/chromedriver.exe')

# 물리 드라이버로 사이트 이동 명령
driver.get('https://www.naver.com')

time.sleep(1)

'''
# 자동으로 버튼이나 링크 클릭 제어하기 (문자열로)
login_btn = driver.find_element_by_xpath('//*[@id="account"]/a')
login_btn.click()

time.sleep(1.5) # 브라우저가 페이지를 로딩할 시간을 벌어주는 것 (대기해라)

# 자동으로 텍스트 입력하기
id_input = driver.find_element_by_xpath('//*[@id="id"]')
id_input.send_keys('abc1234')

time.sleep(1)

pw_input = driver.find_element_by_xpath('//*[@id="pw"]')
pw_input.send_keys('aaa1111!')

time.sleep(1)

driver.find_element_by_xpath('//*[@id="log.login"]').click()
'''

# 네이버에 접속해서 검색창에 "오늘 날씨"를 입력해서
# 검색 후 가장 첫번째로 뜨는 네이버 뉴스를 띄워주기.
driver.find_element_by_xpath('//*[@id="query"]').send_keys('오늘 날씨')
time.sleep(1)
driver.find_element_by_xpath('//*[@id="search_btn"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sp_nws_all4"]/div[1]/div/div[1]/div[2]/a[2]').click()