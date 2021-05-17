import requests
from bs4 import BeautifulSoup



def init_soup(content):
    soup = BeautifulSoup(content, 'html.parser')
    return soup


def get_Title(content):
    lis = []
    soup = init_soup(content)
    Title_Tag = soup.find_all('body')
    Title = Title_Tag
    """for i in Title:
        tr = soup.find_all('tr')
        print(i.text)
        for j in tr:
            return j.text"""
    #Scrap orange title________
    """result2 = soup.find_all('font', {'color': 'orange'})
    lista2=[]
    for k in result2:
        lista2.append(k.text)
        print(k.text)"""
    #____________________________

    #Scrap blue title__________________________
    result3 = soup.find_all('a')
    lista3 = []
    for n in result3:
        lista3.append(n.text)
        print(n.text)
    #_______________________



def get_Body(content):
    soup = init_soup(content)
    Body = soup.find_all('div', class_='entry')
    Body = Body[0].get_text()
    return Body


url = "http://www.millersmiles.co.uk/archives/326"
page = requests.get(url)

print(get_Title(page.content))
