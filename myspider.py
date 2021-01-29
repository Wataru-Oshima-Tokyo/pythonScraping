import scrapy


class BlogSpider(scrapy.Spider):
    name ='blogspider'
    start_urls = ['https://blog.scrapinghub.com'] #the list it starts scraping
    def parse(self, response):
        """
            extract all the titles from the page, pursue the the link connected to the next page if exists
        """
        # extrac all the titles from the page
        for title in response.css('.post-header>h2'):
            yield {'title': title.css('a ::text').get()}


        #piursue the link connected to the next page if exists
        for next_page in response.css('a.next-posts-link'):
            yield response.follow(next_page, self.parse)
