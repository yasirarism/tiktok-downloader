import unittest
from .scrapper import info_post
from .snaptik import snaptik
from .ssstik import ssstik
from .tikmate import tikmate
from .mdown import mdown


class TikTok(unittest.TestCase):
    base_url = 'https://www.tiktok.com/@tribunsumselcom/video/7020708969563917595'
    def test_snaptk(self):
        self.assertTrue(snaptik(self.base_url).get_media())

    def test_sstkio(self):
        self.assertTrue(ssstik().get_media(self.base_url))

    def test_info(self):
        self.assertTrue(info_post(self.base_url).js)
    
    def tikmat(self):
        self.assertTrue(tikmate().get_media(self.base_url))
    
    def mdown(self):
        self.assertTrue(mdown().get_media(self.base_url))

if __name__ == '__main__':
    unittest.main()