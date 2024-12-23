
import numpy as np
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes

class AESdecrypt_ECB(object):
  def __init__(self, key):
    self.__key = np.copy(key)
    self.__cipher = Cipher(algorithms.AES(self.__key), modes.ECB())
    self.__decryptor = self.__cipher.decryptor()
  
  def decrypt_blk(self, data_block):
    return( np.frombuffer(self.__decryptor.update(data_block), np.uint8, -1) )

  def finalize(self):
    self.__decryptor.finalize()
    return