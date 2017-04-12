# -*- encoding:utf-8 -*-

import redis
import requests
from bs4 import BeautifulSoup
from requests.exceptions import SSLError, Timeout, ProxyError

class Proxy(object):
    def __init__(self, size):
        self.size = size
        self.url = "http://proxydb.net/?protocol=http&protocol=https&anonlvl=4"
        self.http_test_url = 'http://httpbin.org/ip'
        self.https_test_url = 'https://httpbin.org/ip'
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)

    def initProxiesPool(self):
        offset = 0
        llen = 0
        while llen < self.size:
            url = self.url + '&offset=' + str(offset)
            response = requests.get(self.url)
            soup = BeautifulSoup(response.text, 'lxml')
            lists = soup.find('tbody').find_all('tr')
            for ls in lists:
                tds = ls.find_all('td')
                proxy = ''.join(tds[0].text.split())
                _type = ''.join(tds[1].text.split()).lower()
                validity = self.checkValidity(_type, proxy)
                print 'check ' + proxy
                if validity == True:
                    print proxy + ' is valid'
                    self.r.lpush(_type, proxy)
                else:
                    print proxy + ' is invalid'
            llen += self.r.llen('http') + self.r.llen('https')
            offset += 50

    def checkValidity(self, _type, proxy):
        proxyDict = {_type : _type + '://' + proxy}
        try:
            if _type == 'http':
                r = requests.get(self.http_test_url, proxies=proxyDict,\
                        timeout=2)
            else:
                r = requests.get(self.https_test_url, proxies=proxyDict,\
                        timeout=2)
        except SSLError:
            return False
        except Timeout:
            return False
        except ProxyError:
            return False
        soup = BeautifulSoup(r.text, 'lxml')
        retDict = eval(soup.find('body').text)
        if proxy.split(':')[0] == retDict['origin']:
            return True
    
    def fetchProxy(self, _type):
        while True:
            if self.r.llen(_type) > 0:
                proxy = self.r.lpop(_type)
                validity = self.checkValidity(_type, proxy)
                if validity == True:
                    self.r.rpush(_type, proxy)
                    break
            else:
                self.initProxiesPool()
        return (_type, proxy)

if __name__ == '__main__':
    proxy = Proxy(20)
    (_type, iport) = proxy.fetchProxy('http')
