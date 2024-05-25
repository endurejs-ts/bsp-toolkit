from bs4 import BeautifulSoup, NavigableString, Tag
import requests
import re

# request.get(url)
def settings(url: str) -> requests.Response:
    url_pattern_regexp = r'^https://[\w\.-]+\.\w+$'
    if re.match(url_pattern_regexp, url):
        value_urls = requests.get(url)
        return value_urls
    
    else:
        raise ValueError("url doesnt like that, url typically start http or https")
    
def find(elements: str, response: requests.Response):
    soup = BeautifulSoup(response.text, "html-parser")
    soup_value = soup.find(elements)

    return soup_value

def getText(value: Tag | NavigableString | None):
    return value.text

