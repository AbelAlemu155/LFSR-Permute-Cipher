import os
from util.constants import MAX_FILE_NAME_LENGTH
# function for checking the appropriate number of characters in the file name 
def check_length(file_name):
    return not len(file_name) > MAX_FILE_NAME_LENGTH

# checking the above for multiple argument file names 
def check_length_arguments(file_names):
    for file_name in file_names:
        if not check_length(file_name):
            return False
    return True 

# checking for .aes suffix in the encrypted file names 
def check_aes_suffix(file_name):
    return "." in file_name and file_name.split(".")[-1] == 'aes'

def check_file_exists(file_name):
    return os.path.exists(file_name)




