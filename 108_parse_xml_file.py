# Parse XML File Example
import xml.etree.ElementTree as ET

# Create a sample XML string
xml_data = '''<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
    </country>
</data>'''

if __name__ == "__main__":
    root = ET.fromstring(xml_data)
    for country in root.findall('country'):
        name = country.get('name')
        rank = country.find('rank').text
        print(f"Country: {name}, Rank: {rank}")
