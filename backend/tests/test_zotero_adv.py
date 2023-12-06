import os
import json
import unittest

from semantico_backend.collector.zotero.adv_interface import ZoteroInterface


class TestZotero(unittest.TestCase):
    def test_interface_item(self):
        """
        Test that the interface is getting items
        """
        # get current path
        current_path = os.getcwd()
        # load configurations
        basic_conf_path = os.path.join(current_path, "configuration/advanced_group.json")
        with open(basic_conf_path) as conf:
            self.conf = json.load(conf)

        # set app configurations
        self.output_file_path = self.conf['output_file']
        self.top_count = self.conf['top_count']

        # instantiation
        z = ZoteroInterface('user')

        # search
        items = z.get_search_items('Sowa')
        # items = z.get_items()
        # tops = z.get_top_items(count=self.top_count)

        for item in items:
            key = item['key']
            data_key = item['data']['key']
            local_json_file_name = os.path.join(self.output_file_path, key + '.json')
            with open(local_json_file_name, 'w') as fjson:
                fjson.write(json.dumps(item))
            local_pdf_file_name = os.path.join(self.output_file_path, key + '.pdf')
            try:
                file = z.zot.file(data_key)
                with open(local_pdf_file_name, 'wb') as f:
                    f.write(file)
            except Exception as e:
                print(str(e))
        self.assertLess(self.top_count, len(items), 'not enough/too much items')


if __name__ == '__main__':
    unittest.main()
