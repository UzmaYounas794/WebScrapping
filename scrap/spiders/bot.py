import scrapy


class BotSpider(scrapy.Spider):
    name = "bot"
    allowed_domains = ["www.shopclues.com/branded-deals.html"]
    start_urls = ["http://www.shopclues.com/branded-deals.html/"]
    custom_settings = {"FEED_URI": "tmp/bot.json"}

    def parse(self, response):

        titles = response.css("img::attr(title)").extract()
        images = response.css("img::attr(data-img)").extract()
        prices = response.css(".p_price::text").extract()
        discounts = response.css(".prd_discount::text").extract()

        for item in zip(titles, prices, images, discounts):
            scraped_info = {
                "title": item[0],
                "price": item[1],
                "image_urls": [item[2]],
                "discount": item[3],
            }

            yield scraped_info
