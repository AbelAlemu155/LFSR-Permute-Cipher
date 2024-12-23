import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import numpy as np
from util.key_file_util import read_key_file, write_key_file

from aes_functionalities.aes_encrypt_ecb import AESencrypt_ECB
from util.constants import BLOCK_SIZE, MAX_FILE_NAME_LENGTH


# the key is the np array key 
def encrypt_cbc(input_file_name, encrypted_name, key):
    aes_enc = AESencrypt_ECB(key)
    header, nonce = generate_header(input_file_name)
    # encrypt the nonce
    y =  aes_enc.encrypt_blk(np.frombuffer(nonce, np.uint8, -1 )).tobytes()
        
    with open(input_file_name, 'rb') as input_file, open(encrypted_name, 'wb') as output_file:
        # write the encrypted nonce to the outpufile
        output_file.write(y)
        # encrypt the header write to the output file 
        st= 16
        en= 32
        # read the 80 byte header
        while(en<= 80):
            header_blk =  bytes(a ^ b for a, b in zip(y, header[st: en]))
            header_blk_enc= aes_enc.encrypt_blk(np.frombuffer(header_blk, np.uint8, -1)).tobytes()
            output_file.write(header_blk_enc)
            st=en
            en += 16
            y= header_blk_enc
       
        # handle the payload
        # read 16 bytes (block size bytes) at a time
        chunk = input_file.read(BLOCK_SIZE)
        while chunk:
            # apply padding if necessary
            if len(chunk) < BLOCK_SIZE:
                chunk = pad_block(chunk)
            # take the xor with previous y
            data_block= bytes(a ^ b for a, b in zip(y, chunk))
            # encrypt the xorred value
            data_block_enc = aes_enc.encrypt_blk(np.frombuffer(data_block, np.uint8, -1)).tobytes()
            output_file.write(data_block_enc)
            # update the y for next iteration
            y= data_block_enc
            # Read the next 16 bytes
            chunk = input_file.read(BLOCK_SIZE)
 
    aes_enc.finalize()

    
# generates the 80 bytes header
def generate_header(input_file_name):
    # generate a nonce
    nonce = os.urandom(BLOCK_SIZE)
    # add the nonce to the header
    header = nonce
    # get the number of characters in the input file name
    # ensure its length 1 byte 
    total_characters= len(input_file_name).to_bytes(1)
    # append the total characters to the header
    header += total_characters
    # ensure the file name is stored as 59 bytes adding a null bytes padding
    file_name_characters = input_file_name.encode().ljust(MAX_FILE_NAME_LENGTH, b'\0') 
    # append the file name
    header += file_name_characters
    # get the input file size in bytes
    file_size = os.path.getsize(input_file_name)
    print(f'input file size: {file_size}')
    # convert the file_size into a big endian consituting 4 bytes 
    file_size_bstring = file_size.to_bytes(4, byteorder= 'big')
    # append to the header
    header += file_size_bstring
    return header, nonce

# padding the last byte to ensure multiple of 16 file size
def pad_block(data):
    padding_len = BLOCK_SIZE - len(data) 
    padding = bytes([padding_len] * padding_len)
    return data + padding







     
    