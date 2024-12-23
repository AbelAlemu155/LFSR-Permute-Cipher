
import os 

# generate an integer randomly given bounds

def random_integer(lower, upper):
    range_size = upper - lower + 1
    num_bytes = (range_size.bit_length() + 7) // 8
    while True:
        random_number = int.from_bytes(os.urandom(num_bytes), 'big')
        if random_number < range_size:
            return lower + random_number