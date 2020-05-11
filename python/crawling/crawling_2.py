# crawling wikipedia
import aiohttp
import asyncio
import time

import async_timeout
from bs4 import BeautifulSoup

async def fetch(session, url):
    node = []
    last = []
    response = None
    f_url = 'https://ko.wikipedia.org/'
    # with async_timeout.timeout(4):
        #async with session.get(url) as response:
    try :
        if url[0] == '/' :
            url = url[1:]
        response = await session.get(f_url+url)
        html = await response.text()
        soup = BeautifulSoup(html, 'html.parser')
        categroyList = soup.select('#mw-subcategories > div a')
        #print(html)
        for link in categroyList:
            if link.text.find('틀:') >= 0 or link.text.find('사용자:') >= 0:
                continue
            ## Tag안의 텍스트
            # print(link.text)
            ## Tag의 속성을 가져오기(ex: href속성)
            # print(link.get('href'))
            node.append(link.get('href'))
        pageList = soup.select('#mw-pages > div a')
        # print("###################문서#########################333")
        for link in pageList:
            if link.text.find('틀:') >= 0 or link.text.find('사용자:') >= 0:
                continue
            ## Tag안의 텍스트
            # print(link.text)
            ## Tag의 속성을 가져오기(ex: href속성)
            # print(link.get('href'))
            last.append(link.get('href'))
        return {'node': node , 'last' : last, 'error' : 0}
    except Exception as e:
        print(f"error : {url} message : {e}")
        if response is not None:
            response.close()
        return {'node' : [url],'last': [], 'error' : 1}
    finally :
        if response is not None:
            await response.release()

async def main(webNode):
    async with aiohttp.ClientSession() as session:
        futures = []
        for u in webNode :
            futures.append(asyncio.ensure_future(fetch(session, u)))
        res = await asyncio.gather(*futures)
        return res

if __name__ == '__main__':
    #webNode = ['/wiki/%EB%B6%84%EB%A5%98:%EB%82%98%EB%9D%BC%EB%B3%84_%EC%98%81%ED%99%94', '/wiki/%EB%B6%84%EB%A5%98:%EB%8F%84%EC%8B%9C%EB%B3%84_%EC%98%81%ED%99%94', '/wiki/%EB%B6%84%EB%A5%98:%EB%8C%80%EB%A5%99%EB%B3%84_%EC%98%81%ED%99%94', '/wiki/%EB%B6%84%EB%A5%98:%EC%84%B8%EA%B8%B0%EB%B3%84_%EC%98%81%ED%99%94', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%9E%91%ED%92%88', '/wiki/%EB%B6%84%EB%A5%98:%EC%97%B0%EB%8C%80%EB%B3%84_%EC%98%81%ED%99%94', '/wiki/%EB%B6%84%EB%A5%98:%EC%9C%A0%ED%98%95%EB%B3%84_%EC%98%81%ED%99%94', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EA%B2%80%EC%97%B4', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EB%8B%A8%EC%B2%B4', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%97%90_%EA%B4%80%ED%95%9C_%EB%AA%A9%EB%A1%9D', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EB%B0%95%EB%AC%BC%EA%B4%80', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%82%B0%EC%97%85', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%9D%98_%EC%97%AD%EC%82%AC', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%82%AC%EC%A1%B0', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%ED%8F%AC%EC%8A%A4%ED%84%B0', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%C2%B7%EC%98%81%EC%83%81_%EC%9A%A9%EC%96%B4', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%9D%8C%EC%95%85', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%9D%B4%EB%A1%A0', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%9D%B4%EB%AF%B8%EC%A7%80', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%9D%B8', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EB%A5%BC_%EC%86%8C%EC%9E%AC%EB%A1%9C_%ED%95%9C_%EC%9E%91%ED%92%88', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EC%9E%A5%EB%A5%B4', '/wiki/%EB%B6%84%EB%A5%98:%EC%A0%95%EB%A6%AC%EA%B0%80_%ED%95%84%EC%9A%94%ED%95%9C_%EC%98%81%ED%99%94_%EA%B4%80%EB%A0%A8_%EA%B8%80', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%EA%B4%80%EB%A0%A8_%EC%A7%81%EC%97%85', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%ED%85%94%EB%A0%88%EB%B9%84%EC%A0%84_%EB%84%A4%ED%8A%B8%EC%9B%8C%ED%81%AC', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%ED%8C%AC%EB%8D%A4', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%ED%8F%AC%ED%84%B8', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94_%ED%96%89%EC%82%AC', '/wiki/%EB%B6%84%EB%A5%98:%ED%9D%AC%EA%B7%B9', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%97%90_%EA%B4%80%ED%95%9C_%EB%91%98%EB%9F%AC%EB%B3%B4%EA%B8%B0_%ED%8B%80', '/wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%97%90_%EA%B4%80%ED%95%9C_%ED%86%A0%EB%A7%89%EA%B8%80']
    lastNode = []
    cnt = 0
    loop = asyncio.get_event_loop()
    webNode = ['wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94']
    # webNode = ['wiki/%EB%B6%84%EB%A5%98:%EC%84%B1%EC%86%8C%EC%88%98%EC%9E%90_%EC%98%81%ED%99%94%EC%A0%9C']
    #webNode = ['wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94%EC%83%81_%EC%88%98%EC%83%81%EC%9E%91']
    start = time.time()
    while len(webNode) > 0:
        cnt+=1
        #loop = asyncio.get_event_loop()
        s = len(webNode)
        result = loop.run_until_complete(main(webNode))
        webNode = []
        errorcnt = 0
        for k in result :
            webNode.extend(k['node'])
            for p in k['last'] :
                if p not in lastNode :
                    lastNode.append(p)
            errorcnt += k['error']
        end = time.time()
        print(f"elapsed time = {end - start}s")
        print(f"#{cnt} - next-search : {len(webNode)} last : {len(lastNode)} start : {s} error : {errorcnt}")
        #loop.close()
    loop.close()
    print(len(lastNode))
