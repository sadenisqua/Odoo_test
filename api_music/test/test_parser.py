import json

import xmltodict
from lxml import etree, objectify
import xml.dom.minidom
import xml.etree.ElementTree as ET
import pprint as pp


def parseXML(xmlFile):
    """
    Parse the xml
    """
    with open(xmlFile, 'r') as r:
        read_xml = r.read()

    root = objectify.fromstring(read_xml)

    # возвращает атрибуты в узле элемента как dict
    attrib = root.attrib

    # как извлечь данные элемента
    artist = root.Artists.artist

    for art in root.getchildren():
        for e in art.getchildren():
            print(f'{e.tag} => {e.text}')
        print()

    # как изменить текст элемента
    # root.Artists.artist = 'something else'
    # print(root.Artists.artist)

    # как добавить новый элемент
    # root.Artists.new_element = "new data"

    # удалить материал py: pytype stuff
    # objectify.deannotate(root)
    # etree.cleanup_namespaces(root)
    # obj_xml = etree.tostring(root, pretty_print=True)
    # print(obj_xml)


# parseXML('test.xml')


def parseXml2(fileXML):
    fileXML = xml.dom.minidom.parse(fileXML)

    print(fileXML.nodeName)
    print(fileXML.firstChild.tagName)

    name = fileXML.getElementsByTagName("name")
    print(f"{name.length} expertise")
    for skill in name:
        print(skill.getAttribute("name"))


# parseXml2('test.xml')




def get_xml():
    with open("/home/user/Moduli/api_music/test/test.xml", "rb") as file:
        result = xmltodict.parse(file)
        print(json.dumps(result))
        artists_names = list(map(lambda artists: artists['name'], result['music']['Artists']['artist']))
        artists_names_in_groups = []
        for group in result['music']['Groups']['group']:
            for artist in group['artists']['artist']:
                artists_names_in_groups.append(artist['name'])
        print(artists_names + artists_names_in_groups)


get_xml()
