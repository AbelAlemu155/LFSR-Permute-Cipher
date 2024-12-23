# TODO handling header error
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# get validated inputs
# from  aes_functionalities.aes_decrypt_ecb import AESdecrypt_ECB
from aes_functionalities.aes_decrypt_ecb import AESdecrypt_ECB
from util.key_file_util import read_key_file
from util.validation import check_file_exists
from util.constants import BLOCK_SIZE
import numpy as np
# key file should np uint8 array 
def decrypt_cbc(encrypted_name, key):
    aes_dec = AESdecrypt_ECB(key)
    with open(encrypted_name, 'rb') as input_file:
        # initialize header data 
        total_name_length =0
        binary_file_name = b'' 
        file_size= 0
        correct_file_name= ''
        output_file_object = None 
        
        chunk = input_file.read(16)
        # number of 16 bytes block read including the header
        num_read_blocks= 1
        # number of 16 bytes block read without the header
        num_read_payload_block=0
        y= chunk
        
        while(chunk):
            chunk = input_file.read(16)
            num_read_blocks +=1 
            chunk_dec =  aes_dec.decrypt_blk(np.frombuffer(chunk, np.uint8, -1))
            x =  bytes(a ^ b for a, b in zip(y, chunk_dec))
            y= chunk 
            # handle header
            if(num_read_blocks <= 5):
                if(num_read_blocks == 2):
                    total_name_length= x[0]
                    # python handles over-indexing in slicing 
                    binary_file_name += x[1: total_name_length + 1]
                elif len(binary_file_name) < total_name_length:
                    length_to_append = total_name_length - len(binary_file_name)
                    # python handles over-indexing in slicing 
                    binary_file_name+= x[:length_to_append]
                if num_read_blocks==5:
                    # read the last 4 bytes of the header to get the size
                    file_size= int.from_bytes(x[-4:], byteorder='big')
                    # decode the binary_file_name to utf
                    correct_file_name = binary_file_name.decode('utf-8')

                    

            # handle payload 
            else:
                num_read_payload_block+=1
                if(num_read_payload_block==1):
                    # instantiate an output file object using the correct file name
                   
                    # append x_ if the file exists 
                    while os.path.exists(correct_file_name):
                        parts = correct_file_name.rsplit('/', 1)  # Split / files in the path entries
                        previous_part = parts[0]  # take the first part forming the path of the file
                        new_part = parts[1]  
                        correct_file_name = previous_part+ '/'+ 'x_'  + new_part
                     # create the file since it doesn't exist       
                    output_file_object= open(correct_file_name, 'xb')
                if(num_read_payload_block <= (file_size // 16)):
                    output_file_object.write(x)
                else :
                    # handle padded data for the last block
                    remaining_bytes = file_size % 16
                    output_file_object.write(x[:remaining_bytes])
    
     
    # close used resource   
    aes_dec.finalize( )
    output_file_object.close()
    return correct_file_name
    





        

    