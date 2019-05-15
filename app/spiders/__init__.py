import requests
from pyquery import PyQuery as pq

def get_doc(url):
    """get PyQuery object"""
    try:
        page = requests.get(url)
        page.raise_for_status()
    except requests.RequestException as exc:
        raise exc
    else:
        # page.encoding = 'utf-8'
        doc = pq(page.text)
        return doc
