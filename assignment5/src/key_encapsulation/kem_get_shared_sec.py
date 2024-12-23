

import binascii
import sys, oqs, base64
from kem_util import kemalg, validate_cipher_text


if(len(sys.argv) !=4):
    print('Provide correct arguments as shown below')
    print('python3 kem_get_shared_sec.py {key_sec.b64} {ciphertxt.b64} {shared_sec.b64}}')
    sys.exit(0)


# get the shared secret on the client side 
# the client object needs to be reinstantiated using the client secret key
try:
    with open(sys.argv[1], 'rb') as sec_key, \
            open(sys.argv[2], 'rb') as cipher_input, \
                open(sys.argv[3], 'wb') as shared_output:
        client_sec_key= base64.b64decode(sec_key.read())
        cipher_text= base64.b64decode(cipher_input.read())

        # the private KEM size is 1632
        if(len(client_sec_key)!=1632 ):
             print('Invalid client secret key in secret key file, exiting')
             sys.exit(1)

        # for kyber512 800 byte cipher key is only valid
        if(not validate_cipher_text(cipher_text)):
            print('Invalid cipher text size , allow 768 bytes only')
            sys.exit(1)
         
        # reinstantiate the client using the secret key    
        client = oqs.KeyEncapsulation(kemalg, client_sec_key)
        shared_secret_client =  client.decap_secret(cipher_text)
        shared_output.write(base64.b64encode(shared_secret_client))
except IOError:
    print('File errors, input the correct files')

except binascii.Error as e:
        print(f"Base64 decoding error")
    
    
    
