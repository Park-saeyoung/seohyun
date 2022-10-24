####################################    정규식  ###########################################
import requests
import sys
import io

# from selenium.webdriver.common.by import By
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

import re

p = re.compile("ca.e")
# m = p.match('catte')
# print(m)
# print(m.group())

# def print_match(m):
#     if m:
#         print(m.group())
#     else:
#         print("매칭되는 값 없음")
# m = p.match("ttcarett")
# print_match(m)
# m = p.match("carett")
# print_match(m)
# m = p.match("ttcare")
# print_match(m)
# m = p.search("ttcare")
# print_match(m)

# def print_match2(m):
#     if m:       
#         print("m.group() :", m.group()) #맨 앞에 일치하는 문자열이 있으면 문자열 출력
#         print("m.start() :", m.start()) #일치하는 문자열의 첫 번째 index
#         print("m.end(): ", m.end()) #일치하는 문자열의 마지막 index
#         print("m.span()" , m.span()) #일치하는 문자열의 처음/마지막 index
#     else:
#         print("매칭되는 값 없음")

# m = p.match("careabcd")
# m = p.search("abcd care cafe cate")
# print_match2(m)

# lst = p.findall("abcd care cafe cate abcd")
# print(lst)

# lst = p.split("abcd care cafe cate abcd")
# print(lst)


# 1. p = re.compile("검색할 패턴/문자열")
# 2. m.match / m.search 주어진 문자열에서 일치하는 문자열 검색
# 3. list = p.findall 일치하는 모든 문자열을 list로 반환
# 4. list = p.split 지정한 문자열로 전체 문자열을 나눠서(쪼개서) list로 반환

# . : 하나의 문자 ca.e, c.re
# ^ : 첫 번째 문자열 일치    ^the
# $ : 마지막 문자열 일치  end$

# p = re.compile("^The")
p = re.compile("best$")
m = p.search("The best")
# print(m.group())

# txt = "hello planet"
# txt = "The best"
# #Check if the string ends with 'planet':

# # x = re.findall("planet$", txt)
# x = re.findall("The$", txt)
# if x:
#   print("Yes, the string ends with 'best'")
# else:
#   print("No match")

######################################################################################
#크롤링, 스크래핑

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "http://www.naver.com"
# res = requests.get(url, headers=headers)  # 요청시 헤더정보 설정
# res = requests.get(url)  # 요청시 헤더정보 설정
# res.raise_for_status() # 응답 오류 확인
# print(res.text)

# from bs4 import BeautifulSoup

# headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "https://comic.naver.com/webtoon/weekday"
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# print(soup)
# print(soup.title)
# print(soup.title.get_text())
# print(soup.a)
# print(soup.a.get_text())
# print(soup.a.attrs)
# print(soup.a["href"])
# print(soup.a["onclick"])
# print(soup.find("span", attrs={"class":"mask"}))

#print(soup.find("li", attrs={"class":"rank01"}).get_text())
#print(soup.find("li", attrs={"class":"rank02"}).get_text())
#print(soup.find("li", attrs={"class":"rank03"}).get_text())
#print(rank2)
# rank1 = soup.find("li", attrs={"class":"rank01"}) #rank01
# rank2 = rank1.next_sibling.next_sibling #rank02

# rank1=rank2.previous_sibling.previous_sibling
# print(rank1.get_text())
# parents = rank1.parent
# print(parents)

# rank2 = rank1.find_next_sibling("li")
# print(rank2.get_text())
# rank3 = rank2.find_next_sibling("li")
# print(rank3.get_text())

# rank2 = rank3.find_previous_sibling("li")
# print(rank2.get_text())


# rank1 = soup.find("li", attrs={"class":"rank01"})
# ranks = rank1.find_next_siblings("li")

# for rank in ranks:
#         print(rank.a.get_text())

# find = soup.find("a", text="삼매경-32화")
# print(find.get_text())

# webtoons = soup.find_all("a", attrs={"class":"title"})
# for webtoon in webtoons:
#         print(webtoon.get_text())


# week = soup.find_all("div", attrs={"class":"col"})
# for day in week:
#     if day.find("h4", "wed"):
#         webtoons = day.find_all("a", attrs={"class":"title"})
#         break

# # webtoons = week.find_all("a", attrs={"class":"title"})
# for webtoon in webtoons:
#     print(webtoon.get_text())

