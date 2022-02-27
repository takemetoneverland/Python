from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
from datetime import datetime

# 엑셀처리 모듈 임포트
import xlsxwriter

# user-agent 정보를 변환해 주는 모듈 임포트
# 특정 브라우저로 크롤링을 진행할 때 차단되는 것을 방지
from fake_useragent import UserAgent

# 이미지를 바이트 변환 처리 모듈
from io import BytesIO

# 요청 헤더 정보를 꺼내올 수 있는 모듈
import urllib.request as req

d = datetime.today()

file_path = f'C:/Users/D/Desktop/Java_Web_JDE/python/crawling/알라딘 베스트셀러 1~400위(뉴 버전)_{d.year}_{d.month}_{d.day}.xlsx'

# User Agent 정보 변환 (필수는 아니다.)
opener = req.build_opener() # 헤더 정보를 초기화
opener.addheaders = [('User-agent', UserAgent().ie)] # ie, opera, chrome, ff 등등 다른 브라우저를 통해 접근하는 것 요청 보낼 수 있게됨.
req.install_opener(opener) # 새로운 헤더 정보를 삽입.

# 엑셀 처리 선언
# Workbook 객체를 생성하여 엑셀 파일을 하나 생성(매개값으로 저장될 경로를 지정.)
workbook = xlsxwriter.Workbook(file_path)

# 워크 시트 생성
worksheet = workbook.add_worksheet()

# 브라우저 안뜨게 하기
chrome_option = Options()
chrome_option.add_argument('--headless')

# 브라우저 설정 - 일반 모드
browser = webdriver.Chrome('C:/Users/D/Desktop/Java_Web_JDE/python/chromedriver.exe')

# 브라우저 설정 -headless모드
browser = webdriver.Chrome('C:/Users/D/Desktop/Java_Web_JDE/python/chromedriver.exe', options=chrome_option)

# 브라우저 사이즈 조정(px 단위로)
browser.set_window_size(800, 600)

# 브라우저 내부 대기
# time.sleep(10) -> 브라우저 로딩에 상관 없이 무조건 10초 대기.

# 웹 페이지 전체가 로딩될 때 까지 대기 후 남은 시간 무시. 자바스크립트의 로딩 시간은 고려하지 않음.
browser.implicitly_wait(10)

# 페이지 이동 (베스트셀러 페이지)
browser.get('https://www.aladin.co.kr/shop/common/wbest.aspx?BranchType=1&start=we')

# 엑셀에 텍스트 저장
cell_format = workbook.add_format({'bold':True, 'font_color':'red', 'bg_color':'yellow'})
worksheet.write('A1', '썸네일', cell_format)
worksheet.write('B1', '제목', cell_format)
worksheet.write('C1', '작가', cell_format)
worksheet.write('D1', '출판사', cell_format)
worksheet.write('E1', '출판일', cell_format)
worksheet.write('F1', '가격', cell_format)
worksheet.write('G1', '링크', cell_format)

while True:
    # bs4 초기화
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    div_ss_book_box_list = soup.find_all('div', class_='ss_book_box')

    for div_ss_book_box in div_ss_book_box_list:

        # 이미지. 여러개 얻어올 때는 select() 하나일 때는 select_one()
        img_url = div_ss_book_box.select_one('table div > a > img.i_cover')
        print(img_url)