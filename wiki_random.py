'''
python 3.5

'''

import requests
import webbrowser

page_count = 0
url = (
    "https://uri.amap.com/marker?position=121.287689,31.234527&name=park&src=mypage&coordinate=gaode&callnative="
    + str(page_count)
)

def load():
    response = requests.get(url)
    if response.ok:
        print(response)
    else:
        response.raise_for_status()

if __name__ == "__main__":
    load()