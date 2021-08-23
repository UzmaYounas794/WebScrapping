import scrapy


class WebsitebotSpider(scrapy.Spider):
    name = "websitebot"
    allowed_domains = ["https://en.wikipedia.org/wiki/List_of_most_popular_websites"]
    start_urls = ["https://en.wikipedia.org/wiki/List_of_most_popular_websites"]
    custom_settings = {"FEED_URI": "tmp/web.json"}

    def parse(self, response):
        Site = response.css(
            "div.mw-parser-output > table > tbody > tr > td:nth-child(1) > a::text"
        ).extract()
        Domain = response.css(
            "div.mw-parser-output > table > tbody > tr > td:nth-child(2)::text"
        ).extract()
        Function = response.css(
            "div.mw-parser-output > table > tbody > tr > td:nth-child(4)::text"
        ).extract()
        Country = response.css(
            "div.mw-parser-output > table > tbody > tr > td:nth-child(5) > span > a::text"
        ).extract()

        for item in zip(Site, Domain, Function, Country):
            scraped_info = {
                "Site": item[0],
                "Domain": item[1],
                "Function": item[2],
                "Country": item[3],
            }

            yield scraped_info
        """'
        #Using Xpath selector
        Site = response.xpath("//table/tbody/tr/td[1]/a/text()").extract()
        Domain = response.xpath("//table/tbody/tr/td[2]/text()").extract()
        Function = response.xpath("//table/tbody/tr/td[4]/text()").extract()
        Country = response.xpath("//table/tbody/tr/td[5]/span/a/text()").extract()
       """ ""
