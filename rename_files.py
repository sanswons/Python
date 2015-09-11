import os;

def rename_files():
    # get the file names
    file_list=os.listdir(r"F:\sanjana\books\CSE\python\Programs\prank\prank")
    print(file_list)
    saved_path=os.getcwd()
    os.chdir(r"F:\sanjana\books\CSE\python\Programs\prank\prank")
    
    # rename the files
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
        print(file_name)
    os.chdir(saved_path) 
rename_files()
