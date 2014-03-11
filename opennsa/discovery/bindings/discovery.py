## Generated by pyxsdgen

from xml.etree import ElementTree as ET

# types

class InterfaceType(object):
    def __init__(self, type_, href, describedBy):
        self.type_ = type_  # string
        self.href = href  # anyURI
        self.describedBy = describedBy  # anyURI

    @classmethod
    def build(self, element):
        return InterfaceType(
                element.findtext('type'),
                element.findtext('href'),
                element.findtext('describedBy') if element.find('describedBy') is not None else None
               )

    def xml(self, elementName):
        r = ET.Element(elementName)
        ET.SubElement(r, 'type').text = self.type_
        ET.SubElement(r, 'href').text = str(self.href)
        if self.describedBy is not None:
            ET.SubElement(r, 'describedBy').text = str(self.describedBy)
        return r


class NsaType(object):
    def __init__(self, id_, version, expires, name, softwareVersion, startTime, networkId, interface, feature, peersWith, other):
        self.id_ = id_  # anyURI
        self.version = version  # dateTime
        self.expires = expires  # dateTime
        self.name = name  # string
        self.softwareVersion = softwareVersion  # string
        self.startTime = startTime  # dateTime
        self.networkId = networkId  # [ anyURI ]
        self.interface = interface  # [ InterfaceType ]
        self.feature = feature  # [ FeatureType ]
        self.peersWith = peersWith  # [ anyURI ]
        self.other = other  # [ HolderType ]

    @classmethod
    def build(self, element):
        return NsaType(
                element.get('id'),
                element.get('version'),
                element.get('expires'),
                element.findtext('name') if element.find('name') is not None else None,
                element.findtext('softwareVersion') if element.find('softwareVersion') is not None else None,
                element.findtext('startTime') if element.find('startTime') is not None else None,
                [ e.text for e in element.findall('networkId') ] if element.find('networkId') is not None else [],
                [ InterfaceType.build(e) for e in element.findall('interface') ] if element.find('interface') is not None else None,
                [ FeatureType.build(e) for e in element.findall('feature') ] if element.find('feature') is not None else None,
                element.findtext('peersWith') if element.find('peersWith') is not None else None,
                [ HolderType.build(e) for e in element.findall('other') ] if element.find('other') is not None else None
               )

    def xml(self, elementName):
        r = ET.Element(elementName, attrib={'id' : str(self.id_), 'version' : str(self.version)})
        if self.name is not None:
            ET.SubElement(r, 'name').text = self.name
        if self.softwareVersion is not None:
            ET.SubElement(r, 'softwareVersion').text = self.softwareVersion
        if self.startTime is not None:
            ET.SubElement(r, 'startTime').text = str(self.startTime)
        if self.networkId is not None:
            for el in self.networkId:
                ET.SubElement(r, 'networkId').text = str(el)
        if self.interface is not None:
            for el in self.interface:
                ET.SubElement(r, 'interface').extend( el.xml('interface') )
        if self.feature is not None:
            for el in self.feature:
                r.append( el.xml('feature') )
        if self.peersWith is not None:
            for el in self.peersWith:
                ET.SubElement(r, 'peersWith').text = str(el)
        if self.other is not None:
            r.append( self.other.xml('other') )
        return r


class FeatureType(object):
    def __init__(self, type_, value):
        self.type_ = type_
        self.value = value

    @classmethod
    def build(self, element):
        return FeatureType(
                element.get('type'),
                element.text
               )

    def xml(self, elementName):
        r = ET.Element(elementName, attrib={'type':self.type_})
        r.text = self.value
        return r


class HolderType(object):
    def __init__(self, topologyReachability):
        self.topologyReachability = topologyReachability # [ Topology ]


    @classmethod
    def build(self, element):
        return HolderType(
                [ Topology.build(e) for e in element.find(str(topology_reachability)) ] if element.find(str(topology_reachability)) is not None else None
               )

    def xml(self, elementName):
        r = ET.Element(elementName)
        if self.topologyReachability:
            e = ET.SubElement(r, topology_reachability)
            for t in self.topologyReachability:
                e.append( t.xml(nml_topology) )
        return r



# Created manually
class Topology:

    def __init__(self, uri, cost):
        self.uri = uri   # string
        self.cost = cost # int


    @classmethod
    def build(self, element):
        return Topology(
                element.attrib.get('id'),
                int( element.attrib.get('cost') )
               )

    def xml(self, elementName):
        r = ET.Element(elementName, attrib={'id':self.uri, 'cost':str(self.cost) } )
        return r



NSI_DISCOVERY_NS = 'http://schemas.ogf.org/nsi/2014/02/discovery/nsa'
GNS_NS  = 'http://nordu.net/namespaces/2013/12/gnsbod'
NML_NS = 'http://schemas.ogf.org/nml/2013/05/base#'

nsa = ET.QName(NSI_DISCOVERY_NS, 'nsa')
topology_reachability = ET.QName('{%s}TopologyReachability' % GNS_NS)
nml_topology = ET.QName('{%s}Topology'   % NML_NS)



def parse(input_):

    root = ET.fromstring(input_)

    return parseElement(root)


def parseElement(element):

    type_map = {
        '{%s}nsa' % NSI_DISCOVERY_NS : NsaType
    }

    if not element.tag in type_map:
        raise ValueError('No type mapping for tag %s' % element.tag)

    type_ = type_map[element.tag]
    return type_.build(element)
