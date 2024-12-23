

import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from AES.util.key_file_util import write_key_file
from elgamal.util.mod_ex import modExEfficient

def find_private_key(alpha, p, beta, lower_bound, upper_bound):
    for b in range(lower_bound, upper_bound):
        if(beta == modExEfficient(alpha, b, p)):
            print(f'Private key of landon is: {b}')
            
            return
    print('unable to find a key')


p = 100035179
alpha = 22055634

beta= 40948688

lower_bound= 85393050

upper_bound = 85393150

find_private_key(alpha, p, beta,lower_bound , 100035178 )
