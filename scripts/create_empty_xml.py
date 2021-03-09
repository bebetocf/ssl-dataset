# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os
from shutil import copyfile

  
# Function to rename multiple files 
def main(): 

    start = 817
    end = 820
    src_folder = 'detection/'


    for i in range(start, end + 1):
        txt = f'<annotation>\n\t\
<folder>frames</folder>\n\t\
<filename>{i:05d}.jpg</filename>\n\t\
<path>/home/roberto/Documents/msc/msc-project/yolo_v4/ssl-dataset/1_resized/{i:05d}.jpg</path>\n\t\
<source>\n\t\t\
<database>Unknown</database>\n\t\
</source>\n\t\
<size>\n\t\t\
<width>224</width>\n\t\t\
<height>224</height>\n\t\t\
<depth>3</depth>\n\t\
</size>\n\t\
<segmented>0</segmented>\n\
</annotation>'
        f = open(src_folder + f'{i:05d}' + '.xml', "w")
        f.write(txt)
        f.close()
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 
