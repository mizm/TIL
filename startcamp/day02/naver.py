import requests
import bs4

response = requests.get('https://naver.com').text
soup = bs4.BeautifulSoup(response, 'html.parser')#
#result = soup.select('div.PM_CL_realtimeKeyword_list_base > .ah_l > .ah_item')
result = soup.select('div.PM_CL_realtimeKeyword_list_base a.ah_a')

for item in result :
    st = item.text.strip().split('\n')
    print(f'{st[0]}위는 {st[1]}입니다')
 
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(7) > a

#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(13) > a > span.ah_k
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_roll.PM_CL_realtimeKeyword_rolling_base > div > ul > li:nth-child(13) > a > span.ah_r