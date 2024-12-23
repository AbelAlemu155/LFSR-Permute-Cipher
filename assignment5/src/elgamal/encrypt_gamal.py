import base64
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from AES.util.key_file_util import write_key_file
from elgamal.util.generate_random_number import random_integer
from elgamal.util.mod_ex import modExEfficient




# plaint text bstring x
def encrypt_gamal(x, p, alpha, beta, output_file):
    # the binary keys should be b64 encoded
    b64_x = base64.b64encode(x)
    with open(output_file, 'wb') as output:
        for i in range(len(b64_x)):
            byte= b64_x[i]
            # select random integer  b between 1 and p-1 for each byte df
            b= random_integer(1, p-1)
            y1= modExEfficient(alpha, b,p).to_bytes(4, 'big')
            secret = modExEfficient(beta, b, p)
            y2= ((byte * secret) % p).to_bytes(4, 'big')
            output.write(y1)
            output.write(y2)


# use the p and alpha values in the system parameter's parameter certificates
p= 100035179
alpha=  22055634
key = os.urandom(32)
write_key_file(key, 'keys/elgamal_aes.b64')
beta= 81999981


encrypt_gamal(key, p, alpha, beta, 'keys/encrypted_key1.eg' )



    
    
        

