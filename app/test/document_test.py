import unittest
from src.document import Document
from src.document import document_from_file
import os

class DocumentTest(unittest.TestCase):
    def test_should_load_the_document_from_file(self):
        filepath = os.path.join(os.path.dirname(__file__), '../word-test-doc.xml')
        document = document_from_file(filepath)
        self.assertEqual(len(document.sections), 4)

    def test_should_return_header(self):
        filepath = os.path.join(os.path.dirname(__file__), '../word-test-doc.xml')
        document = document_from_file(filepath)
        self.assertEqual(document.header().content, 'Lorem Ipsum')

    def test_should_return_subheader_titles(self):
        filepath = os.path.join(os.path.dirname(__file__), '../word-test-doc.xml')
        document = document_from_file(filepath)
        self.assertEqual(document.subheader_titles(), ['Where does it come from?', 'Why do we use it?', 'Where can I get some?'])

    def test_should_return_subheader_sections_with_bodies(self):
        filepath = os.path.join(os.path.dirname(__file__), '../word-test-doc.xml')
        document = document_from_file(filepath)
        body_sections = list(map((lambda s: s.sections), document.subheaders()))
        self.assertEqual(len(body_sections), 3)


if __name__ == '__main__':
    unittest.main()
