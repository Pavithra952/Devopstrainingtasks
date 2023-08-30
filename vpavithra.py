import xmltodict,json

xml_file_name=input("enter the xml_file name:")

try:

    with open(xml_file_name,'r') as xml_file:

        xml_dict=xmltodict.parse(xml_file.read(),dict_constructor=dict)

        json_data=json.dumps(xml_dict,indent=4)

        print(json_data)

except FileNotFoundError:

    print("file not found")

except xmltodict.expat.ExpatError:

    print("invalid xml format ,please check xml file")
