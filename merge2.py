# -*- coding:utf-8 -*-


#-----------------------------------------------------
def note_copy(file_name):	#copy notes;
	obj_note_sourse = open(file_name,'r')
	list_lines_in_note = obj_note_sourse.readlines()
	str_lines_in_note = ''.join(list_lines_in_note)
	obj_note_sourse.close()

	return str_lines_in_note
#-----------------------------------------------------
def creat_blank_file():
	obj_file = open("result_note.txt",'w')
	obj_file.write('\n')
	print("Fnished step 2.1: Finished to creat result note now.")
	obj_file.truncate()
	print("Fnished step 2.2: Finished to truncate note now.")
	obj_file.close()
#----------------------------------------------------
def result_write(file_name):	#get result file;
	obj_note_result = open("result_note.txt",'a')
	obj_note_result.write('\n' + note_copy(file_name))
	obj_note_result.close()
#--------------------------------------------------------------
def merge_files():
    obj_note_contents = open("all_files_path.txt",'r')
    list_lines_in_contents = obj_note_contents.readlines()
    num_of_file = 0
    
    for str_line in list_lines_in_contents:
        str_line_modify = str_line[:-1]
        num_of_file = num_of_file+1
        try:
            result_write(str_line_modify)
        except UnicodeDecodeError:
            #print(num_of_file)
            #print(str_line_modify)
            pass
        else:
            continue

    obj_note_contents.close()



def main_2():
        creat_blank_file()
        merge_files()
        print("Fnished step 2.3: Finished to merge the files.")
