# Simple bit level cipher using permutation and Linear Feedback Shift Registers for randomization

LFSR-Based File Encryption and Decryption
Overview
This project provides an implementation of file encryption and decryption using:

A Linear Feedback Shift Register (LFSR) for pseudo-random number generation.
Permutation encoding and decoding for data scrambling.
The solution is designed to securely process files, creating encrypted outputs and allowing for their decryption back to the original format.

Features
Encryption:

Permutes file data using a predefined permutation sequence.
Generates LFSR-based pseudo-random outputs to XOR with permuted data.
Produces an encrypted .dat file.
Decryption:

Reverses the encryption process using the LFSR output and reverse permutation.
Restores the original file from the encrypted .dat file.
File Structure
Encryption Function: encryptAFile(fileName)
Decryption Function: decryptAFile(fileName)
Helper Functions:
permute_encode(number): Applies a permutation to the data bits.
permute_decode(encByte, lfsrOutput): Reverses the permutation and restores original data.
lfsr_xor(binaryArray): Generates LFSR outputs using predefined polynomial taps.
Dependencies
The implementation uses the following Python libraries:

numpy: For bit-level manipulations and data processing.
os: For file path and extension handling.
sys: For potential command-line integration.
