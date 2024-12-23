
import base64, os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from cryptography.hazmat.primitives.asymmetric import (padding, rsa, utils)
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography import exceptions
from cryptography.hazmat.primitives import hashes
from util.SHA256 import SHA256_c


def verify_signature(data_file, public_key):
    
    
    fd = open(data_file, 'rb')
    data_in = fd.read()
    fd.close()

    maxval = data_in.find(b'END***\n') + 7
    myHash = SHA256_c()
    myHash.push_data( data_in[:maxval] )

    # remove new line character since the signature does not contain a new line character 
    b64_sig = data_in[maxval:].replace(b"\n", b"").replace(b"\r", b"")
    sig_verify = base64.b64decode( b64_sig )
    

    try: 
        public_key.verify(
        sig_verify,
        data_in[: maxval],
        padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()  )

    except exceptions.InvalidSignature:
        return False 
    return True 


# define the public key object to use for verification
fd = open('keys/perk_public_rsa_key.txt', 'rb')
pub_key_b = fd.read()
fd.close()
public_key = load_pem_public_key(pub_key_b)
# verify the signature of all files in the system_parameters folder 

folder= 'certificate/system_parameters'
file_names = os.listdir(folder)

for name in file_names:
    path = folder + '/' + name 
    if(verify_signature(path, public_key)):
        print(f'Valid system parameter is the certificate: {path}')



