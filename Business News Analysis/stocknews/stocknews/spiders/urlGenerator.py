import scrapy
import pandas as pd
import re

from stocknews.items import StocknewsItem

class urlGenerator(scrapy.Spider):

	#spider name
    name = "urlGenerator"
    #domains
    allowed_domains = ["livemint.com"]
    #urls
    start_urls = []
    file_name = '../../livemint_data_3.csv'
    df = pd.read_csv(file_name,encoding='iso-8859-1')
    start_urls = df['href'].tolist()
    
    base_url = "https://www.livemint.com/Query/lZy3FU0kP9Cso5deYypuDI/people.html?facet=subSection&page="

    def parse(self, response):
    	print start_urls
        
        