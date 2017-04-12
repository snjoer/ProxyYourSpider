# ProxyYourSpider

[![AUR](https://img.shields.io/aur/license/yaourt.svg)](https://github.com/Rafael-Cheng/ProxyYourSpider/blob/master/LICENSE)
[![AUR](https://img.shields.io/badge/python-2.7-green.svg)](https://github.com/scrapy/scrapy)
[![Maintenance](https://img.shields.io/maintenance/yes/2017.svg)](https://github.com/Rafael-Cheng/ProxyYourSpider)

## Introduction
   Getting banned by websites can be really annoying. Given that the free proxy ips available on the Interent are generally hard to use. This project aims to provide a library with which spider programmers can easily fake the ip of their spider.

## Usage
   Generally, you only need to call fetchProxy method to fet a proxyyou desire.
   ![](https://github.com/Rafael-Cheng/ProxyYourSpider/blob/master/usage.gif)

   However, you should bear in mind that run.py should be executed first and keep alive while using ProxyYourSpider.

   Just execute run.py like:
   `python run.py 20`
   here 20 is the number of proxies you need.
   ![](https://github.com/Rafael-Cheng/ProxyYourSpider/blob/master/run_launch.png)

   Another thing worth mention is that run.py should be KEEP ALIVE while using ProxyYourSpide. It will continuously check whether the available proxies in your proxies pool is sufficient.

   Notice: You also need to keep Redis alive since it is our database on which we store our proxies.

## Requirements
   * Python 2.7
   * Redis
   * Requests
   * BeautifulSoup
   * Works on Linux, Mac OSX, Windows, BSD

## Installation
   Todo

## License
   The license of this project is GPL license.
