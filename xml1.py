import sys
import xml.etree.ElementTree as etree

def get_attr_number_req(node):
    tmp = len(node.attrib)
    for child in node:
        tmp += get_attr_number_req(child)
    return tmp

def get_attr_number(node):
    return sum([len(elem.attrib) for elem in node.iter()])

if __name__ == '__main__':
    xml = "<feed xml:lang='en'>" + \
    "<title>HackerRank</title>" + \
    "<subtitle lang='en'>Programming challenges</subtitle>" + \
    "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>" + \
    "<updated>2013-12-25T12:00:00</updated>" +\
    "</feed>"
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))