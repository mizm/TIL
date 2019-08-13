import os
import requests
import csv
import bs4 
class use_api :
    def __init__(self,url) :
        self.url = url
    def kobis_response(self,params) :
        res = requests.get(self.url,params=params)
        return res.json()
    def naver_response(self,params,header) :
        res = requests.get(self.url,params=params,headers=header)
        return res.json()
def makeboxoffice(kobis_key) :
    day_boxoffice_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json'
    week_boxoffice = use_api(week_boxoffice_url)
    dates = ['20190113','20190106','20181230','20181223','20181216','20181209','20181202','20181125','20181118','20181111']
    movie_list = {}
    for date in dates :
        week_params = {
            'key' : kobis_key,
            'targetDt' : date,
            'weekGb' : '0'    
        }
        item = week_boxoffice.kobis_response(week_params)
        for i in item['boxOfficeResult']['weeklyBoxOfficeList'] :
            if not movie_list.get(i['movieCd']) :
                movie_list.update({i['movieCd'] : {'title' : i['movieNm'], 'audience' : i['audiAcc'], 'recorded_at' : date}})
        with open('boxoffice.csv','w',newline='',encoding='utf8') as f:
            writer = csv.DictWriter(f,fieldnames=['movie_code','title','audience','recorded_at'])
            writer.writeheader()
            for key,value in movie_list.items():
                data = { 'movie_code' : key }
                for key1,value1 in value.items() :
                    data.update({key1 : value1})
                writer.writerow(data) 
def search_movie(csvfile,item) :
    movie_code_list = []
    with open(csvfile,'r',newline='',encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            movie_code_list.append(row[item])
    return movie_code_list

def movie_details(kobis_key) :
    movie_details_url = 'http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json'
    movie_details = use_api(movie_details_url)
    movie_code_list = search_movie('boxoffice.csv','movie_code')
    details_list = []
    for code in movie_code_list:
        params = {
            'key' : kobis_key,
            'movieCd' : code
            #code
        }
        item = movie_details.kobis_response(params)
        i = item['movieInfoResult']['movieInfo']
        tempdic={}
        tempdic.update({'movie_code' : i['movieCd']})
        tempdic.update({'movie_name_ko' : i['movieNm']})
        tempdic.update({'movie_name_en' : i['movieNmEn']})
        tempdic.update({'movie_name_og' : i['movieNmOg']})
        tempdic.update({'prdt_year' : i['prdtYear']})
        tempdic.update({'directors' : i['directors'][0]['peopleNm']})
        tempdic.update({'watch_grade_nm' : i['audits'][0]['watchGradeNm']})
        strgenres = ''
        for j in i['genres'] :
            strgenres += '/' + j['genreNm']
        tempdic.update({'genres' : strgenres[1:]})
        for j in range(1,4) :
            actnum = 'actor'+str(j)
            if j-1 < len(i['actors']):
                actname = i['actors'][j-1]
                tempdic.update({actnum : actname['peopleNm']})
            else :
                tempdic.update({actnum : 'none'})
        details_list.append(tempdic)
    with open('movie.csv','w',newline='',encoding='utf8') as f:
        writer = csv.DictWriter(f,fieldnames=['movie_code','movie_name_ko','movie_name_en','movie_name_og','prdt_year','genres','directors','watch_grade_nm','actor1','actor2','actor3'])
        writer.writeheader()
        for i in details_list :
            writer.writerow(i)

def naver_movie_search(naver,headers) :
    movie_name_list = search_movie('movie.csv','movie_name_ko')
    movie_code_list = search_movie('movie.csv','movie_code')
    movie_naver_list = []
    for idx,name in enumerate(movie_name_list) :
        params = { 'query' : name}
        item = naver.naver_response(params,headers)
        t=item['items'][0]
        tempdic = {} 
        tempdic.update({'movie_code': movie_code_list[idx]})
        tempdic.update({'thumb_url':t.get('image')})
        tempdic.update({'link_url':t['link']})
        tempdic.update({'user_rating':t['userRating']})
        movie_naver_list.append(tempdic)
    with open('movie_naver.csv','w',newline='',encoding='utf8') as f:
        writer = csv.DictWriter(f,fieldnames=['movie_code','thumb_url','link_url','user_rating'])
        writer.writeheader()
        for temp in movie_naver_list :
            writer.writerow(temp)
            
def naver_image_down(naver,headers) :
    image_list = search_movie('movie_naver.csv','thumb_url')
    movie_code_list = search_movie('movie_naver.csv','movie_code')
    for idx, item in enumerate(image_list) :
        image_file = requests.get(item)
        jpgname = 'images/'+movie_code_list[idx]+'.jpg'
        with open(jpgname,'wb') as f:
            f.write(image_file.content)
            
                
            

            

# # kobis
# kobis_key = os.getenv('KOBIS_KEY')
# naver_url = 'https://openapi.naver.com/v1/search/movie.json'
# headers = { 'X-Naver-Client-Id' : os.getenv('NAVER_ID') , 'X-Naver-Client-Secret': os.getenv('NAVER_SECRET') }
# naver = use_api(naver_url)
# # makeboxoffice(kobis_key)
# movie_details(kobis_key)
# naver_movie_search(naver,headers)
# naver_image_down(naver,headers)