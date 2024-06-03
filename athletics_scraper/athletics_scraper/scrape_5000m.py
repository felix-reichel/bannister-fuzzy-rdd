from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

from athletics_scraper.athletics_scraper.spiders.FiveThousandMetresSpider import FiveThousandMetresSpider


def run_spider():
    settings = get_project_settings()
    settings.set('FEEDS', {
        'world_athletics_5000m_men_results.csv': {
            'format': 'csv',
            'encoding': 'utf8',
            'store_empty': False,
            'fields': ['rank', 'mark', 'competitor', 'dob', 'nat', 'pos', 'venue', 'date', 'result_score'],
            'overwrite': True,
        },
    })

    process = CrawlerProcess(settings)
    process.crawl(FiveThousandMetresSpider)
    process.start()


if __name__ == "__main__":
    run_spider()
