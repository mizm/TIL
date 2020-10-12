##pip install geocoder
import geocoder
def getLocation(ip='me') :
    myloc = geocoder.ip(ip)

    return f'{myloc.latlng[0]},{myloc.latlng[1]}'
print(getLocation())

# pip install socket
import socket
def getMyIp() :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('8.8.8.8', 0))
    return s.getsockname()[0]

# 혹시 IP 가 구하는 방법이 필요하시면 getMyIp로 구하시면 됩니다.
# getLocation() 을 호출해도 자신 아이피를 통해 위도 경도를 출력합니다.


import requests
#
def getLocation2() :
    URL = 'https://www.googleapis.com/geolocation/v1/geolocate?key=AIzaSyArRJLHllRxNNK5tuyWyJ2QXCUsQu_qMFA'
    param = {
        'considerIp': True,
    }
    response = requests.post(URL,param)
    response_data = response.json()
    return f"{response_data['location']['lat']},{response_data['location']['lng']}"

print(getLocation2())