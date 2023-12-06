import json
import os

from pyzotero import zotero


class ZoteroInterface:
    def __init__(self, type: str):
        # get current path
        current_path = os.getcwd()
        # load configurations
        if type == 'group':
            basic_conf_path = os.path.join(current_path, "configuration/advanced_group.json")
        elif type == 'user':
            basic_conf_path = os.path.join(current_path, "configuration/advanced.json")
        with open(basic_conf_path) as conf:
            self.conf = json.load(conf)
        if type == 'group':
            self.zot = zotero.Zotero(self.conf['library_id'], self.conf['library_type'])
        elif type == 'user':
            self.zot = zotero.Zotero(self.conf['library_id'], self.conf['library_type'],
                                     self.conf['api_key'])

    def get_items(self) -> dict():
        items = self.zot.items()
        return items

    def get_top_items(self, count) -> dict():
        tops = self.zot.top(limit=count)
        return tops

    def get_search_items(self, term) -> dict():
        items = self.zot.items(q=term)
        return items
