# crawling wikipedia
from bs4 import BeautifulSoup
import requests
import asyncio  # Python 비동기 지원 모듈입니다.
import aiohttp  # asyncio를 사용하여 HTTP 요청을 하기 위해 사용합니다.
import time
startTime = time.time()

url = 'https://ko.wikipedia.org/'
webNode = ['wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%83%81_%EC%88%98%EC%83%81%EC%9E%91']
#webNode = ['wiki/%EB%B6%84%EB%A5%98:%EB%82%98%EC%8A%A4%ED%8A%B8%EB%A1%9C_%EB%94%94%EC%95%84%EB%A5%B4%EC%A0%A0%ED%86%A0_%EC%88%98%EC%83%81%EC%9E%90']
lastNode = []
while webNode :
    htmlUrl = url + webNode.pop(0)
    ## HTTP GET Request
    req = requests.get(htmlUrl)
    ## HTML 소스 가져오기
    html = req.text
    ## BeautifulSoup으로 html소스를 python객체로 변환하기
    ## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
    ## 이 글에서는 Python 내장 html.parser를 이용했다.
    soup = BeautifulSoup(html, 'html.parser')
    categroyList = soup.select('#mw-subcategories > div a')
    for link in categroyList:
        if link.text.find('틀:') >= 0 or link.text.find('사용자:') >= 0:
            continue
        ## Tag안의 텍스트
        # print(link.text)
        ## Tag의 속성을 가져오기(ex: href속성)
        # print(link.get('href'))
        webNode.append(link.get('href'))
    pageList = soup.select('#mw-pages > div a')
    # print("###################문서#########################333")
    for link in pageList:
        if link.text.find('틀:') >= 0 or link.text.find('사용자:') >= 0:
            continue
        ## Tag안의 텍스트
        # print(link.text)
        ## Tag의 속성을 가져오기(ex: href속성)
        # print(link.get('href'))
        lastNode.append(link.get('href'))
    # if(len(lastNode) > 500) :
    #     break
print(len(lastNode))

# 실행 코드

endTime = time.time() - startTime
print(endTime)