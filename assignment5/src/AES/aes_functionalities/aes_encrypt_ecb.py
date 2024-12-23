
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes



class AESencrypt_ECB(object):
  def __init__(self, key):
    self.__key = np.copy(key)
    self.__cipher = Cipher(algorithms.AES(self.__key), modes.ECB())
    self.__encryptor = self.__cipher.encryptor()
  
  def encrypt_blk(self, data_block):
    return( np.frombuffer(self.__encryptor.update(data_block), np.uint8, -1) )

  def finalize(self):
    self.__encryptor.finalize()
    return
  
