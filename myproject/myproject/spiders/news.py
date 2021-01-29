import scrapy


class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    def parse(self, response):
        """
             show the extracted links for each topic from the list of topics on the top page
        """
        for url in response.css('ul.topicsList_main a::attr("href")').re(r'/pickup/\d+$'):
            yeild response.follow(url, self.parse_topics)

    def parse_topics(self, response):
        pass
        
