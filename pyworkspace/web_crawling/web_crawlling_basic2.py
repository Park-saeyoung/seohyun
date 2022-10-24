####################################    정규식  ###########################################
import requests
import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')

# 주민번호 : 0301010-1234567
# email : boy@naver.com

# apple, approach, approve,
# care, case, cafe


# late, fade, shade, made

# . : 문자 한 개 ->  (ca.e)
# ^ : 문자열의 시작 -> (^ca)
# $ : 문자열의 끝 -> (de$)

# import re

# p = re.compile("ca.e")

# m = p.match('catte')

# print(m.group())

# def print_match(m):
#     if m:
#         print(m.group())
#     else:
#         print("매칭되지 않음")

# m = p.match("careless")   # match 주어진 문자열의 처음부터 일치하는지 확인 일치된 문자열 뒤 는 상관없음
# print_match(m)

# m = p.search("careless")   #search 주어진 문자열 중간에 일치하는게 있는지 확인
# print_match(m)


# def print_match(m):
#     if m:
#         print("m.group()", m.group()) #일치하는 문자열 반환
#         print("m.string()", m.string()) #입력받은 문자열 
#         print("m.start()", m.start()) #일치하는 문자열의 시작 index
#         print("m.end()", m.end()) #일치하는 문자열의 끝 index
#         print("m.span()", m.span()) #일치하는 문자열의 시작/끝 index
#     else:
#         print("매칭되지 않음")

# lst = p.findall("good cafe will take care of you, be carefull") # findall : 일치하는 모든 것을 리스트 형태로 반환
# print(lst)


########################################################################################

# User-Agent
#헤더 정보를 통해서 모바일인지, pc인지 확인 후 요청에 맞게 페이지 제공, 또는 접속 요청자가 사람인지 크롤링인지 판단하여
#제공 여부 결정
# useragent 확인 chrome, ie 가 다름

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "https://www.tistory.com"
# res = requests.get(url, headers=headers)   #사용자가 설정한 Useragent 값 전달
# res.raise_for_status() #문제가 있을시 에러 발생, 멈춤
# with open("tistory.html", "w", encoding="utf-8") as fd:
#     fd.write(res.text)

############################################################################################

# pip install lxml #구문 분석용 파서

# from bs4 import BeautifulSoup

# url = "https://comic.naver.com/index"
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml") #페이지의 모든 정보를 갖고 있는 객체

# print(soup.title) # title 갖고 옴
# print(soup.title.get_text()) # title의 텍스트만 갖고 옴
# print(soup.a) # soup객체에서 첫 번째 발견되는  a태그
# print(soup.a.attrs) # a태그(element)의 모든 속성 정보
# print(soup.a["href"]) # a태그(element)의 "href" 속성 정보

# print(soup.find("a", attrs={"class": "Nbtn_upload"})) #soup 객체에서 일치되는 첫 번째 앨리먼트, 해당 속성)
# print(soup.find(attrs={"class": "Nbtn_upload"})) #soup 객체에서 class가 "Nbtn_upload"인 첫 번째 앨리먼트)

# print(soup.find("li", attrs={"class": "rank01"}))

# rank1 = soup.find("li", attrs={"class": "rank01"})
# print(rank1.a.get_text()) rank1(soup객체)에서 a 태그의 텍스트 반환

# rank2 = rank1.next_sibling 형제(다음)앨리먼트
# print(rank2) 태그 서이에 개행정보(줄바꿈)가 있어서 내용이 없음
# rank2 = rank1.next_sibling.next_sibling
# print(rank2.a.get_text())
# rank3 = rank2.next_sibling.next_sibling
# print(rank3.a.get_text())
# rank2 = rank3.previous_sibling.previous_sibling 이전 앨리먼트
# print(rank2.a.get_text())

# rank_parents = rank1.parent 부모 앨리먼트
# print(rank_parents)

# rank2 = rank1.find_next_sibling("li") 중간에 개행정보(줄바꿈)있어도 지정한 태그를 검색
# print(rank2.a.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.a.get_text())
# rank2 = rank3.find_previous_sibling("li")
# print(rank2.a.get_text())

# rank1 = soup.find("li", attrs={"class": "rank01"})
# ranks = rank1.find_next_siblings("li")
# # print(ranks)
# for rk in ranks:
#     print(rk.a.get_text())

# find = soup.find("a", text = "약한영웅-164화")
# print(find.get_text())