# webtoons_wed = soup.find_all("h4", attrs={"class":"mon"})
# ul = webtoons_wed[0].find_next_sibling("ul")
# titles = ul.find_all("a", attrs={"class":"title"})
# for title in titles:
#         print(title.get_text())

#####################################################################################

# from bs4 import BeautifulSoup
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# # url = "https://comic.naver.com/webtoon/weekday"
# url = "https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon" #참교육
# res = requests.get(url, headers=headers)
# res.raise_for_status() #에러 발생시 중지
# soup = BeautifulSoup(res.text, "lxml")

# webtoons = soup.find_all("td", attrs={"class":"title"})
# title = webtoons[0].a.get_text()
# # print(title)
# # link = webtoons[0].a["href"]
# # print("https://comic.naver.com/" + link)

# for i in range(len(webtoons)):
#     print(webtoons[i].a.get_text() + " : http://comic.naver.com" + webtoons[i].a["href"])

############################################## 2021-11-08

# from bs4 import BeautifulSoup
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "https://comic.naver.com/webtoon/list?titleId=758037&weekday=mon"
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# total_score = 0

# p_elements = soup.find_all("div", attrs={"class":"rating_type"})
# for element in p_elements:
#         score = element.find("strong").get_text()
#         total_score += float(score)

# print("총 평점 : ", total_score)
# print("평균 별 : ", total_score/len(p_elements))


##############################################

# from bs4 import BeautifulSoup
# from bs4 import BeautifulSoup
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page=1&rocketAll=false&searchIndexingToken=1=5&backgroundColor="
# res = requests.get(url, headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")
# items = soup.find_all("li", attrs={"class": "search-product"})

# for item in items:
#         name = item.find("div", attrs={"class":"name"}).get_text()
#         price = item.find("strong", attrs={"class":"price-value"}).get_text()
#         rating = item.find("em", attrs={"class":"rating"}).get_text()
#         ad_badge = item.find("span", attrs={"class":"ad-badge-text"})     
#         rating_count = item.find("span", attrs={"class":"rating-total-count"}).get_text()
#         rocket = item.find("span", attrs={"class":"rocket"})

#         if ad_badge:
#                 continue
#                 # print("광고제품입니다.")

#         if float(rating) <= 4.5:
#                 continue
#                 # print("별점이 4.5이하인 제품")
        
#         if int(rating_count[1:-1]) < 1000:
#                 continue
#                 print("리뷰수가 1000이상인 제품")
#         if rocket:
#                 continue
#                 print("로켓배송 제품입니다.")

#         # if not item.find("span", attrs={"class":"rocket"}):
#         #     nrd.append(item)

#         print(name, price, rating, rating_count)

####################################쿠팡 여러페이지 검색########################

# from bs4 import BeautifulSoup
# import re

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

# for i in range(1, 5):
#      print("현재 페이지 : {}".format(i))
#      url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={}&rocketAll=false&searchIndexingToken=1=5&backgroundColor=".format(i)
#      res = requests.get(url, headers=headers)
#      res.raise_for_status()
#      soup = BeautifulSoup(res.text, "lxml")
#      items = soup.find_all("li", attrs={"class":re.compile("^search-product")})  #해당 문자열로 시작하는 모든 문자열
#      for item in items:
#         ad_badge = item.find("span", attrs={"class":"ad-badge-text"})

#         # if(item.find(class_="rating")):                                       # 별점이 없는 제품
#         # if(item.find(attrs={"class":"rating"})):                              # 별점이 없는 제품
#         # if(item.find("em", attrs={"class":"rating"})):                        # 별점이 없는 제품
#         #         rating = rating = item.find("em", attrs={"class":"rating"}).get_text()
        
#         if(item.find(class_= "rating")):                                        # 별점이 없는 제품
#                 rating = item.find(attrs={"class":"rating"}).get_text()
#         else: 
#                 rating = 0

#         # if(item.find("span", attrs={"class":"rating-total-count"})):            #리뷰수가 없는 제품
#         #         rating_count = item.find("span", attrs={"class":"rating-total-count"}).get_text()
#         # else:
#         #         rating_count = 0
#         if(item.find(class_= "rating-total-count")):            #리뷰수가 없는 제품
#                 rating_count = item.find(class_= "rating-total-count").get_text()
#         else:
#                 rating_count = 0

