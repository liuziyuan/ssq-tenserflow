import requests
from bs4 import BeautifulSoup


def get_soup(url):
    """get PyQuery object"""
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as exc:
        raise exc
    else:
        page.encoding = 'utf-8'
        soup = BeautifulSoup(page.text, 'html.parser')
        return soup

def ssq_generate(date, number, reds):
    ssq_obj = []
    ssq_obj.append(date)
    ssq_obj.append(number)
    ssq_obj.append(reds[0])
    ssq_obj.append(reds[1])
    ssq_obj.append(reds[2])
    ssq_obj.append(reds[3])
    ssq_obj.append(reds[4])
    ssq_obj.append(reds[5])
    ssq_obj.append(reds[6])
    ssq_obj.append(reds[0:5])
    ssq_obj.append(reds)
    return ssq_obj