# ######################################################################
# url = "https://comic.naver.com/webtoon/weekday" #네이버만화(홈) -> 웹툰
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml") #페이지의 모든 정보를 갖고 있는 객체
# cartoons = soup.find_all("a", attrs={"class":"title"}) # a태그 이면서 class가 "title"인 모든 앨리먼트
# for cartoon in cartoons:
#     print(cartoon.get_text())

###############################만화 정보와 링크 가져오기#########################

# url = "https://comic.naver.com/webtoon/list?titleId=758037" #참교육
# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml") #페이지의 모든 정보를 갖고 있는 객체
# webtoons = soup.find_all("td", attrs={"class":"title"})
# title = webtoons[0].a.get_text()
# print(title)
# link = webtoons[0].a["href"]   링크 가져오기 a[속성] : a태그에서 지정한 속성 값(href) 가져오기
# print("https://comic.naver.com" + link)

# for webtoon in webtoons:
#     link = "https://comic.naver.com/" + webtoon.a["href"]
#     print(webtoon.a.get_text(), link)

##############################평점 구하기##############################

# total_rates = 0
# webtoons = soup.find_all("div", attrs={'class':'rating_type'})
# for webtoon in webtoons:
#     rate = webtoon.find("strong").get_text()
#     total_rates += float(rate)
# print("전체 평점 : ", total_rates)
# print("평균 평점 : ", total_rates/len(webtoons))


##############################쿠팡 노트북 검색 ##########################

# # import re

# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=auto&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
# # res = requests.get(url)
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# items = soup.find_all("li", attrs={'class':re.compile('^search-product')}) #"search-product"문자열로 시작하는 모든 class 속성 값
# print(items[0].find("div", attrs={"class":"name"}).get_text())

#################################모든 제품 검색###########################
# for item in items:
#     name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
#     price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격
#     star = item.find("em", attrs={"class":"rating"})  # 별점(별점이 없는 경우 "별점 없음" 출력)
#     if star:
#         star = star.get_text()
#     else:
#         star = "평점 없음"
#     count = item.find("span", attrs={"class":"rating-total-count"}).get_text()  # 구매수(구매가 없는 경우 "구매 없음" 출력)
#     print(name, price, star, count)

#################################조건에 맞는 제품 검색(평점 없는 제품, 광고 제품 제외)############################
# for item in items:
        
#     ad_badge = item.find("span", attrs={"class":"ad-badge-text"}) # 광고 제품 
#     star = item.find("em", attrs={"class":"rating"}) 
#     count = item.find("span", attrs={"class":"rating-total-count"})
#     name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
#     price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

#     if "레노버" in name:
#         print("레노버 노트북 제외")
#         continue
    
#     if ad_badge:
#         print("광고 제품 제외")
#         continue

#     if star:
#         star = star.get_text()
#     else:
#         print("평점 없는 제품 제외")
#         continue
        
#     if count:
#         count = count.get_text()
#         # count = count[1:-1] # count 값에서 괄호 제거
#     else:
#         print("구매수 없는 제품 제외")
#         continue

#     if float(star) >= 4.5 and int(count[1:-1]) > 1000:   #별이 4.5개 이상이고 구매수 1000 이상
#         print(name, price, star, count)

#######################조건에 맞는 제품 검색(평점 없는 제품, 광고 제품 제외) 여러 페이지####################

# for i in range(1,5):
  
#     url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     items = soup.find_all("li", attrs={'class':re.compile('^search-product')}) #"search-product"문자열로 시작하는 모든 class 속성 값
#     print("페이지 정보 : ",i)

#     for item in items:
#         ad_badge = item.find("span", attrs={"class":"ad-badge-text"}) # 광고 제품 
#         star = item.find("em", attrs={"class":"rating"}) 
#         count = item.find("span", attrs={"class":"rating-total-count"})
#         name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
#         price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

#         if "레노버" in name:
#             print("레노버 노트북 제외")
#             continue
        
#         if ad_badge:
#             print("광고 제품 제외")
#             continue

#         if star:
#             star = star.get_text()
#         else:
#             print("평점 없는 제품 제외")
#             continue
            
#         if count:
#             count = count.get_text()
#             # count = count[1:-1] # count 값에서 괄호 제거
#         else:
#             print("구매수 없는 제품 제외")
#             continue

#         if float(star) >= 4.5 and int(count[1:-1]) > 1000:   #별이 4.5개 이상이고 구매수 1000 이상
#             print(name, price, star, count)


#############조건에 맞는 제품 검색(평점 없는 제품, 광고 제품 제외) 여러 페이지 + 출력 내용 정리 ##############

# for i in range(1,5):
  
