import sys

from cbc_module.decrypt_cbc import decrypt_cbc
from cbc_module.encrypt_cbc import encrypt_cbc
from util import display_util
from util.key_file_util import read_key_file
from util.validation import check_aes_suffix, check_length
num_arguments =[3,4]
# invalid number of arguments display error 
if len(sys.argv) not in num_arguments:
    display_util.get_help_message()
    sys.exit(1)
# decrypt the file
if len(sys.argv)==4:
    file_name= sys.argv[1]
    if not check_length(file_name):
        print(f'Input files should contain a maximum of 59 characters')
        sys.exit(0)
    encrypt_to = sys.argv[2]
    if not check_aes_suffix(encrypt_to):
        print(f'Only use .aes extension for files to be encrypted')
        sys.exit(0)
    key_path= sys.argv[3]
    try:
        # read the key for encryption
        key = read_key_file(key_path)
        if(not key[1]):
            print('Problem in provided key fil: key sizes should be exactly 32 bytes')
            sys.exit(0)
        # perform encryption
        
        encrypt_cbc(file_name, encrypt_to, key[0])
        print(f'File encryption successful!')
    except IOError as e:
        print(f'Error in file operations, exiting')
elif len(sys.argv)==3:
    try:
        file_to_decrypt= sys.argv[1]
        key_path= sys.argv[2]
        key = read_key_file(key_path)
        if(not key[1]):
            print('Problem in provided key fil: key sizes should be exactly 32 bytes')
            sys.exit(0)
        
        correct_file_name=decrypt_cbc(file_to_decrypt, key[0])
        print(f'Decryption completed to {correct_file_name}')
    except IOError as e:
        print(e)
        print(f'Error in file operations, exiting')

    

    
    

