import json
import os
import requests
from requests import Response
import logging


class ZoteroInterface:
    def __init__(self):
        # get current path
        current_path = os.getcwd()
        # set configurations and headers path
        basic_conf_path = os.path.join(current_path, "configuration/basic.json")
        header_path = os.path.join(current_path, "configuration/header.json")

        # set logger configurations
        logging.basicConfig()
        logging.getLogger().setLevel(logging.DEBUG)
        req_log = logging.getLogger('requests.packages.urllib3')
        req_log.setLevel(logging.DEBUG)
        req_log.propagate = True

        # read headers and configurations
        with open(header_path) as head:
            self.header = json.load(head)
        with open(basic_conf_path) as conf:
            self.conf = json.load(conf)

        # set app configurations
        self.base_url = self.conf['base_url']
        self.output_file_path = self.conf['output_file']

    # items
    def get_items(self, ident: str, group=False, item_key=None, children=False,
                  top=False, trash=False,
                  res_format=json) -> Response:
        user_group_prefix = self._build_user_group_prefix(group, ident)
        request = self._build_item_request(item_key, children, top)

        request_url = self.base_url + user_group_prefix + request
        response = requests.get(request_url, headers=self.header)
        with open(self.output_file_path, 'w') as data:
            data.write('\n')
            data.write(str(response.text))
        return response

    def get_link_to_pdf(self, ident: str, item_key):
        items = json.loads(self.get_items(ident=ident, group=False, item_key=item_key).text)
        for item in items:
            print(f"Item type: {item['data']['itemType']}")

    # collections
    def get_collections(self, ident: str, group=False, collection_key=None, sub_collections=False,
                        top=False,
                        res_format=json) -> Response:
        user_group_prefix = self._build_user_group_prefix(group, ident)
        request = self._build_coll_request(collection_key, sub_collections, top)

        request_url = self.base_url + user_group_prefix + request
        response = requests.get(request_url, headers=self.header)
        with open(self.output_file_path, 'w') as data:
            data.write('\n')
            data.write(str(response.text))
        return response

    @staticmethod
    def _build_user_group_prefix(group, ident) -> str:
        if group:
            return '/groups/' + ident
        else:
            return '/users/' + ident

    @staticmethod
    def _build_coll_request(collection_key, sub_collections, top) -> str:
        request = '/collections'
        if collection_key is not None:
            request = request + '/' + collection_key
        if sub_collections:
            request = request + '/collections'
        if top:
            request = request + '/top'
        return request

    @staticmethod
    def _build_item_request(item_key, children, top) -> str:
        request = '/items'
        if item_key is not None:
            request = request + '/' + item_key
        if children:
            request = request + '/children'
        if top:
            request = request + '/top'
        return request

