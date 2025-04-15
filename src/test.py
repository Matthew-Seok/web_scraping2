import requests
from bs4 import BeautifulSoup

url = 'https://www.naver.com'
response = requests.get(url) # url에 get 요청을 보냄
# print(response) # 200은 성공을 의미
# # print(response.text)  # HTML 소스 출력

# (위의 HTML 소스 대신 테스트용 html을 사용하기 위한 예제)
html = """
<nav class="menu-box-1" id="menu-box">
  <ul>
    <li>
      <a class="naver a b c d" href="https://www.naver.com">네이버로 이동</a>
    </li>
    <li>
      <a class="google" href="https://www.google.com">구글로 이동</a>
    </li>
    <li>
      <a class="daum" href="https://www.daum.net">다음으로 이동</a>
    </li>
  </ul>
</nav>
"""
# BeautifulSoup 객체 생성
soup = BeautifulSoup(html, 'html.parser')

# ! find 사용법

# html 상에 있는 첫 번째 li를 가져온다
print(soup.find('li'))

# html 상에 있는 첫 번째 a를 가져온다
print(soup.find('a'))

# ! find_all 사용법
# html 상에 있는 모든 li를 검색해서 가져온다.
# 가져온 데이터는 리스트 객체로 변환된다
print(soup.find_all('li'))

# 위 코드를 반복문을 이용한 순회
find_li = soup.find_all('li');

for idx, li in enumerate(find_li):
  print(f"{idx} : {li}")

# html 상에 있는 모든 a를 검색해서 모두 가져온다.
print(soup.find_all('a'))

find_a = soup.find_all('a')

for idx, a in enumerate(find_li):
  a_text = a.get_text().strip()
  print(f"{idx} : {a_text.strip()}")

# ! select_one() 테스트
# class 이름이 menu-box-1 인 엘리먼트 검색
print("== select_one 테스트, class 검색 ==")
print(soup.select_one('.menu-box-1'))

# id 이름이 menu-box-1 인 엘리먼트 검색
print("== select_one 테스트, id 검색 ==")
print(soup.select_one('#menu-box'))

# nav > ul > li : nav의 자식의 ul, ul의 자식인 li를 검색
print("== select_one 테스트, 선택자 검색 ==")
print(soup.select_one('nav > ul > li'))

# ! select() 테스트
# 1. select()

# 반복문을 이용하여 데이터 순회
select_a = soup.select('.menu-box-1 a')

# v1 : 엘리먼트 속성값 가져오기
print("== 엘리먼트 속성값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(a.attrs)  # attrs : 엘리먼트의 속성을 딕셔너리 객체로 변환

# v2 : 엘리먼트 href 속성값 가져오기
print("== 엘리먼트 href 속성값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(a.attrs['href'])  # href 키로 접근하여 속성값 가져오기

# v3 : 엘리먼트 class 속성값 가져오기
print("== 엘리먼트 class 속성값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(a.attrs['class'])  # class 키로 접근하여 속성값 가져오기

# v1 : 엘리먼트의 text 값 가져오기
print("== 엘리먼트의 text 값 가져오기 ==")
for idx, a in enumerate(select_a):
  print(f"{idx} : {a.get_text()}")