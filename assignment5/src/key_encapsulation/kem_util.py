

kemalg = "Kyber512" 


def validate_cipher_text(cipher_text):
    if kemalg== "Kyber512":
        if(len(cipher_text)==768):
            return True
    return False
        

       