#     url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=6&backgroundColor=".format(i)
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     items = soup.find_all("li", attrs={'class':re.compile('^search-product')}) #"search-product"문자열로 시작하는 모든 class 속성 값
#     # print("페이지 정보 : ",i)

#     for item in items:
#         ad_badge = item.find("span", attrs={"class":"ad-badge-text"}) # 광고 제품 
#         star = item.find("em", attrs={"class":"rating"}) 
#         count = item.find("span", attrs={"class":"rating-total-count"})
#         name = item.find("div", attrs={"class":"name"}).get_text() # 제품명
#         price = item.find("strong", attrs={"class":"price-value"}).get_text() # 가격

#         if "레노버" in name:
#             # print("레노버 노트북 제외")
#             continue
        
#         if ad_badge:
#             # print("광고 제품 제외")
#             continue

#         if star:
#             star = star.get_text()
#         else:
#             # print("평점 없는 제품 제외")
#             continue
            
#         if count:
#             count = count.get_text()
#             count = count[1:-1] # count 값에서 괄호 제거
#         else:
#             # print("구매수 없는 제품 제외")
#             continue

#         link = item.find("a", attrs={"class": "search-product-link"})["href"]

#         if float(star) >= 4.5 and int(count) > 1000:   #별이 4.5개 이상이고 구매수 1000 이상
#             # print(name, price, star, count)
#             print(f"제품명 : {name}")
#             print(f"가격 : {price}원")
#             print(f"별 : {star}개 ({count})")
#             print("바로가기 : {}".format("https://www.coupang.com"+ link))
#             print("-"*100)
            

############# 영화 검색(이미지 저장) ##############

# url = "https://search.daum.net/search?w=tot&q=2020%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# images = soup.find_all("img", attrs={"class":"thumb_img"})

# for idx, image in enumerate(images):
#     image_url = image["src"]

#     # if image_url.startwith("//"):  url이 "//"로 시작하는 경우 "https:"를 앞에 추가함
#         # image_url = "https:" + image_url

#     # print(image_url)

#     image_res = requests.get(image_url)
#     image_res.raise_for_status()

#     with open("movie{}.jpg".format(idx + 1), "wb") as f:
#         f.write(image_res.content)

# ############# 영화 검색(이미지 저장) / 2015 ~ 2021년 사이 각 년도의 상위 5개 영화 이미지 저장##############

# for year in range(2015, 2021):
#     url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
#     res = requests.get(url, headers=headers)
#     res.raise_for_status()
#     soup = BeautifulSoup(res.text, "lxml")

#     images = soup.find_all("img", attrs={"class":"thumb_img"})

#     for idx, image in enumerate(images):
#         image_url = image["src"]

#         image_res = requests.get(image_url)
#         image_res.raise_for_status()

#         with open("movie{}_{}.jpg".format(year, idx + 1), "wb") as f:
#             f.write(image_res.content)
        
#         if idx >= 4:
#             break;

############# 네이버 금융(주식)정보 수집 ##############################

# import csv
# import requests
# from bs4 import BeautifulSoup

# url ="https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1"

# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# filename ="시가총액 1-200.csv"
# f = open(filename, "w", encoding="utf-8-sig", newline="") # "utf-8-sig" 문자열이 아닌 Byte Order Mark(BOM)로 처리
# writer = csv.writer(f)

# #타이틀 저장하기(1)
# title = "N	종목명	현재가	전일비	등락률	액면가	시가총액	상장주식수	외국인비율	거래량	PER	ROE	토론실".split("\t")
# writer.writerow(title)

# #타이틀 저장하기(2)
# # data_head = soup.find("table", attrs={"class":"type_2"}).find("thead").find_all("th")
# # tmp_str = list()
# # for dh in data_head:
# #         tmp_str.append(dh.get_text())  
# # writer.writerow(tmp_str) #실제 csv형태로 파일 저장

# data_rows = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr") #table에 있는 전체 row 가져옴
# for row in data_rows:
#     columns = row.find_all("td")    #각각의 row에 있는  td 전부 가져옴
#     # print(columns)
#     if len(columns) <= 1: # tr에  td가 한 개 이하인 경우(줄바꿈 또는 경계선 일 경우) 필요없는 정보 스킵
#         continue
#     data = [column.get_text().strip() for column in columns]  #한 줄 반복문
#     # print(data)
#     writer.writerow(data)


############# Selenium ##############################
# # pip install selenium
# # webdriver 설치(브라우저용)
# # 크롬 버전 확인 : chrome://version
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# current_path = os.path.dirname(__file__)
# driver_path = os.path.join(current_path, "chromedriver")
# driver = os.path.join(driver_path, "chromedriver.exe")

# s = Service(driver)

