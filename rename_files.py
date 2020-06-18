# Pythono3 code to rename multiple  
# files in a directory or folder 
  
# importing os module 
import os
from shutil import copyfile

  
# Function to rename multiple files 
def main(): 

    start = 215
    src_folder = 'new/'
    dst_folder = '0_raw/'
    file_format = '.jpg'
  
    for filename in os.listdir(src_folder):
        src = src_folder + filename 
        dst = dst_folder + f'{start:05d}' + file_format
        
        # os.rename(src, dst)
        copyfile(src, dst)
        start += 1
  
# Driver Code 
if __name__ == '__main__': 
      
    # Calling main() function 
    main() 