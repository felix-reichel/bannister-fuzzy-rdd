import sys
import os
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# Add the parent directory to the system path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Custom reactor installation
try:
    import custom_reactor

    custom_reactor.install_asyncio_reactor()
except Exception as e:
    print(f"Error installing asyncio reactor: {e}")

from athletics_scraper.athletics_scraper.spiders.athletics import AthleticsSpider


def run_spider():
    process = CrawlerProcess(get_project_settings())
    process.crawl(AthleticsSpider)
    process.start()


if __name__ == "__main__":
    run_spider()
