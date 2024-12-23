import binascii
import sys, base64, oqs, os
from kem_util import kemalg

if(len(sys.argv) !=4):
    print('Provide correct arguments as shown below')
    print(' kem_gen_ciphertext {key_pub.b64} {ciphertxt.b64} {shared_sec.b64}')
    sys.exit(0)


try:
    with open(sys.argv[1], 'rb' ) as pub_input, open(sys.argv[2], 'wb') as cipher_output, \
    open(sys.argv[3], 'wb') as sec_output, oqs.KeyEncapsulation(kemalg) as server:
        # read 32 bytes public key decode base64
        pub_key = base64.b64decode(pub_input.read())

        # public key of the client is 800
        if(len(pub_key)!=800):
            print(f'Invalid public key in pubkey file, exiting')
            sys.exit(1)
        
        cipher_text, ssecret= server.encap_secret(pub_key) 
        cipher_output.write(base64.b64encode(cipher_text))
        sec_output.write(base64.b64encode(ssecret))
except IOError as e:
    print(e)
    # print('File errors, input the correct files')
except binascii.Error as e:
        print(f"Base64 decoding error")
    
    


        



