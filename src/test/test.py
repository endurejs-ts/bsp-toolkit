# from typing import Dict

# from typing import Dict

# def getDict(*args: Dict[str, str]) -> str:
#     result = ', '.join(str(d) for d in args)
#     return result

# a = getDict({ "b": "1" }, { "ab": "2" })
# print(a)

'''
start
'''
from ..main.index import *

url = settings("https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC")

value = getText(find("p", url))
print(value)