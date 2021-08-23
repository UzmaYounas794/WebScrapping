import scrapy
from scrapy.http import Request


class SanetSpider(scrapy.Spider):
    name = "sanet"
    page_number = 2
    allowed_domains = [
        "www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results"
    ]
    start_urls = [
        "http://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results/"
    ]
    custom_settings = {"FEED_URI": "tmp/sanet.json"}

    def parse(self, response):
        yield {
            "Names": response.xpath("//h4/a/text()").extract(),
            "Positions": response.xpath("//dl/dd[2]/text()").extract(),
        }

        next_page = (
            "https://www.aph.gov.au/Senators_and_Members/Parliamentarian_Search_Results?page="
            + str(SanetSpider.page_number)
            + "&q=&mem=1&sen=1&par=-1&gen=0&ps=12&st=1"
        )
        if SanetSpider.page_number <= 7:
            SanetSpider.page_number += 1
            yield scrapy.Request(next_page, callback=self.parse)


"""''
        # next_page = response.xpath('//a[@title="Next page"]/@href').get()
        # next_page = response.urljoin(next_page)
        # If next_page have value
        if next_page:

            yield scrapy.Request(url=next_page, callback=self.parse)
""" """"""
