
from decrypt_gamal import decrypt_gamal
from util.mod_ex import modExEfficient

    

p = 100035179
alpha = 22055634

beta= 40948688

private_exponent=85393102

dec_file= 'keys/key_aes_07.eg'

dec_output= 'keys/decrypted_key_landon.b64'

decrypt_gamal(private_exponent, p, dec_file, dec_output)