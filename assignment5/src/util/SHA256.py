
import numpy as np, sys, os


from cryptography.hazmat.primitives import hashes

class SHA256_c(object):
  def __init__(self):
    self.__digest = hashes.Hash(hashes.SHA256())

  def push_data(self, data_block):
    self.__digest.update(data_block)

  def get_hash(self):
    return( np.frombuffer(self.__digest.finalize(), np.uint8, -1) )
