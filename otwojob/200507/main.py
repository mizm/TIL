from urllib.parse import unquote_plus
from bs4 import BeautifulSoup
import requests
import re
import wikipediaapi
import json

cursor = db.cursor() # 커서 가져오기

count = 0

wiki = wikipediaapi.Wikipedia( language='ko', extract_format=wikipediaapi.ExtractFormat.WIKI) # wikipedia api 사용
url_base = 'https://ko.wikipedia.org'
start_urls = ('/wiki/분류:나라별_영화','/wiki/분류:도시별_영화','/wiki/분류:대륙별_영화','/wiki/분류:세기별_영화','/wiki/분류:영화_작품',
              '/wiki/분류:연대별_영화','/wiki/분류:유형별_영화','/wiki/분류:영화_목록','/wiki/분류:장르별_영화','/wiki/분류:영화를_소재로_한_영화',
              '/wiki/분류:영화_제작을_소재로_한_영화','/wiki/분류:포르노그래피를_소재로_한_영화')
# category_blacklist = ('텔레비전_에피소드_목록',"애니메이션_에피소드_목록")

'''
table -> 중복을 체킹하기 위한 테이블입니다. table[_hash(url)] 에 값이 0이 아니면 이전에 방문한 url입니다.
상태는
0 아직 본 적 없음
1 대기중
2 파싱 했음
입니다.
'''
table = [0 for _ in range(1<<24)]

'''
mask -> 해싱할 때 크기를 조절하기 위한 마스킹 정보가 담긴 변수입니다.

_hash -> 문자열을 적절하게 해싱하여 2^24보다 작은 음이아닌 정수 값으로 반환합니다.
'''
mask = (1<<24)-1
def _hash(x):
    '''
    파이썬에 내장된 해싱함수로 해싱값을 정수로 구합니다.
    값이 음수인 경우 양수로 변환하고 h에 저장
    h에 저장된 값의 비트를 반대로 뒤집어 k에 저장
    """
    t += h&mask
    t ^= k&mask
    h>>=24
    k>>=24
    """
    를 h가 0이 될 때까지 반복합니다.
    '''
    h = hash(x)
    if h < 0:h *= -1
    b = bin(h)[::-1]
    b = b[:b.index('b')]
    k = int(b,2)
    t = 0
    while h:
        t += h&mask
        t ^= k&mask
        h >>= 24
        k >>= 24
    return t&mask

'''
방문하지 않길 원하는 url을 미리 방문했다고 표시합니다.
'''
table[_hash("/wiki/영화")] = 1

def parse2(x):
   ret = dict()
   if x.text:
      ret['text'] = x.text
   if x.sections:
      ret['subsections'] = dict()
      for i in x.sections:
         ret['subsections'][i.title] = parse2(i)
   return ret

def parse(url):
    global count
    '''
    /wiki/분류:~~~ 을 파싱해주는 함수입니다.
    '''
    url = url_base + url                        # 인자로 들어온 url에 base_url을 덧붙여 해당 url에 접속할 수 있도록 합니다.
    html = unquote_plus(requests.get(url).text) # 해당 url에 접속하여 html을 받고 url decoding을 해줍니다.

    bs = BeautifulSoup(html, 'html.parser')     # BeautifulSoup으로 파싱해줍니다.

    all_urls = [i['href'] for i in bs.findAll('a',attrs={'href':re.compile('^(/wiki/).*$')},limit=10000)]
    # html에서 모든 a태그를 구하고 그 중 "/wiki"로 시작하는 것만 가져옵니다
    # category_urls = [i for i in all_urls if i.startswith('/wiki/분류:') and '영화' in i and '영화_감독' not in i]
    # 가져온 url 중 영화에 관련된 분류에 해당하는 url만 가져옴니다
    category_urls = [i \
    for i in all_urls \
    if table[_hash(i)] == 0 and \
    i.startswith('/wiki/분류:') and \
    '영화' in i  and \
    '영화_감독' not in i and \
    '영화_배우' not in i and \
    '영화_프로듀서' not in i and \
    '출연진' not in i and \
    '영화_제작자' not in i and \
    '영화_편집자' not in i and \
    '영화_평론가' not in i and \
    '영화_배우' not in i and \
    '텔레비전' not in i and \
    '영화인' not in i and \
    '영화_각본' not in i and \
    '각본' not in i and \
    '영화_감독' not in i and \
    '영화_단체' not in i and \
    '스튜디오' not in i and \
    '엔터테이먼트' not in i and \
    'E&M' not in i and \
    '영화_제작사' not in i and \
    '감독_영화' not in i and \
    '영화_감독' not in i]            # 가져온 url 중 영화에 관련된 분류에서 적당히 필터링하여 가져옴
    page_urls = [i \
    for i in all_urls \
    if table[_hash(i)] == 0 and \
    ':' not in i and \
    i != '/wiki/위키미디어_공용' and \
    '텔레비전' not in i]  # 가져온 url 중 텔레비전에 관련되지 않은 일반 문서에 해당하는 url만 가져옵니다

    for i in page_urls + category_urls: # 대기중인 url들을 1로 설정해줍니다.
        table[_hash(i)] = 1

    for url in page_urls:       # 일반 문서 url에 접속하여 html을 저장하는 반복문 입니다.
        x = _hash(url)
        if table[x] == 2:continue    # 중복을 체크합니다.
        table[x] = 2             # 방문 표시를 합니다.
        print(url)
        page = unquote_plus(requests.get(url_base+url).text)    # 페이지에 접속하여 html을 받습니다.
        # print(page)
        with open(f"out/{url.split('/')[-1].replace('_',' ')}.html", 'w') as f:
           f.write(page)
           count+=1
           print(count)

        page_py = wiki.page(url.split('/')[-1])

        if page_py.exists():
            out = dict()

            out['title'] = page_py.title
            out['정의'] = page_py.summary

            soup = BeautifulSoup(page,'html.parser')
            go = soup.find('table')
            try:
                for tr in go.find_all('tr'):
                    try:
                        if tr.find('th'):
                            out[tr.find('th').text] = tr.find('td').text
                    except:
                        pass
            except:
                continue

            print('!')
            for i in page_py.sections: # 섹션 별로
               out[i.title] = parse2(i) # wiki 모듈을 이용해서 json으로 가져오기

            with open(f"json/{url.split('/')[-1].replace('_',' ')}.json",'w',encoding='utf-8') as f: # json 파일 저장
                json.dump(out,f,indent="\t",ensure_ascii=False)

            data = db.escape_string(page_py.text)
            # print(data)
            try:
                command = 'insert into movie(name,summary,content) values ("'+db.escape_string(page_py.title)+'","'+db.escape_string(page_py.summary)+'","'+data+'");'
                cursor.execute(command) # 명령 실
                db.commit() # 값 넣은거 저장
            except:
                pass

    for url in category_urls:   # 분류 url에 접속하여 파싱하는 것을 반복하는 반복문입니다.
        x = _hash(url)
        if table[x] == 2:continue    # 중복을 체크합니다.
        table[x] = 2            # 방문 표시를 합니다.
        print(url)
        parse(url)              # 해당 url을 새롭게 파싱합니다.

for url in start_urls:  # start_urls에 있는 url들을 파싱하는 반복문입니다.
    parse(url)