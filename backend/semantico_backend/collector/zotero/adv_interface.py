import json
import logging
import os

from pyzotero import zotero

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)


class ZoteroInterface:
    def __init__(self, conn_type: str):
        # get current path
        current_path = os.getcwd()
        # load configurations
        if conn_type == 'group':
            basic_conf_path = os.path.join(current_path, "configuration/advanced_group.json")
        elif conn_type == 'user':
            basic_conf_path = os.path.join(current_path, "configuration/advanced.json")
        else:
            raise ValueError('Connection type not available yet')

        with open(basic_conf_path) as conf:
            self.conf = json.load(conf)

        self.output_file_path = os.path.join(current_path, self.conf['output_folder'])

        if conn_type == 'group':
            self.zot = zotero.Zotero(self.conf['library_id'], self.conf['library_type'])
        elif conn_type == 'user':
            self.zot = zotero.Zotero(self.conf['library_id'], self.conf['library_type'],
                                     self.conf['api_key'])

    def get_items(self) -> dict:
        items = self.zot.items()
        return items

    def get_top_items(self, count) -> dict:
        tops = self.zot.top(limit=count)
        return tops

    def get_search_items(self, term) -> dict:
        items = self.zot.items(q=term)
        return items

    def get_pdfs(self, term):
        file_paths = list()
        items = self.get_search_items(term)
        for item in items:
            data_key = item['data']['key']
            file_name = data_key + '.pdf'
            if file_name in os.listdir(self.output_file_path):
                file_paths.append(os.path.join(self.output_file_path, file_name))
            else:
                try:
                    self.zot.dump(data_key, file_name, self.conf['output_folder'])
                    file_paths.append(os.path.join(self.output_file_path, file_name))
                except Exception as e:
                    logger.debug(str(e))

        return file_paths
