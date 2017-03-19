from mongoengine import *
import src.word_to_json as WordToJson
from src.section import Section
import json
import datetime

def document_from_file(filepath):
    return Document(sections=__load_sections(filepath))

def __json(filepath):
    return json.loads(WordToJson.transform_to_json(filepath))

def __load_sections(filepath):
    sections = []
    json_document = __json(filepath)
    header_section = None
    for section_document in json_document["document"]["section"]:
        section = Section(type=section_document['type'], content=section_document['content'], position=int(section_document['position']))
        if(section.is_top_header() or section.is_sub_header()):
            header_section = section
            sections.append(header_section)
        elif header_section is None:
            sections.append(section)

        if(section.is_body()):
            header_section.sections.append(section)

    return sorted(sections, key=lambda s: s.position)

class Document(Document):
    sections = ListField(EmbeddedDocumentField(Section))
    date_modified = DateTimeField(default=datetime.datetime.now)

    def header(self):
        return next((section for section in self.sections if section.is_top_header()), None)

    def subheaders(self):
        return list(filter(lambda s: s.is_sub_header(), self.sections))

    def subheader_titles(self):
        return list(map(lambda s: s.content, self.subheaders()))
