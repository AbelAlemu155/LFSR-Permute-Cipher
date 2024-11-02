import numpy as np, os, sys

# Define global variables accessed by all functions
# Initial register data
regInHex = 0x67BD5  
# Convert to binary string and remove the '0b' prefix
binaryStr = bin(regInHex)[2:]  


# use the function given to permute the values
# get an unsigned uint8 
def permute_encode(number):
    permutations = [ 2, 6, 3, 5, 1 , 8 , 4 , 7 ]
    # unpack the uint8 number into 8 bits 
    bits = np.unpackbits(np.array([number]))
    #initialize an array to copy to 
    newBits= np.zeros(8, dtype=np.uint8)
    # permute the list using the above permutation
    for i in range(len(permutations)):
        # subtract -1 for zero indexing 
        newBits[i]= bits[permutations[i]-1]
    # convert back to uint8
    newNumber = np.packbits(newBits)[0]
    return newNumber

# get an uint8 and associated lfsr output
def permute_decode(encByte, lfsrOutput): 
    permutedData = encByte ^ lfsrOutput
    # convert the permuteByte to bits 
    permutedBits= np.unpackbits(np.array([permutedData]))
    # apply reverse permutation on the permuted bits
    reversePermutation= [5,1, 3, 7, 4, 2, 8,6]
    unencBits = np.zeros(8, dtype=np.uint8)
    # set the reverse permuted values into a new array
    for i in range(len(reversePermutation)):
        unencBits[i]= permutedBits[reversePermutation[i]-1]
    
    # convert back to bytes 
    unencByte= np.packbits(unencBits)[0]
    return unencByte



def lfsr_xor(binaryArray):
    # representing the taps for lfsr
    polynomials= [13, 16, 17,18]
    # initalize array of size 8 to hold lfsr output 
    lfsrOutput = np.zeros(8, dtype=np.uint8)
    for i in range (0,8):
        sum= binaryArray[polynomials[0]]
        # bitwise xor all the values in the register for the polynomial taps
        for j in range(1, len(polynomials)):
            sum = sum ^ binaryArray[polynomials[j]] 
        # Before shifting store the last bit as the current output
        outputBit= binaryArray[-1]
        # use slicing to assign the shifted array ouputs
        binaryArray = np.insert(binaryArray[:-1], 0, 0)
        # add the sum as the most significant bit of the register bits 
        binaryArray[0]= sum
        # add the state into the lfsr output
        lfsrOutput[i]= outputBit
    
    # return the lfsr output and current registration bytes
    # pack the bits to represent byte information from bits
    return np.packbits(lfsrOutput)[0] , binaryArray


def encryptAFile(fileName):
    fdr = open(fileName, 'rb')
    indat_b = fdr.read() ; fdr.close()
    indat = np.copy( np.frombuffer(indat_b, np.uint8, -1) )
    # initialize the register value as bits array of 0X67BD5
    regData = np.array([int(bit) for bit in binaryStr], dtype=int)
    
    # use os feature to remove the extension of the file for better naming
    fileNoExtension= os.path.splitext(fileName)[0]
    with open(f'{fileNoExtension}_encrypted.dat', "wb") as outputFile:
        print(f'Encrypting a file to {fileNoExtension}_encrypted.dat, wait a few seconds!')
        # iterate the bytes of the file to be encrypted 
        for data in indat:
            # permute the byte of the data to be encrypted
            permutedData= permute_encode(data)
            # perform lfsr coninuously using the updated register data of 19 bits
            lfsrOutput = lfsr_xor(regData)
            # take the lfsr output and xor with the permuted data
            dataToWrite= lfsrOutput[0] ^ permutedData
            # write the data to a file
            outputFile.write(dataToWrite.tobytes())
            # update the register data after doing shift and sum mod 2 operations
            regData= lfsrOutput[1]
 

    

def decryptAFile(fileName):
    # read the file as bytes
    fdr = open(fileName, 'rb')
    indat_b = fdr.read() ; fdr.close()
    indat = np.copy( np.frombuffer(indat_b, np.uint8, -1) )
    # use os feature to remove the file extension for better naming
    fileNoExtension= os.path.splitext(fileName)[0]
    
    # use png file extensions for decrypting the file however any file type could work
    # initialize the register value as bits array of 0X67BD5
    regData = np.array([int(bit) for bit in binaryStr], dtype=int)
    with open(f'{fileNoExtension}_decrypted.png', "wb") as output_file:
        print(f'Decrypting a file to {fileNoExtension}_decrypted.png, wait a few seconds!')
        for data in indat: 
            lfsrOutput = lfsr_xor(regData)
            unpermutedData= permute_decode(data, lfsrOutput[0])
            output_file.write(unpermutedData.tobytes())
            # update the register data using the lfsr function output
            regData= lfsrOutput[1]
            
            



