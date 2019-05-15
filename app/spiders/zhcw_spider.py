import requests
import app.spiders as spiders
import app.utils.url_utils as url_utils
import app.spiders as spiders
class ZhcwSpider(object):
    __FIRST_PAGE = 1
    __total_dic = {'count': 0, 'page': 0}
    __page_urls = []
    ssq_list = []
    def __init__(self, url):
        self.__ssq_base_url = url
        self.__first_url = url_utils.replace_url_placeholder(url, self.__FIRST_PAGE)
        self.__first_doc = spiders.get_soup(self.__first_url)
        self.total_count = int(self.__get_total_count())
        self.total_page = int(self.__get_total_page())

    def get_current_page_data(self, current_url):
        page_soup = spiders.get_soup(current_url)
        if page_soup.table is not None:
            table_rows = page_soup.table.find_all('tr')
            for row_num in range(2, len(table_rows)-1):
                row_tds = table_rows[row_num].find_all('td')
                ems = row_tds[2].find_all('em')
                reds = []
                reds.append(int(ems[0].string))
                reds.append(int(ems[1].string))
                reds.append(int(ems[2].string))
                reds.append(int(ems[3].string))
                reds.append(int(ems[4].string))
                reds.append(int(ems[5].string))
                reds.append(int(ems[6].string))
                ssq_obj = spiders.ssq_generate(row_tds[0].string, int(row_tds[1].string), reds)
                self.ssq_list.append(ssq_obj)
        
        return self.ssq_list

    def get_page_urls(self):
        return self.__get_all_page_urls(self.__ssq_base_url)

    def __get_all_page_urls(self, url):
        urls = []
        for page in range(1, self.total_page + 1):
            urls.append(url_utils.replace_url_placeholder(url, page))
        return urls  

    def __get_total_count(self):
        return self.__get_total_dic('count')

    def __get_total_page(self):
        return self.__get_total_dic('page')

    def __get_total_dic(self, key):
        self.__total_dic['page'] = self.__first_doc.find('p', attrs={"class": "pg"}).find_all('strong')[0].text
        self.__total_dic['count'] = self.__first_doc.find('p', attrs={"class": "pg"}).find_all('strong')[1].text
        return self.__total_dic.get(key)


