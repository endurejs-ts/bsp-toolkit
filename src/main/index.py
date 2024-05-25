from typing import Any
from bs4 import BeautifulSoup, NavigableString, ResultSet, Tag
import requests
# import re

# request.get(url)
def settings(url: str) -> requests.Response:
    # url_pattern_regexp = r'^https://[\w\.-]+\.\w+$'
    # if re.match(url_pattern_regexp, url):
    #     value_urls = requests.get(url)
    #     return value_urls
    
    # else:
    #     raise ValueError("url doesnt like that, url typically start http or https")
    value_url = requests.get(url)
    return value_url
    
def find(elements: str, response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    soup_value = soup.find(elements)

    return soup_value

def getText(value: Tag | NavigableString | None) -> str:
    return value.text

# url = settings("https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")

# value = getText(find("p", url))
# print(value)

def findALL(elements: str, response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    soup_value = soup.find_all(elements)

    return soup_value

# url = settings("https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")

# value = getText(findALL("p", url))
# print(value) errorable

def getTextByALL(value: ResultSet[Any]) -> str:
    # 모든 요소의 텍스트를 리스트에 저장
    prt = [p.text for p in value]

    # 리스트의 모든 텍스트를 하나의 문자열로 결합
    return "\n".join(prt)

# url = "https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"
# res = requests.get(url)

# soup = BeautifulSoup(res.text, "html.parser")
# h1all = soup.find_all("p")
# print(h1all)

url = settings("https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")
# value = getTextByALL(findALL("p", url))
# print(value)

def getTextByALLindex(value: ResultSet[Any], index: int):
    prt = [p.text for p in value]

    return f"{prt[index]}"

vl2 = getTextByALLindex(findALL("p", url), 2)
print(vl2)

def selectByClass(elements: str, attrs: str, response: requests.Response) -> ResultSet[Tag]:
    selector = f"{elements}.{attrs}"

    soup = BeautifulSoup(response.text, "html.parser")
    sbc_value = soup.select(selector)

    return sbc_value

def select(attr: str, response: requests.Response) -> ResultSet[Tag]:
    soup = BeautifulSoup(response.text, "html.parser")
    s_value = soup.select(attr)

    return s_value

def selectOne(attr: str, response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    so_value = soup.select_one(attr)

    return so_value

def selectOneByClass(elements: str, attr: str, response: requests.Response):
    selector = f"{elements}.{attr}"

    soup = BeautifulSoup(response.text, "html.parser")
    sobc_value = soup.select_one(selector)

    return sobc_value

def checkIfthereIsah1(response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    cii_value = soup.find("h1")

    if cii_value:
        return True
    
    else: return False

def customCheckIfthereIsa(elements: str, response: requests.Response):
    soup = BeautifulSoup(response.text, "html.parser")
    ccii_value = soup.find(elements)

    return ccii_value

