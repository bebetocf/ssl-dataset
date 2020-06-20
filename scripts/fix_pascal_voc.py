import os
import xml.etree.ElementTree as ET


def main(): 

    folder = '../annotation/pascal_voc/'
  
    for filename in os.listdir(folder):
        src_file = folder + filename
        tree = ET.parse(src_file)
        root = tree.getroot()

        for child in root.findall("path"):
            path_val = child.text.split('/')[-2:]
            child.text = '../../' + path_val[0] + '/' + path_val[1]

        tree.write(src_file)
        
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 