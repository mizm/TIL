import pymysql
'''
url_base -> 크롤링 시 href로 전체 url가 아닌 /wiki/ 형식으로 주어지므로 기초가 되는 url을 저장합니다
start_url -> /wiki/분류:영화 에서 영화만 포함된 분류들을 골라 지정하였습니다.
'''

db = pymysql.connect( # db 접속
    user='root',
    passwd='12345678',
    host='127.0.0.1',
    db='crawl',
    charset='utf8'
)
