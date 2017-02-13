from urllib.request import urlopen
from urllib.request import urlparse
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    includeUrl = urlparse(includeUrl).scheme + "://" + urlparse(includeUrl).netloc
    internalLinks = []
    #找出所有以"/"开头的链接
    for link in bsObj.findAll('a', href = re.compile('^(/|.{0,2})' + includeUrl + ')')):
        if link.attrs['href'] is not None:
            href = 'http://' + re.sub('^(.|/)+','',link.attrs['href'])
            if link.attrs['href'] not in internalLinks:
                #if (link.attrs['href'].startswith('/')):
                internalLinks.append(includeUrl + link.attrs['href'])
                #else:
                    #internalLinks.append(link.attrs['href'])
    return internalLinks

#获取页面所有内链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    #找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll('a',
                        {'href': re.compile('^(http)((?!' + excludeUrl + ').)*$')}):
        if link.attrs['href'] is not None:
            href = link.attrs['href']
            if href not in externalLinks:
                externalLinks.append(href)
    return externalLinks

def splitAddress(address):
    addressParts = address.replace("http://", "").split("/")
    return addressParts

def getRandomExternalLink(startlingPage):
    html = urlopen(startlingPage)
    bsObj = BeautifulSoup(html, "html.parser")
    externalLinks = getExternalLinks(bsObj, splitAddress(startlingPage)[0])
    if len(externalLinks) == 0:
        print("No external Links, looking around the site for one")
        #domain = urlparse(startlingPage).scheme + "://" + urlparse(startlingPage).netloc
        internalLinks = getInternalLinks(bsObj, splitAddress(startlingPage)[0])
        return (getRandomExternalLink(internalLinks[random.randit(0,len(internalLinks) - 1)]))
    else:
        return externalLinks[random.randint(0, len(externalLinks) - 1)]

def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print("Random external link is: " + externalLink)
    try:
        followExternalOnly(externalLink)
    except (HTTPError, ValueError, URLError):
        followExternalOnly(startingSite)
    #followExternalOnly(externalLink)

followExternalOnly("http://www.163.com")