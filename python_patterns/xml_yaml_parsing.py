import xml.etree.ElementTree as ET
import xmltodict
import yaml

"""
ElementTree (ET) is a lightweight Python library for parsing and creating XML documents. 
It represents an XML document as a tree structure, where each element is a node with attributes and text content.

Key Components:
- `ET.parse(file)`: Parses an XML file and returns an ElementTree object.
- `tree.getroot()`: Retrieves the root element of the XML tree.
- `ET.Element(tag)`: Creates a new XML element with the specified tag.
- `ET.SubElement(parent, tag)`: Creates a sub-element inside the specified parent element.
- `tree.write(file)`: Writes the XML tree to a file.

xmltodict is another library for working with XML in a way similar to JSON parsing:
- `xmltodict.parse(xml_string)`: Converts XML to an OrderedDict.
- `xmltodict.unparse(dictionary)`: Converts an OrderedDict back to XML.
"""

# 1. Read XML File using ElementTree
def read_xml(file_path):
    """Reads an XML file and returns the root element."""
    # Parse the XML file and create an ElementTree object
    tree = ET.parse(file_path)
    
    # Get the root element of the XML document
    root = tree.getroot()
    return root

# 2. Write XML File using ElementTree
def write_xml(file_path, root_element, data):
    """Writes an XML file with a given root element and dictionary of key-value pairs."""
    # Create the root element with the specified tag
    root = ET.Element(root_element)
    
    # Iterate through the provided dictionary and create sub-elements
    for key, value in data.items():
        child = ET.SubElement(root, key)  # Create a sub-element with key as tag
        child.text = str(value)  # Set the text content of the sub-element
    
    # Create an ElementTree object with the root
    tree = ET.ElementTree(root)
    
    # Write the XML structure to the specified file
    tree.write(file_path)
    print(f"XML file written: {file_path}")

# 3. Read XML File using xmltodict
def read_xml_dict(file_path):
    """Reads an XML file and converts it into a dictionary using xmltodict."""
    with open(file_path, 'r', encoding='utf-8') as file:
        xml_content = file.read()
        return xmltodict.parse(xml_content)

# 4. Write XML File using xmltodict
def write_xml_dict(file_path, data):
    """Writes a dictionary to an XML file using xmltodict."""
    xml_content = xmltodict.unparse(data, pretty=True)
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(xml_content)
    print(f"XML file written using xmltodict: {file_path}")

# 5. Read YAML File
def read_yaml(file_path):
    """Reads a YAML file and returns its contents as a dictionary."""
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Use yaml.safe_load to safely parse the YAML content into a dictionary
        return yaml.safe_load(file)

# 6. Write YAML File
def write_yaml(file_path, data):
    """Writes a dictionary to a YAML file."""
    # Open the file in write mode
    with open(file_path, 'w') as file:
        # Convert the dictionary into YAML format and write it to the file
        yaml.dump(data, file)
    print(f"YAML file written: {file_path}")

# Example usage (Uncomment to run)
# xml_data = read_xml("example.xml")
# write_xml("output.xml", "Person", {"Name": "Alice", "Age": "30"})
# xml_dict = read_xml_dict("example.xml")
# write_xml_dict("output_dict.xml", {"Person": {"Name": "Alice", "Age": 30}})
# yaml_data = read_yaml("example.yaml")
# write_yaml("output.yaml", {"Name": "Alice", "Age": 30})

