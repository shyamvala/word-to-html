from mongoengine import *
import datetime

SECTION_TYPES={
    'top_header': ['heading1'],
    'sub_header': ['heading2', 'heading3'],
    'body': ['normalweb', 'heading4', 'heading5']
}
class Section(EmbeddedDocument):
    type = StringField(max_length=20, required=True)
    content = StringField(required=True)
    position = IntField(required=True)
    sections = ListField(EmbeddedDocumentField("self"))
    date_modified = DateTimeField(default=datetime.datetime.now)

    def is_of_type(self, type):
        matched_type = { key: values for key, values in SECTION_TYPES.items() if self.type.lower() in values }
        return matched_type != None and type in matched_type

    def is_top_header(self):
        return self.is_of_type('top_header')

    def is_sub_header(self):
        return self.is_of_type('sub_header')

    def is_body(self):
        return self.is_of_type('body')