# # print(driver)

# # browser = webdriver.Chrome("D:\pyworkspace\web_crawling\chromedriver\chromedriver.exe")
# # browser = webdriver.Chrome(driver)

# browser = webdriver.Chrome(service=s)

# # 1. 네이버로 이동
# browser.get("https://www.naver.com/")
# # browser.get("https://www.daum.net")


# # 2. 로그인 버튼 클릭
# # elem = browser.find_element_by_class_name("link_login")
# elem = browser.find_element(By.CLASS_NAME, "link_login")
# elem.click()

# # 3. id, pw 입력 
# # browser.find_element_by_id("id").send_keys("test_id")
# # browser.find_element_by_id("pw").send_keys("test_pw")
# browser.find_element(By.ID, "id").send_keys("test_id")
# browser.find_element(By.ID, "pw").send_keys("test_pw")

# # 4. 로그인 버튼 클릭
# # browser.find_element_by_id("log.login").click()
# browser.find_element(By.ID, "log.login").click()

# time.sleep(3)

# # 5. id, pw 재입력
# browser.find_element(By.ID, "id").clear()
# browser.find_element(By.ID, "pw").clear()
# browser.find_element(By.ID, "id").send_keys("new_id")
# browser.find_element(By.ID, "pw").send_keys("new_pw")

# print(browser.page_source)
# time.sleep(5)


# ############# Selenium (네이버 항공권)##############################
# # pip install selenium
# # webdriver 설치(브라우저용)
# # 크롬 버전 확인 : chrome://version
# import os
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time

# current_path = os.path.dirname(__file__)
# driver_path = os.path.join(current_path, "chromedriver")
# driver = os.path.join(driver_path, "chromedriver.exe")

# browser = webdriver.Chrome(driver)
# browser.get("https://flight.naver.com/") 

# # 출발지 선택
# browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()
# time.sleep(2)
# # 국내 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
# time.sleep(2)
# # 김포 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[4]").click()
# time.sleep(2)
# # 도착지 선택
# browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
# time.sleep(2)
# # 국내 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
# time.sleep(2)
# # 제주도 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[2]").click()
# time.sleep(2)
# # 가는 날 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
# time.sleep(2)
# # 가는날짜 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[3]/button").click()
# time.sleep(2)
# # 오는날짜 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[4]/td[5]/button").click()
# time.sleep(2)
# # 성인 2명, 할인/일반/특가석 선택
# # 직접 작성하도록
# # 항공권 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()

# try:
#     elem = WebDriverWait(browser, 15).until(EC.presence_of_element_located((By.XPATH,"//*[@id='__next']/div/div[1]/div[5]/div/div[2]/div[2]")))
#     print(elem.text)
# finally:
#     browser.quit()

# # time.sleep(20)

############# Selenium, (Requests) 동적페이지 (구글 영화 차트)##############################
import os

import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top"
# "Accept-Language":"ko-KR,ko" 한국으로 설정하지 않으면 기본적으로 request에 미국으로 설정됨.
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36",
           "Accept-Language":"ko-KR,ko"}

res = requests.get(url, headers=headers)
# res = requests.get(url)
res.raise_for_status()
soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"ImZGtf mpg5gc"})
# print(len(movies))

# with open("movies.html", "w", encoding="utf-8") as f:
#     # f.write(res.text)
#     f.write(soup.prettify())


for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    print(title)

############# Selenium 동적페이지 (구글 영화 차트)##############################
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, "chromedriver")
driver = os.path.join(driver_path, "chromedriver.exe")

s = Service(driver)

browser = webdriver.Chrome(service=s)
browser.maximize_window() #브라우저 화면 최대화

url = "https://play.google.com/store/movies/top"

# 페이지 이동
# # 1. 구글플레이 영화 - https://play.google.com/store/movies/top
browser.get(url)

#스크롤 내리기
#모니터(헤상도) 높이 만큼 (1080) 스크롤 내리기 / 자바스크립트 실행
# for idx in range(1,4):
#     # page = idx * 1080
#     browser.execute_script("window.scrollTo(0, {})".format(idx * 1080))
#     time.sleep(3)


# 화면 가장 아래로 스크롤 내리기(한 화면씩)
# browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
# time.sleep(5)

prev_height = browser.execute_script("return document.body.scrollHeight")
# print(scroll_height)

#스크롤 후 로딩 대기 시간
time_interval = 3
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    #페이지 로딩 대기
    time.sleep(time_interval)
    #현재 문서 높이를 가져와서 저장
    curent_height = browser.execute_script("return document.body.scrollHeight")
    #이전 높이와 현재 높이를 비교(같으면 가장 아래까지 스크롤한 상태)
    if curent_height == prev_height:
        break
    prev_height = curent_height
    
