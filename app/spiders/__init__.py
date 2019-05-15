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
