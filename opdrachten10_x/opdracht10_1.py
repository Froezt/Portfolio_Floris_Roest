import xmltodict

def processXML(filename):
    with open (filename) as myXMLfile:
        filestring = myXMLfile.read()
        xmldictionary = xmltodict.parse(filestring)
        return xmldictionary
artikelendict = processXML('artikelen.xml')
artikelen = artikelendict ['artikelen']['artikel']
for artikel in artikelen:
    print(artikel['naam'])

