from enum import Enum

class XpathsEnum(Enum):
    POKEMON_URLS_XPATH = './/table[contains(@class,"tabpokemon")]//td[3]'
    NAME_XPATH = './/div[@id="nombrepokemon"]/text()'
    