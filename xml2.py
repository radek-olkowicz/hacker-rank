import sys
import xml.etree.ElementTree as etree


def maxdepth(elem, level):
    tmp_arr = [maxdepth(child, level+1) for child in elem]
    if len(tmp_arr) > 0:
        return max(tmp_arr)
    else:
        return level

if __name__ == '__main__':
    xml = "<feed xml:lang='en'>" + \
    "<title>HackerRank</title>" + \
    "<subtitle lang='en'>Programming challenges<dup>aaa<aa>dffdfdfd</aa></dup></subtitle>" + \
    "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>" + \
    "<updated><ZZ>xx</ZZ>2013-12-25T12:00:00</updated>" +\
    "</feed>"
    tree = etree.ElementTree(etree.fromstring(xml))
    
    print(maxdepth(tree.getroot(), 0))