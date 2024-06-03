import scrapy


class OneMileSpider(scrapy.Spider):
    name = "one_mile_spider"
    allowed_domains = ["worldathletics.org"]
    start_urls = [
        f'https://worldathletics.org/records/all-time-toplists/middlelong/one-mile/all/men/senior?regionType=world&page={page}&bestResultsOnly=false&firstDay=1900-01-01&lastDay=2024-06-03&maxResultsByCountry=all&eventId=10229503&ageCategory=senior'
        for page in range(1, 24)
    ]

    bannister_one_mile = 4.00
    limit = 3.56

    def parse(self, response):
        rows = response.xpath('//table[@class="records-table"]/tbody/tr')
        for row in rows:
            yield {
                'rank': row.xpath('td[1]/text()').get(),
                'mark': row.xpath('td[2]/text()').get(),
                'competitor': row.xpath('td[4]/text()').get(),
                'dob': row.xpath('td[5]/text()').get(),
                'nat': row.xpath('td[6]/text()').get(),
                'pos': row.xpath('td[7]/text()').get(),
                'venue': row.xpath('td[9]/text()').get(),
                'date': row.xpath('td[10]/text()').get(),
                'result_score': row.xpath('td[11]/text()').get(),
            }
