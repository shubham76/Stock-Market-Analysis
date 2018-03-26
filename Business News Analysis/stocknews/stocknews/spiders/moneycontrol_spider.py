import scrapy
from stocknews.items import StocknewsItem

class MoneycontrolSpider(scrapy.Spider):
    
    #spider name
    name = "moneycontrol_spider"
    #domains
    allowed_domains = ["moneycontrol.com"]
    #urls 1 to 100
    start_urls = []
    
    for i in range(2,0,-1):
        
        url_start = "http://www.moneycontrol.com/news/all-news-All-"
        url_end = "-next-0.html"
        temp = url_start+str(i)+url_end
        start_urls.append(temp)
    
        
    def parse(self, response):

        title_start = "/html/body[@id='newsn']/section[@id='mc_content']/section[@class='pgWrapper clearfix PT10']/section[@class='colLft_in']/div[@class='wbg']/div[@class='artiCol PR']/div[@class='clearfix']/div[2]/ul[@class='nws_listing']/li["
        #title_end = "]/div[@class='clearfix']/div[@class='ohidden']/h2/a/@title"                
        title_end = "]/div[@class='clearfix']/div[@class='ohidden']/h2"                
        intro_start = "/html/body[@id='newsn']/section[@id='mc_content']/section[@class='pgWrapper clearfix PT10']/section[@class='colLft_in']/div[@class='wbg']/div[@class='artiCol PR']/div[@class='clearfix']/div[2]/ul[@class='nws_listing']/li["
        #intro_end = "]/div[@class='clearfix']/div[@class='ohidden']/p[@class='MT2']/text()"
        intro_end = "]/div[@class='clearfix']/div[@class='ohidden']/p[@class='MT2']"
        date_start = "/html/body[@id='newsn']/section[@id='mc_content']/section[@class='pgWrapper clearfix PT10']/section[@class='colLft_in']/div[@class='wbg']/div[@class='artiCol PR']/div[@class='clearfix']/div[2]/ul[@class='nws_listing']/li["
        #date_end = "]/div[@class='clearfix']/div[@class='ohidden']/p[@class='nws_datetx MT5']/text()"
        date_end = "]/div[@class='clearfix']/div[@class='ohidden']/p[@class='nws_datetx MT5']"
        href_start = "/html/body[@id='newsn']/section[@id='mc_content']/section[@class='pgWrapper clearfix PT10']/section[@class='colLft_in']/div[@class='wbg']/div[@class='artiCol PR']/div[@class='clearfix']/div[2]/ul[@class='nws_listing']/li["
        href_end = "]/div[@class='clearfix']/div[@class='ohidden']/h2/a[@class='nws_linkhd']"
           
        result=[]        
        
        
        for i in range(2,7):
        
            item = StocknewsItem()
            
            path = title_start+str(i)+title_end
            #item['title'] = response.selector.xpath(path).extract()
            temp = response.selector.xpath(path).extract()
            
            #validity check            
            if len(temp)==0:
                item['title'] = 'empty'
            else:              
                item['title'] = temp
            
            path = intro_start+str(i)+intro_end
            item['intro'] = response.selector.xpath(path).extract()
            
            path = date_start+str(i)+date_end
            item['date'] = response.selector.xpath(path).extract()
            
            path = href_start+str(i)+href_end
            temp = response.selector.xpath(path).extract()
            
            if len(temp)==0:
                item['href'] = 'empty'
            else:              
                item['href'] = "http://www.moneycontrol.com"+temp[0]

            
            result.append(item)
        
        return result

'''

'''
