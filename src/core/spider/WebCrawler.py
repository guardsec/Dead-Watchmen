from urllib.request import urlopen
from link_finder import LinkFinder
from general import *

class spider:

    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file = ''
    queue = set()
    crawled = set()

    def __init__(self, project_name, Base_url, Domain_name):
        spider.project_name = project_name
        spider.Base_url = Base_url
        spider.Domain_name = Domain_name
        spider.Queue_file = spider.project_name + '/queue.txt'
        spider.Crawled_file = spider.project_name + '/crawled.txt'
        self.boot()
        self.crawl_page('SpiderMan 1', spider.Base_url)
        
        @staticmethod
        def boot(self):
            create_project_dir(spider.project_name)
            create_data_files(spider.project_name, spider.base_url)
            spider.queue = file_to_set(spider.queue_file)
            spider.crawled = file_to_set(spider.crawled_file)

        @staticmethod
        def crawl_page()
            
            