#         name = item.find("div", attrs={"class":"name"}).get_text()              #제품 이름(스팩)
#         price = item.find("strong", attrs={"class":"price-value"}).get_text()   #제품 가격    
#         link = item.find("a", attrs={"class":"search-product-link"})["href"]    #제품 링크
#         rocket = item.find("span", attrs={"class":"rocket"})                    #로켓배송 제품

#         if ad_badge:
#                 continue
#         # print("광고제품입니다.")

#         if float(rating) != 0:
#                 continue
#                 # print("별점이 4.5이하인 제품")

#         if int(rating_count) != 0 and (rating_count[1:-1]) < 3000:
#                 # continue
#                 # print("리뷰수가 3000이상인 제품")
#                 print("")
# #      if rocket:
# #             continue
# #             print("로켓배송 제품입니다.")  
        
#         print("제품명 : {}".format(name))
#         print("별점 : {}".format(rating))
#         print("리뷰수 : {}".format(rating_count))
#         print("가격 : {}".format(price))          
#         print("제품 링크 : {}".format("https://www.coupang.com"+link))
#         print("-" * 100)
# #      print("-" * 100)


####################################웹에서 이미지 저장하기########################

# from bs4 import BeautifulSoup
# import re

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

# for year in range(2016, 2021):
#         url = "https://search.daum.net/search?w=tot&q={}%EB%85%84%EC%98%81%ED%99%94%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR".format(year)
#         res = requests.get(url, headers=headers) #URL, headers 정보 설정
#         res.raise_for_status() # 오류 발생시 멈춤
#         soup = BeautifulSoup(res.text, "lxml") #Soup객체 생성
#         images = soup.find_all("img", attrs={"class":"thumb_img"})
#         titles = soup.find_all("a", attrs={"class":"tit_main"})

#         for idx, image in enumerate(images):

#                 image_src = image["src"]
#                 image_res = requests.get(image_src)
#                 image_res.raise_for_status()

#                 # with open("movie.jpg", "wb") as f:  # movie1.jpg, movie2.jpg,
#                 #어벤져서: 시빌워 -> movie_2019_어벤저스-시빌워_1.jpg
#                 with open("movie_{}_{}_{}.jpg".format(year, titles[idx].get_text().replace(":","-"), idx+1),"wb") as f: 
#                         f.write(image_res.content)
#                 print(titles[idx].get_text())
                
#                 if idx >= 4:
#                         break

#2020 ~ 2016 까지 각 년도별 1위 부터 5위 까지의 영화 이미지 저장
# 이미지 이름 : movie_년도_영화제목_순위.jpg


####################################웹에서 데이터 CSV 저장 ########################

# from bs4 import BeautifulSoup
# import csv

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "https://finance.naver.com/sise/sise_market_sum.nhn"
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# filename = "시가총액1-50.csv"

# fd = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(fd)

# data_head = soup.find("table", attrs={"class":"type_2"}).find("thead").find_all("th")

# tmp_str = list()

# for dh in data_head:
#         tmp_str.append(dh.get_text())  
# writer.writerow(tmp_str) #실제 csv형태로 파일 저장

# data_row = soup.find("table", attrs={"class":"type_2"}).find("tbody").find_all("tr")

# for row in data_row:
#         columns = row.find_all("td")
#         if len(columns) <=1:
#                 continue
#         data = [column.get_text().strip() for column in columns]
#         writer.writerow(data)
    
####################################웹에서 데이터 CSV 저장(환율) ########################

# from bs4 import BeautifulSoup
# import csv

# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}
# url = "https://finance.naver.com/marketindex/exchangeList.naver"
# res = requests.get(url,headers=headers)
# res.raise_for_status()
# soup = BeautifulSoup(res.text, "lxml")

# filename = "환율.csv"

# fd = open(filename, "w", encoding="utf-8-sig", newline="")
# writer = csv.writer(fd)

# data_head = soup.find("table", attrs={"class":"tbl_exchange"}).find("thead").find_all("th")

# print(data_head)

# tmp_str = list()

# for idx, dh in enumerate(data_head):
#         if dh.get("class") == "th_ex3" or dh.get("class") == "th_ex4":
#                 continue
#         tmp_str.append(dh.get_text())  
# writer.writerow(tmp_str) #실제 csv형태로 파일 저장

