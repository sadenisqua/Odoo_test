from xml.etree import ElementTree as ET


def parseXML(xmlFile):
    """
    Parse the xml
    """
    with open(xmlFile, 'r') as r:
        xml = r.read()

    xml = ET.SubElement('name')
    print(xml)
