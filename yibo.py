"""
symmetric cipher
"""

import random

def yibo_matrix(verbose=False):
    hex_literals = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']

    # 16x16 hex matrix
    hex_matrix = [hex_literals[row]+hex_literals[col] for col in range(16) for row in range(16)]

    if verbose:
        print "\nhex matrix"
        for i in [[hex_matrix[16*row+col] for col in range(16)] for row in range(16)]: print i

    # random shuffle hex matrix
    rnd_hex_matrix=[]
    for i in range(256):
        while True:
            r = hex_matrix[random.randint(0,255)]
            if r not in rnd_hex_matrix:
                rnd_hex_matrix.append(r)
                break

    # verify if there are no duplicate cells in the matrix
    if not (256==len(set(rnd_hex_matrix))): raise AssertionError("duplicate cells in rnd_hex_matrix")

    if verbose:
        print "\nRANDOM hex matrix"
        for i in [[rnd_hex_matrix[(16*row)+col] for col in range(16)] for row in range(16)]: print i

    return rnd_hex_matrix

def encrypt(mtrx, plainhex):
    return ''.join(mtrx[int(plainhex[i:i+2],16)] for i in range(0,len(plainhex),2))

def decrypt(mtrx, cipherhex):
    return ''.join(hex(mtrx.index(cipherhex[i:i+2]))[2:] for i in range(0,len(cipherhex),2))


mtrx=yibo_matrix(True)

pt="attack at dawn"
pthex= pt.encode('hex')

cthex= encrypt(mtrx, pthex)
ct   = cthex.decode('hex')

dthex= decrypt(mtrx, cthex)
dt   = dthex.decode('hex')

print "\nplaintext       :",pt,
print "\nplaintext    hex:",pthex
print "\nciphertext      :",ct,
print "\nciphertext   hex:",cthex
print "\ndeciphertext    :",dt,
print "\ndeciphertext hex:",dthex