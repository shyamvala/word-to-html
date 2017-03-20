import unittest
from src.section import Section

class SectionTest(unittest.TestCase):
    def test_should_be_of_top_header_type(self):
        section = Section(type='Heading1', content="", position=1)
        self.assertTrue(section.is_top_header())

    def test_should_be_of_sub_header_type(self):
        for header in ['Heading2', 'Heading3']:
            section = Section(type=header, content="", position=1)
            self.assertTrue(section.is_sub_header())

    def test_should_be_of_body_type(self):
        for header in ['Heading4', 'Heading5', 'NormalWeb']:
            section = Section(type=header, content="", position=1)
            self.assertTrue(section.is_body())

