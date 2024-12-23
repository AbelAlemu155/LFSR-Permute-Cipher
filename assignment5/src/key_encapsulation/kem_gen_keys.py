

import sys, base64, os , oqs

# append path to access  directory 
from kem_util import kemalg

if(len(sys.argv) !=3):
    print('Provide correct arguments as shown below')
    print(' kem_gen_keys {key_pub.b64} {key_sec.b64}')

    sys.exit(1)


# append client to the folder for storing the public key output
pubilc_key_out_path = sys.argv[1] 

client_secret_out_path =  sys.argv[2] 
try:
    with open(pubilc_key_out_path, 'wb' ) as pub_output, open(client_secret_out_path, 'wb') as sec_output:
        client= oqs.KeyEncapsulation(kemalg)
        pub_key = client.generate_keypair()
        sec_key= client.export_secret_key()
        pub_output.write(base64.b64encode(pub_key))
        sec_output.write(base64.b64encode(sec_key))
except IOError:
    print('File errors, input the correct files')





    