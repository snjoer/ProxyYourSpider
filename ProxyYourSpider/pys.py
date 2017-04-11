# -*- encoding:utf-8 -*-

import requests
from bs4 import BeautifulSoup

class Proxy():
    def __init__(self):
        self.url = "http://proxydb.net/?protocol=http&protocol=https&anonlvl=4"
        self.http_test_url = 'http://httpbin.org/ip'
        self.https_test_url = 'https://httpbin.org/ip'

    def getIP(self):
        response = requests.get(self.url)
        soup = BeautifulSoup(response.text, 'lxml')
        lists = soup.find('tbody').find_all('tr')
        for ls in lists:
            tds = ls.find_all('td')
            iport = ''.join(tds[0].text.split())
            _type = ''.join(tds[1].text.split()).lower()
            validity = self.checkValidity(_type, iport)
            if validity == True:
                self.storeToDataBase(_type, iport)

    def checkValidity(self, _type, iport):
        proxyDict = {_type : _type + '://' + iport}
        if _type == 'http':
            r = requests.get(self.http_test_url, proxies=proxyDict)
        else:
            r = requests.get(self.https_test_url, proxies=proxyDict)
        soup = BeautifulSoup(r.text, 'lxml')
        retDict = eval(soup.find('body').text)
        if iport.split(':')[0] == retDict['origin']:
            return True
    
    def storeToDataBase(self, _type, ip):
        # todo
        pass

if __name__ == '__main__':
    proxy = Proxy()
    proxy.getIP()
