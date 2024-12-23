

# fetch system parameters and public key of the reciever
# includes alpha, p and beta


# TODO: check if the certificates are valid??
# get text files for the system parameter and recieiver certificates 
def get_public_keys(sys_param_file, rec_certificate):
    
    with open(sys_param_file, 'r') as sys_file, open(rec_certificate, 'r') as rec_file:
        sys_lines = sys_file.readlines() 
        rec_lines = rec_file.readlines()
        # read the second line for p 
        p = int(sys_lines[1].split(":")[1])


        alpha = int(sys_lines[2].split(":")[1])

        # convert to numbers 
        gamal_key = int(rec_lines[2].split(":")[1] ) 
    return p, alpha, gamal_key