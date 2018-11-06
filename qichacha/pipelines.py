# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


from scrapy.exceptions import DropItem

from qichacha.model import QccModel, get_sqlsession, engine, create_newtable


class QichachaPipeline(object):
    def __init__(self):
        self.session = get_sqlsession(engine)
        create_newtable(engine)

    def close_spider(self, spider):
        self.session.close()

    def process_item(self, item, spider):
        _item = QccModel.db_distinct(self.session, QccModel, item, item['url'])
        QccModel.save_mode(self.session, QccModel(), _item)

        return item



