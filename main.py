from app.utils import yaml_utils
from app.spiders.zhcw_spider import ZhcwSpider

yaml_dic = yaml_utils.get_config_yaml()
zhcw_ssq_url = yaml_dic['zhcw_ssq_url']

zhcw_spider = ZhcwSpider(zhcw_ssq_url)
page_urls = zhcw_spider.get_page_urls()
for current_url in page_urls:
    zhcw_spider.get_current_page_data(current_url)






