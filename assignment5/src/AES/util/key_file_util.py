
import base64, numpy as np

# read a key file given a file name 
# return a tuple of the np uint8 array and boolean state 
# the boolean state indicates whether the length of the key file read is 32 
def read_key_file( filename ):
  fd = open(filename, 'rb')
  key_b = base64.b64decode( fd.read() ); fd.close()
  array_of_bytes = np.frombuffer(key_b, np.uint8, -1)
  
  len_check = len(array_of_bytes)==32
  return ( array_of_bytes, len_check )

# the same steps for writing to a key file of 32 bytes
def write_key_file( key, filename ):
  fd = open(filename, 'wb')
  fd.write( base64.b64encode(key) )
  fd.write( b'\n')
  fd.close()
  return
