import os
import pathlib
import shutil
import time
from pathlib import Path

def cleaner():
    
    path = "C:\\Users\\namit\\OneDrive\\Desktop\\activity\\projetcs\\folder"
    time.sleep(1)
    list1 = os.listdir(path)
    dirset =set()
    for file in list1:
    
        file_extension = pathlib.Path(path + "\\" + file).suffix[1:]
        if file_extension == '':
            continue
        if file_extension not in dirset:
              dirset.add(file_extension)
              if not os.path.exists(path+"\\"+file_extension+"_folder"):
                   os.mkdir(path+"\\"+file_extension+"_folder")            
        my_file = Path(path+"\\"+file_extension+"_folder"+"\\"+file)  
        if my_file.exists():  
              my_file = check_and_rename(my_file)       
        shutil.move(path + "\\" + file, my_file)
        

def check_and_rename(file_path: Path, add: int = 0) -> Path:
    original_file_path = file_path
    if add != 0:
        file_path = file_path.with_stem(file_path.stem + "_" + str(add))
    if not os.path.isfile(file_path):
        return file_path
    else:
        return check_and_rename(original_file_path, add + 1)

      
