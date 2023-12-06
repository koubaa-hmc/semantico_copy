import unittest

from semantico_backend.collector.zotero.api_interface import ZoteroInterface


class TestZotero(unittest.TestCase):
    def test_interface_collection(self):
        """
        Test that the interface is getting collections
        """
        z = ZoteroInterface()
        result = z.get_collections(ident='10358870')  # 10358870 is me

    def test_interface_item(self):
        """
        Test that the interface is getting items
        """
        z = ZoteroInterface()
        result = z.get_items(ident='10358870')  # 10358870 is me

    def test_interface_item_key(self):
        """
        Test that the interface is getting an item per key
        """
        z = ZoteroInterface()
        result = z.get_items(ident='10358870', item_key='8BLXLF3F')

    def test_interface_item_key_children(self):
        """
        Test that the interface is getting an items children per key
        """
        z = ZoteroInterface()
        result = z.get_items(ident='10358870', item_key='8BLXLF3F', children=True)

    def test_get_pdf(self):
        z = ZoteroInterface()
        result = z.get_link_to_pdf(ident='10358870', item_key='8BLXLF3F')


if __name__ == '__main__':
    unittest.main()
