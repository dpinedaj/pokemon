from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from pokemon_scrapy.core.models.pokemon import load_pokemon_item
from pokemon_scrapy.core.enums import XpathsEnum


class PokemonSpider(CrawlSpider):
    name = 'pokemon_spider'
    start_urls = [
        "https://www.wikidex.net/wiki/Lista_de_Pok%C3%A9mon_de_la_primera_generaci%C3%B3n"]

    rules = (
        Rule(LinkExtractor(
            allow=[r'.*', ],
            restrict_xpaths=[XpathsEnum.POKEMON_URLS_XPATH.value]),
            callback='parse_item',
            follow=True),
        
    )

    def parse_item(self, response):
        pokemon_item = load_pokemon_item(response)
        yield pokemon_item
