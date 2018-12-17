import requests
import bs4

response = requests.get('https://finance.naver.com/sise').text
soup = bs4.BeautifulSoup(response, 'html.parser')
result = soup.select_one('#KOSPI_now').text
print(result)

doller = requests.get('https://finance.naver.com/marketindex/').text
dsoup = bs4.BeautifulSoup(doller, 'html.parser')
dolresult = dsoup.select_one('#exchangeList > li.on > a.head.usd > div > span.value').text

print('지금 1원/달러 환율은 {0}원 입니다'.format(dolresult))
print(f'지금 원/달러 환율은 {dolresult} 입니다.')

# ctrl + `