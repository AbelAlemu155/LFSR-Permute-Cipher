

# a is the private key of the reciever 
from util.extended_euclidean import extended_euclidean_inverse
from util.mod_ex import modExEfficient


def decrypt_gamal(a, p, dec_file, dec_output ):
    with open(dec_file, 'rb') as file, open(dec_output, 'wb') as output:
        while(chunk:= file.read(8)):
            y1= int.from_bytes(chunk[:4], 'big')
            y2 = int.from_bytes(chunk[4:], 'big')
            secret = modExEfficient(y1,a,p )
            secret_inverse= extended_euclidean_inverse(secret, p)
            x = (y2* secret_inverse ) % p 
        
            output.write(x.to_bytes(1, byteorder='big'))



if __name__ == "__main__":
    a= 27197851          

    p= 100035179

    dec_file= 'elgamalfiles/key_aes_03.eg'

    dec_output= 'elgamalfiles/decrypted_key.b64'

    decrypt_gamal(a, p, dec_file, dec_output)

