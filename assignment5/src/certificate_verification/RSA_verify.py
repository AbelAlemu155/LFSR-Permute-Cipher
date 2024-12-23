#!/usr/local/bin/python3
import numpy as np
import math
import os,sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import sys
import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import (padding, rsa, utils)
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography import exceptions
from util.SHA256 import SHA256_c

#############
# Main starts here
#############

if len(sys.argv) != 4 :
  print(f"usage is: {sys.argv[0]} datafile pub_key.key sig.txt")
  sys.exit(1)

fd = open(sys.argv[2], 'rb')
pub_key_b = fd.read()
fd.close()
public_key = load_pem_public_key(pub_key_b)

fd = open(sys.argv[1], 'rb')
data_in = fd.read()
fd.close()

maxval = data_in.find(b'END***\n') + 7
myHash = SHA256_c()
myHash.push_data( data_in[:maxval] )
message = myHash.get_hash().tobytes()

fd = open(sys.argv[3], 'rb')
b64_sig = fd.read()
fd.close()

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
  print("ERROR!: Invalid signature detected")
  sys.exit(1)
print("Signature was verified!")  
