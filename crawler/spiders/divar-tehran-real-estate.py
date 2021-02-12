import re

import scrapy


class Divar(scrapy.Spider):
    name = 'divar-tehran-real-estate'

    start_urls = [
        'https://api.divar.ir/v8/web-search/tehran/real-estate'
    ]

    key_map = {
        "متراژ": "area",
        "ساخت": "year",
        "اتاق": "room",
        "آژانس املاک": "agency",
        "طبقه": "floor",
        "آسانسور ندارد": "elevator",
        "آسانسور": "elevator",
        "پارکینگ ندارد": "parking",
        "پارکینگ": "parking",
        "انباری ندارد": "storage",
        "انباری": "storage",
        "بالکن ندارد": "balcony",
        "بالکن": "balcony",
    }

    floor_map = {
        "همکف": 0,
        "زیر همکف": -1,
        "زیرهمکف": -1,
    }
    get_number = lambda s: int(re.findall(r'\d+', s.replace("٫", ""))[0])
    same = lambda s: s
    get_room = lambda s, get_number=get_number: 0 if s == "بدون اتاق" else get_number(s)
    get_floor = lambda s, floor_map=floor_map, get_number=get_number: floor_map[s] if s in floor_map else get_number(s)

    value_map = {
        "متراژ": get_number,
        "ساخت": get_number,
        "اتاق": get_room,
        "آژانس املاک": same,
        "طبقه": get_floor,
        "آسانسور ندارد": same,
        "آسانسور": same,
        "پارکینگ ندارد": same,
        "پارکینگ": same,
        "انباری ندارد": same,
        "انباری": same,
        "بالکن ندارد": same,
        "بالکن": same,
    }

    def parse(self, response, **kwargs):
        response = response.json()
        for widget in response['widget_list']:
            yield scrapy.Request(f'https://api.divar.ir/v8/posts/{widget["data"]["token"]}',
                                 callback=self.parse_details)
        if response['last_post_date'] != -1:
            yield scrapy.Request(method='POST', url='https://api.divar.ir/v8/search/1/real-estate',
                                 body='{"json_schema": {"category": {"value": "real-estate"}}, "last-post-date": %s}' %
                                      response['last_post_date'])

    def parse_details(self, response):
        response = response.json()
        item = {
            'district': response['data']['district'],
            'token': response['token'],
            'sub_category': response['widgets']['breadcrumb']['categories'][0]['slug'],
            'category': response['widgets']['breadcrumb']['categories'][1]['slug'],
            'business_type': response['data']['webengage']['business_type'],
            'price': response['data']['webengage']['price'],
            'credit': response['data']['webengage']['credit'],
            'rent': response['data']['webengage']['rent'],
            'title': response['widgets']['header']['title'],
            'location': response['widgets']['location']
        }
        list_data = response['widgets']['list_data']
        for data in list_data:
            if data['format'] == 'group_info_row':
                for i in data['items']:
                    if i['title'] in self.key_map:
                        item[self.key_map[i['title']]] = self.value_map[i['title']](i['value'])
            elif data['format'] == "group_feature_row":
                for i in data['items']:
                    if i['title'] in self.key_map:
                        item[self.key_map[i['title']]] = i['available']
            else:
                if data['title'] in self.key_map:
                    item[self.key_map[data['title']]] = self.value_map[data['title']](data['value'])
        yield item