# data_row = soup.find("table", attrs={"class":"tbl_exchange"}).find("tbody").find_all("tr")

# for row in data_row:
#         columns = row.find_all("td")
#         # if len(columns) <=1:
#         #         continue
#         data = [column.get_text().strip() for column in columns]
#         writer.writerow(data)

################################## selenium(네이버 로그인) #####################

# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# current_path = os.path.dirname(__file__)
# driver_path = os.path.join(current_path, "chromedriver")
# driver = os.path.join(driver_path, "chromedriver.exe")

# # print(driver)

# browser = webdriver.Chrome(driver)

# # 1. url("https://www.naver.com")접속
# browser.get("https://www.naver.com")

# # 2. 로그인 앨리먼트 검색
# # elem = browser.find_element_by_class_name("link_login")
# elem = browser.find_element(By.CLASS_NAME, "link_login")

# # 3. 로그인 버튼 클릭
# elem.click()

# # 4. id 앨리먼트검색
# # id = browser.find_element_by_id("id")
# id = browser.find_element(By.ID, "id")
# # 5. 아이디 입력
# id.send_keys("naver-id")
# # 6. 패스워드 앨리먼트 검색
# # pw = browser.find_element_by_id("pw")
# pw = browser.find_element(By.ID, "pw")
# # 7. 패스워드 입력
# pw.send_keys("naver-pw")
# # 8. 로그인 실행(엔터키 입력)
# # pw.send_keys(Keys.ENTER)

# # 로그인 버튼 클릭
# # btn_login = browser.find_element_by_id("log.login")
# browser.find_element(By.ID, "log.login").click()
# # btn_login.click()

# time.sleep(3)

# # 아이디, 비번 삭제 후 재입력
# # id = browser.find_element_by_id("id")
# id = browser.find_element(By.ID, "id")
# # pw = browser.find_element_by_id("pw")
# pw = browser.find_element(By.ID, "pw")
# id.clear()
# pw.clear()

# time.sleep(3)

# id.send_keys("new_naver_id")
# pw.send_keys("new_naver_pwd")

# # btn_login = browser.find_element_by_id("log.login")
# # btn_login.click()
# browser.find_element(By.ID, "log.login").click()

# # print(elem)
# time.sleep(5)

# ################################## selenium(다음 로그인) #####################

# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# current_path = os.path.dirname(__file__)
# driver_path = os.path.join(current_path, "chromedriver")
# driver = os.path.join(driver_path, "chromedriver.exe")

# # print(driver)

# browser = webdriver.Chrome(driver)

# browser.get("https://www.daum.net/")

# elem = browser.find_element(By.XPATH, "//*[@id='inner_login']/a[2]")
# elem.click()

# # browser.find_element(By.XPATH, "//*[@id='inner_login']/a[2]").click()

# id = browser.find_element(By.ID, "id")
# id.send_keys("daum-id")
# pw = browser.find_element(By.ID, "inputPwd")
# pw.send_keys("daum-pwd")

# loginBtn = browser.find_element(By.ID, "loginBtn")
# loginBtn.click()

# time.sleep(5)

# ################################## selenium(네이버 여행정보) #####################
# import os
# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# current_path = os.path.dirname(__file__)
# driver_path = os.path.join(current_path, "chromedriver")
# driver = os.path.join(driver_path, "chromedriver.exe")
# browser = webdriver.Chrome(driver)  # 드라이버
# browser.get("https://flight.naver.com/") 

# # 출발지 선택
# browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[1]").click()
# # 국내 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
# # 김포 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[4]").click()
# # 도착지 선택
# browser.find_element(By.XPATH,"//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]").click()
# # 국내 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/button[1]").click()
# # 제주도 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/section/section/div/button[2]").click()
# # 가는 날 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]").click()
# # 가는날짜 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[2]/table/tbody/tr[3]/td[6]/button").click()
# # 오는날짜 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[10]/div[2]/div[1]/div[2]/div/div[3]/table/tbody/tr[5]/td[6]/button").click()
# # 성인 2명, 할인/일반/특가석 선택
# # 직접 작성하도록
# # 항공권 선택
# browser.find_element_by_xpath("//*[@id='__next']/div/div[1]/div[4]/div/div/button").click()
# time.sleep(20)

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