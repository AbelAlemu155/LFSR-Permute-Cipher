
# O(e)
def modEx(b,e, p):
    # initialize the output to multiply to
    output= 1
    # make b < p if b is large
    b = b % p 
    if(b==0): return 0
    for _ in range(e):
        output= (output *b) % p
    return output

# O(log(e)), efficient implementation using right shift operations 
def modExEfficient(b,e,p ):
     # initialize the output to multiply to
    output= 1
    # make b < p if b is large
    b = b % p 
    if(b==0): return 0
    while(e > 0):
        # check if the last bit is 1 and mulitply to the result 
        if(e & 1 ):
            output= (output * b) % p

        # perform a right shift operation to get the next result update from e  
        e = e >> 1
        # compute the next b to multiply on as one bit is shifted from e 
        b= (b*b) % p
    return output


    
