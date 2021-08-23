import scrapy


class CrawlerSpider(scrapy.Spider):
    name = "crawler"
    allowed_domains = ["http://cs.qau.edu.pk/faculty.php"]
    start_urls = ["http://cs.qau.edu.pk/faculty.php/"]
    custom_settings = {"FEED_URI": "tmp/crawler.json"}

    def parse(self, response):
        names = response.css(
            "div.container > table > tbody > tr > td > strong > a::text,div.container > table > tbody > tr > td > a > strong::text,div.container > table > tbody > tr > td > strong:nth-child(2)::text"
        ).extract()
        emails = response.css(
            " table > tbody > tr > td > p > a:nth-child(1)::text"
        ).extract()
        contacts = response.css(
            " table > tbody > tr > td > p > a:nth-child(4)::text"
        ).extract()

        for item in zip(names, emails, contacts):
            scraped_info = {
                "Name": item[0],
                "Email": item[1],
                "Contact": item[2],
            }

            yield scraped_info
