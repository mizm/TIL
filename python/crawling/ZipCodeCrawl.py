import requests
import xml.etree.ElementTree as elemTree
import datetime
import zipfile

def getDownloadUrl() :
    #다운로드 Url 가져오기
    url = 'http://openapi.epost.go.kr/postal/downloadAreaCodeService/downloadAreaCodeService/getAreaCodeInfo'
    queryParams = '?ServiceKey=AggSeUXyjkR0ETSS4W6bf6erMLfCg6WjfRk518sN9717gpL9LOekNJz%2Fe6gjLvFKS0W6BzoukbUx204wayh%2FAg%3D%3D&dwldSe=2'
    with requests.get(url+queryParams) as url:
        tree = elemTree.fromstring(url.text)
    return tree.find('file').text

def download(url, today, file_name = None):
    # 날짜 경로에 다운로드합니다
	import os
	if not os.path.isdir(today) :
		os.makedirs(today)

	if not file_name:
		file_name = url.split('/')[-1]

	with open(today + "/" + file_name, "wb") as file:
		response = requests.get(url)
		file.write(response.content)
	return file_name


def getNow() :
    #오늘 날짜를 가지고옵니다.
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d')

def unzip(source_file, dest_path):
    source_file = dest_path + '/' + source_file
    with zipfile.ZipFile(source_file, 'r') as zf:
        zipInfo = zf.infolist()
        for member in zipInfo:
            try:
                if member.filename.split('.')[-1] == 'txt' :
                    member.filename = member.filename.encode('cp437').decode('euc-kr', 'ignore')
                    readFileName = member.filename
                    zf.extract(member, dest_path)
            except:
                print(source_file)
                raise Exception('what?!')

def insert(readFileName) :
    with open(readFileName,'r', encoding='UTF8') as f :
        for line in f :
            print(line.split('|'))
# downUrl = getDownloadUrl()
# today = getNow()
# fileName = download(downUrl,today)
# readFileName = unzip(fileName,today)

insert('강원도.txt')