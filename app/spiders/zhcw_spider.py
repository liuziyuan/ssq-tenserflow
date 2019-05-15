import requests
from pyquery import PyQuery as pq
import app.spiders as spiders
import app.utils.url_utils as url_utils

class ZhcwSpider(object):
    FIRST_PAGE = 1
    total_dic = {'count': 0, 'page': 0}
    def __init__(self, url):
        self.url = url_utils.replace_url_placeholder(url, self.FIRST_PAGE)
        self.first_doc = spiders.get_doc(self.url)
        self.total_count = int(self.__get_total_count())
        self.total_page = int(self.__get_total_page())
        self.urls = self.__get_all_page_urls(url)

    def __get_all_page_urls(self):
        urls = []
        for page in range(self.total_page):
            urls.append(url_utils.replace_url_placeholder(self.url, page))
        return urls  

    def __get_total_count(self):
        return self.__get_total_dic('count')

    def __get_total_page(self):
        return self.__get_total_dic('page')

    def __get_total_dic(self, key):
        p_html = self.first_doc.find('.pg').html()
        p_doc = pq(p_html)
        self.total_dic['page'] = p_doc.find('strong')[0].text
        self.total_dic['count'] = p_doc.find('strong')[1].text
        return self.total_dic.get(key)


