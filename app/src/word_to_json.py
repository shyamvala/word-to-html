import os
import lxml.etree as ET
import json, xmltodict

def transform_to_json(xml_filename):
    xml_data = ET.parse(xml_filename)
    xsl_filename = os.path.join(os.path.dirname(__file__), "simplify_word_document.xslt")
    xslt = ET.parse(xsl_filename)
    transform = ET.XSLT(xslt)
    simplified_xml_document = transform(xml_data)
    return json.dumps(xmltodict.parse(ET.tostring(simplified_xml_document)))
