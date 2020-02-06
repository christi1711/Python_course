import xml.etree.ElementTree as ET
import re
import argparse

def ArgumentParser() :
    parser = argparse.ArgumentParser(descr='This is a program for reading data from xml file')
    parser.add_argument('-path_xml', '-xml', help='Type path to xml file including file name')
    global args
    args = parser.parse_args()

def RetrieveGovernments() :
    governments = set()
    try :
        with open(args.path_xml, 'r') as xml_file :
            xml_data = xml_file.read()
            xml_data = ET.fromstring(xml_data)
            countries = xml_data.findall('country')

            for country in countries :
                governments.add(country.get('government').strip())

        governments_str = re.sub("['{}]", "", str(governments))
        print(governments_str)
    except :
        print("You have a problem. Check the path and file name.")

if __name__ == '__main__' :
    ArgumentParser()
    RetrieveGovernments()
