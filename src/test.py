import requests

url = 'https://www.naver.com'
response = requests.get(url) # url에 get 요청을 보냄
print(response) # 200은 성공을 의미
print(response.text)  # HTML 소스 출력
