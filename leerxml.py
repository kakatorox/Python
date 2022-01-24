from typing import Text
from xml.dom.minidom import Node, parse 


xmltree=parse('note.xml')

for nodo in xmltree.getElementsByTagName('pro'):
    for nodo_hijo in nodo.childNodes:
        if nodo_hijo.nodeType == Node.TEXT_NODE:
            print(nodo_hijo.data)

print("sepracion")
import xml.sax
from xml.etree.ElementTree import parse

xml_doc=parse('note.xml')
for ele in xml_doc.findall('pro'):
    print(ele.text)

