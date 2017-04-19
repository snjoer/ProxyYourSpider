import codecs
import os
import sys

try:
    from setuptools import setup
except:
    from distutils.core import setup

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

NAME = "ProxyYourSpider"

PACKAGES = ["ProxyYourSpider",]

DESCRIPTION = "Proxy your spider and crawl the galaxy."

LONG_DESCRIPTION = read("README.rst")

KEYWORDS = "python"

AUTHOR = "Rafael Cheng"

AUTHOR_EMAIL = "rafaelcheng13@gmail.com"

URL = "https://github.com/Rafael-Cheng/ProxyYourSpider"

VERSION = "1.0.1"

LICENSE = "GPL"

setup(
    name = NAME,
    version = VERSION,
    description = DESCRIPTION,
    long_description = LONG_DESCRIPTION,
    classifiers = [
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Programming Language :: Python',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
    ],
    keywords = KEYWORDS,
    author = AUTHOR,
    author_email = AUTHOR_EMAIL,
    url = URL,
    license = LICENSE,
    packages = PACKAGES,
    include_package_data=True,
    zip_safe=True,
)
