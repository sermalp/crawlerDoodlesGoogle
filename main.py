import requests
from bs4 import BeautifulSoup

""" парсинг страницы https://www.google.com/doodles """

def get_new_doodles():
    
    str_host = "https://www.google.com/"

    text_html = requests.get(str_host+'doodles').text
    soup = BeautifulSoup(text_html, 'html.parser')
    
    dict_doodles = dict()
    for link in soup.find_all("div", class_="container"):
        str_text = link.img.get('alt')
        str_link = "http:"+link.img.get('src')
        img = requests.get(str_link).content
        dict_doodles[str_text] = img
    return dict_doodles


""" def get_link(link):
    text_html = requests.get(link).text
    soup = BeautifulSoup(text_html, 'lxml')

    for link in soup.find_all(id='text'):
        r = link.text
        print('!!!')
        print(type(r))
        print(r)
        # break """


if __name__ == '__main__':
    dict_doodles = get_new_doodles()