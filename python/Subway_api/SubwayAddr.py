import requests
import xml.etree.ElementTree as elemTree
import datetime
import zipfile

class subway :
    def __init__(self,node) :
        self.statnId = node.find('statnId').text
        self.statnNm = node.find('statnNm').text
        self.subwayId = node.find('subwayId').text
        self.subwayNm = node.find('subwayNm').text
        self.subwayXcnts = node.find('subwayXcnts').text
        self.subwayYcnts = node.find('subwayYcnts').text
    
    def __str__(self) :
        return self.statnId + '\t' + self.statnNm + '\t' + self.subwayId + '\t' + self.subwayNm + '\t' + self.subwayXcnts + '\t' + self.subwayYcnts

def getSubwayName(readFileName) :
    subwayNames = []
    with open(readFileName, 'r', encoding='UTF8') as f :
        for line in f :
            subwayNames.append(line.split("\n")[0])
    return subwayNames

def getSubwayInfo(subwayNm) :
    #다운로드 Url 가져오기
    url = 'http://swopenAPI.seoul.go.kr/api/subway/484d6d465369646f39317175556c52/xml/stationInfo/0/5/' + subwayNm

    with requests.get(url) as url:
        #print(url.text)
        tree = elemTree.fromstring(url.text)
        #print(tree.find('RESULT').find('status').text)
        subways = []
        for node in tree.findall('row') :
            subways.append(subway(node))
    return subways

def createFile(subways) :
    with open("SubwayInfo.txt", 'w', encoding='UTF8') as f :
        for subway in subways :
            f.write(str(subway) + '\n')

        
subwayNames = getSubwayName("역이름.txt")
subways = []
for nm in subwayNames :
    subways.extend(getSubwayInfo(nm))
    print(nm)
createFile(subways)

# for i in getSubwayInfo('강남대') :
#     print(str(i))

