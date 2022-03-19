from scrapy.spiders import Spider, CrawlSpider
from scrapy.exceptions import DropItem
from typing import Union

from pokemon_scrapy.ports import Pipeline, ScrapyEtlItem
from pokemon_scrapy.core.commons.orm import db_session


class PokemonPipeline(Pipeline):
    
    def __init__(self):
        self.session = db_session()
    
    def process_item(self, item: ScrapyEtlItem, spider: Union[Spider, CrawlSpider]):
        try:
            db_item = item.process()
            item.save(db_item, self.session)
            return item
        except Exception as exc:
            raise DropItem(f"error: {exc.__class__.__name__} "
                           f"detail: {str(exc)}")
        