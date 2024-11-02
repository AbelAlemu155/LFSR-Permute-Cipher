import sys

from functionalities import *
# define an option for encryption and decryption
options={'e', 'd'}
if len(sys.argv) != 3:
  print(f" Arguments not correctly provided, exiting")
  sys.exit(0)
elif sys.argv[1] not in options:
    print(f"Second option can only be 'e' or 'c' ") 
    sys.exit(0)
else:
    # extract option for encrypting or decrypting 
    type= sys.argv[1]
    fileName= sys.argv[2]
    if(type == 'e'):
        try:
            encryptAFile(fileName)
        except:
            print('Error getting file to encrypt')
    elif(type== 'd'):
        try:
            decryptAFile(fileName)
        except:
            print('Error getting file to decrypt')
    
        