print("스크롤 완료")
    
import requests
from bs4 import BeautifulSoup

#페이지 전체 소스 가져오기(page_source)
soup = BeautifulSoup(browser.page_source, "lxml")
    
# movies = soup.find_all("div", attrs={"class":["ImZGtf mpg5gc", "Vpfmgd"]})
movies = soup.find_all("div", attrs={"class":"Vpfmgd"})

print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)
    
    #할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title, " <할인되지 않은 영화 제외> ")
        continue
    
    # 할인된 가격
    price = movie.find("span", attrs={"class","VfPpfd ZdBevf i5DZme"}).get_text()

    # 링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]
    # 올바른 링크 : https://play.google.com + link
    
    print(f"제목 : {title}")
    print(f"할인 전 금액 : {original_price}")
    print(f"할인 후 금액 : {price}")
    print("링크 : ", "https://play.google.com" + link)
    print("-" * 120)

############# 크롬 headless (브라우저를 실행시키지 않고 스크래핑 작업)##############################
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# options = webdriver.ChromeOptions()
# options.headless = True # 브라우저를  띄우지 않음
# options.add_argument("window-size=1920X1080") #실제로 띄우지 않지만 내부적으로 브라우저의 크기 지정

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--mute-audio")
#user_agent를 설정하지 않고 접속을 시도하면 HeadlessChrome으로 User-Agent가 전송되면서 서버에서 접속을 거부할 수 있다.
# chrome_options.add_argument('--user-agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"')


current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, "chromedriver")
driver = os.path.join(driver_path, "chromedriver.exe")

s = Service(driver)

browser = webdriver.Chrome(options=chrome_options, service=s)
browser.set_window_size(1920, 1080)
# browser.minimize_window()
# browser.maximize_window()

# Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36
url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
user_agent = browser.find_element(By.ID, "detected_value")
print(user_agent.text)

# url = "https://play.google.com/store/movies/top"

# # browser.get(url)
# # time.sleep(3)
# # browser.get_screenshot_as_file("screen.png")

##################
################## https://www.google.com/robots.txt
##################


### 퀴즈
# 조회 조건
# https://www.r114.com/?_c=memul&_m=p10&direct=A
# 부동산114 에서 매물 정보
#===============매물 1 ================
# 동부센트레빌 103동
# 월세 80,000 / 320 만원
# 방4개 136.29/114.49㎡ 저층/총23층 
# 남서향으로 채광 우수 내부 수리되어 아주 깔끔하며 정상 협의 입주 
#===============매물 2 ================
# 동부센트레빌 103동
# 월세 80,000 / 320 만원
# 방4개 136.29/114.49㎡ 저층/총23층 
# 남서향으로 채광 우수 내부 수리되어 아주 깔끔하며 정상 협의 입주 


import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

current_path = os.path.dirname(__file__)
driver_path = os.path.join(current_path, "chromedriver")
driver = os.path.join(driver_path, "chromedriver.exe")

s = Service(driver)

browser = webdriver.Chrome(service=s)
browser.maximize_window() #브라우저 화면 최대화

url = "https://www.r114.com/?_c=memul&_m=p10"

# 페이지 이동
browser.get(url)

#스크롤 내리기
#모니터(헤상도) 높이 만큼 (1080) 스크롤 내리기 / 자바스크립트 실행
# for idx in range(1,4):
#     # page = idx * 1080
#     browser.execute_script("window.scrollTo(0, {})".format(idx * 1080))
#     time.sleep(3)


# 화면 가장 아래로 스크롤 내리기(한 화면씩)
browser.execute_script("window.scrollTo(0, 1080)")
time.sleep(3)
browser.execute_script("window.scrollTo(0, 2160)")
time.sleep(3)
browser.execute_script("window.scrollTo(0, 3240)")
time.sleep(3)

soup = BeautifulSoup(browser.page_source, "lxml")

with open("house.html", "w", encoding="utf-8") as f:
    f.write(soup.prettify())

houses = soup.find("ul", attrs={"class":"list_article Best"}).find_all("li")

print(len(houses))

for idx, house in enumerate(houses):   
    title = house.find("strong", attrs={"class":"tit_a"}).get_text()
    rent = house.find("em").get_text()
    rooms = house.find("span", attrs={"class":"info_memul"}).get_text()
    print("============{}번 물건============".format(idx+1))
    print(title)
    print(rent)
    print(rooms)
    
time.sleep(20)