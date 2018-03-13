# -*- coding: utf-8 -*-

import os

#-----------------------------------------------------
def traverse(f):
    
    fs = os.listdir(f)
    
    all_files_path = open("all_files_path.txt","w+") 
    for f1 in fs:  
        tmp_path = os.path.join(f,f1) 
        if not os.path.isdir(tmp_path):  
            #print('文件: %s'%tmp_path)
            if '.txt' in str(tmp_path):
                all_files_path.write('%s'%tmp_path +"\n")
            else:
                pass
        else:  
            #print('文件夹：%s'%tmp_path)
            #all_files_path.write('%s'%tmp_path +"\n")
            traverse(tmp_path)
    all_files_path.close()

#------------------------------------------------------
def main_1():
    path = input("Enter the file path:");

    try:
        traverse(path)
    except FileNotFoundError:
        print("File path not found!")
        return False
    else:
        print("Fnished step 1.1: Finished to traverse the folder slected.")
        print("Fnished step 1.2: Finished to sift the '.txt' files.")
        return True
#------------------------------------------------------
