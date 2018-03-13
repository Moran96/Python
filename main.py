#coding=utf-8

import re
import collections
import os
import find_document
import merge2

def count_word(path):
    result = {}
    with open(path) as file_obj:
        all_the_text = file_obj.read()
        #大写转小写
        all_the_text = all_the_text.lower()
        #正则表达式替换特殊字符
        all_the_text = re.sub("\"|,|\.", "", all_the_text)
        
        for word in all_the_text.split():
            if word not in result:
                result[word] = 0
            result[word] += 1 
            
        return result

def sort_by_count(d):
    #字典排序
    d = collections.OrderedDict(sorted(d.items(), key = lambda t: -t[1]))
    return d

def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i) #
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

if __name__ == '__main__':
    file_name = "result_note.txt"

    if find_document.main_1() == False:
        print("Failure to make target file!!!!!!!!")
    else:
        merge2.main_2()
        
        dword = count_word(file_name)
        dword = sort_by_count(dword)
    
        obj_files = open("result.txt","w+")

        for key,value in dword.items():
            #print (key + ":%d" % value)
            obj_files.write(key)
            obj_files.write("\t"+"\t")
            obj_files.write(":%d" % value)
            obj_files.write("\n")

        obj_files.close()

        os.remove('all_files_path.txt')
        os.remove('result_note.txt')
        del_path = (os.getcwd() + '/__pycache__')
        del_file(del_path)
        os.rmdir(del_path)

        print("Fnished step 3.0: Finished to statistic.")
