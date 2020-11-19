"""

RSA  python implementation

"""

## Extended Euclidean Algorithm for 
## multiplicative inverse

def eea(a,b):
    # Init
    t0=0
    t1=1
    original_a=a
    while b!=0:

        # Compute Stuff
        c=a%b
        q=(a-c)//b
        t=t0-q*t1

        # Update for next iteration
        t0=t1
        t1=t
        a=b
        b=c
    
    return a,t0%original_a

import random

## Fermat Primiality Test

def is_prime(a):
    if a < 4:
        return True
    rand=random.randrange(2,a-1)
    return pow(rand,a-1,a) == 1

## Brute force primality test

from math import sqrt
def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

## Prime random number generator
## Python3.9 Required to test!
## Not super accurate though ;(

import sys

def prng(n=128):
    if sys.version_info[1] >= 9 :
        rand = int.from_bytes(random.randbytes(n),"big")
        while not is_prime(rand):
            rand = int.from_bytes(random.randbytes(n),"big")
        return rand
    else:
        return old_prng(n*8)

## "Legacy" and slower but more accurate prng

def old_prng(n=1024):
    rand  = random.randrange(pow(2,n-1),pow(2,n) -1)
    while not is_prime(rand):
        rand  = random.randrange(pow(2,n-1),pow(2,n) -1)
    return rand

## Public Exponend computer

def public_exp(phi, standard=True):
    # Default e acording to standards
    if standard:
        return 65537
    # Choose a random e
    a = 0
    e = 0
    while(a!=1):
        e = random.randrange(1,phi)
        a,_ = eea(phi,e)
    return e

##
## RSA Core
##

def rsa_keypair(s=2048):
    size_q = s // 2
    size_p = s - size_q
    p = 0
    q = 0
    n = 0
    while(p == q):
        # prng() takes size in bytes
        p = prng(size_p//8)
        q = prng(size_q//8)
    n       = p*q
    phi     = (p-1)*(q-1)
    e       = public_exp(phi)
    one,d   = eea(phi,e)
    assert one == (e*d)%phi == 1
    return e,d,n

def rsa_encrypt_byte(mess,e,n):
    return pow(mess,e,n)

def rsa_decrypt_byte(encrypted,d,n):
    return pow(encrypted,d,n)

# Take bytes as an input
def rsa_encrypt(mess,e,n):
    enc = list(mess)
    return list(map(lambda x: rsa_encrypt_byte(x,e,n), mess))

# Take a list as an input
def rsa_decrypt(mess,d,n):
    return bytes(list(map(lambda x: rsa_decrypt_byte(x,d,n), mess)))