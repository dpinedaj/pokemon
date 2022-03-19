from scrapy.item import Field
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst


from sqlalchemy.orm import Session
from sqlalchemy import Column, VARCHAR, INTEGER

import logging

from pokemon_scrapy.ports import DeclarativeBase, ScrapyEtlItem
from pokemon_scrapy.core.exceptions import PokemonException
from pokemon_scrapy.core.enums import XpathsEnum


        
class PokemonDB(DeclarativeBase):
    __tablename__ = 'pokemon'
    id = Column('id', INTEGER, primary_key=True, autoincrement=True)
    name = Column('name', VARCHAR, nullable=False)


class PokemonItem(ScrapyEtlItem):
    name = Field(output_processor=TakeFirst())
    

    def process(self):
        logging.info("Processing pokemon Item to DB")
        db_item = PokemonDB(**self)
        return db_item
        
    def save(self, db_item: PokemonDB, session: Session):
        logging.info("Saving PokemonDB")
        try:
            session.add(db_item)
            session.commit()
        except Exception as ex:
            session.rollback()
            raise PokemonException(f"error: {ex.__class__.__name__} "
                                   f"detail: {str(ex)}")
    
def load_pokemon_item(selector: Selector) -> PokemonItem:
    logging.info("Loading Pokemon Item")
    item = ItemLoader(PokemonItem(), selector)
    item.add_xpath('name', XpathsEnum.NAME_XPATH.value)
    return item.load_item()