#
# url = 'https://ko.wikipedia.org/'
# webNode = ['wiki/%EB%B6%84%EB%A5%98:%EC%98%81%ED%99%94']
# #webNode = ['wiki/%EB%B6%84%EB%A5%98:%EB%82%98%EC%8A%A4%ED%8A%B8%EB%A1%9C_%EB%94%94%EC%95%84%EB%A5%B4%EC%A0%A0%ED%86%A0_%EC%88%98%EC%83%81%EC%9E%90']
# lastNode = []
# while webNode :
#     print('####')
#     htmlUrl = url + webNode.pop(0)
#     ## HTTP GET Request
#     req = requests.get(htmlUrl)
#     ## HTML 소스 가져오기
#     html = req.text
#     ## BeautifulSoup으로 html소스를 python객체로 변환하기
#     ## 첫 인자는 html소스코드, 두 번째 인자는 어떤 parser를 이용할지 명시.
#     ## 이 글에서는 Python 내장 html.parser를 이용했다.
#     soup = BeautifulSoup(html, 'html.parser')
#     categroyList = soup.select('#mw-subcategories > div a')
#     for link in categroyList:
#         if link.text.find('틀:') >= 0 or link.text.find('사용자:') >= 0:
#             continue
#         ## Tag안의 텍스트
#         # print(link.text)
#         ## Tag의 속성을 가져오기(ex: href속성)
#         # print(link.get('href'))
#         webNode.append(link.get('href'))
#     pageList = soup.select('#mw-pages > div a')
#     # print("###################문서#########################333")
#     for link in pageList:
#         if link.text.find('틀:') >= 0 or link.text.find('사용자:') >= 0:
#             continue
#         ## Tag안의 텍스트
#         # print(link.text)
#         ## Tag의 속성을 가져오기(ex: href속성)
#         # print(link.get('href'))
#         lastNode.append(link.get('href'))
# print(len(lastNode))
#
# # 실행 코드
#
# endTime = time.time() - startTime
# print(endTime)