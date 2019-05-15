import requests
import app.spiders as spiders
import app.utils.url_utils as url_utils
import lxml
class ZhcwSpider(object):
    FIRST_PAGE = 1
    total_dic = {'count': 0, 'page': 0}

    red_num = [] #历史上开出的红球
    blue_num = [] #历史上开出的蓝球

    def __init__(self, url):
        self.url = url_utils.replace_url_placeholder(url, self.FIRST_PAGE)
        self.first_doc = spiders.get_soup(self.url)
        self.total_count = int(self.__get_total_count())
        self.total_page = int(self.__get_total_page())
        self.urls = self.__get_all_page_urls(url)

    def get_ssq_history(self):
        for current_url in self.urls:
            current_doc = spiders.get_soup(current_url)

    def get_data_table(self):
        page_soup = spiders.get_soup(self.url)
        if self.first_doc.table is not None:
            table_rows = page_soup.table.find_all('tr')
            for row_num in range(2, len(table_rows)-1):
                row_tds = table_rows[row_num].find_all('td')
                ems = row_tds[2].find_all('em')
                # result = '开奖日期:'+ row_tds[0].string +','+'期号:'+ row_tds[1].string +', '+ems[0].string+' '+ems[1].string+' '+ems[2].string+' '+ems[3].string+' '+ems[4].string+' '+ems[5].string+' '+ems[6].string
                result = row_tds[0].string +','+ row_tds[1].string +', '+ems[0].string+' '+ems[1].string+' '+ems[2].string+' '+ems[3].string+' '+ems[4].string+' '+ems[5].string+' '+ems[6].string
                # local_file.write(result+'\n')
                print(result)
                self.red_num.append(ems[0].string) # 红球1
                self.red_num.append(ems[1].string) # 红球2
                self.red_num.append(ems[2].string) # 红球3
                self.red_num.append(ems[3].string) # 红球4
                self.red_num.append(ems[4].string) # 红球5
                self.red_num.append(ems[5].string) # 红球6
                self.blue_num.append(ems[6].string) # 蓝球

    def __get_all_page_urls(self, url):
        urls = []
        for page in range(1, self.total_page):
            urls.append(url_utils.replace_url_placeholder(url, page))
        return urls  

    def __get_total_count(self):
        return self.__get_total_dic('count')

    def __get_total_page(self):
        return self.__get_total_dic('page')

    def __get_total_dic(self, key):
        # p_html = self.first_doc.find('.pg').html()
        # p_doc = pq(p_html)
        self.total_dic['page'] = self.first_doc.find('p', attrs={"class": "pg"}).find_all('strong')[0].text
        self.total_dic['count'] = self.first_doc.find('p', attrs={"class": "pg"}).find_all('strong')[1].text
        return self.total_dic.get(key)


