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
## Fermat Primiality test

def is_prime(a):
    if a < 4:
        return True
    rand=random.randrange(2,a-1)
    return (rand**(a-1))%a == 1

## Brute force primality test

from math import sqrt
def prime(a):
    if a < 2: return False
    for x in range(2, int(sqrt(a)) + 1):
        if a % x == 0:
            return False
    return True

## Prime random number generator

def prng():
    rand=random.randrange(2,1000)
    while not prime(rand) :
        rand=random.randrange(2,1000)
    return rand

## Public Exponend computer
def public_exp(phi):
    a = 0
    e = 0
    while(a!=1):
        e = random.randrange(1,phi)
        a,_ = eea(phi,e)
    return e

def rsa_keypair():
    p = 0
    q = 0
    while(p == q):
        p = prng()
        q = prng()
    n   = p*q
    phi = (p-1)*(q-1)
    e   = public_exp(phi)
    one,d   = eea(phi,e)
    assert one == (e*d)%phi == 1
    return e,d,n

def rsa_encrypt(mess,e,n):
    return (mess**e)%n

def rsa_decrypt(encrypted,d,n):
    return (encrypted**d)%n



e,d,n = rsa_keypair()
print("Public Key        E: "+str(e))
print("Public            N: "+str(n))

print("Private Key       D: "+str(d))
x=random.randrange(int(sqrt(n)))
print("Message           X: "+str(x))

# Encrypt with public
y   = rsa_encrypt(x,e,n)
print("Encrypted Message Y: "+str(y))

# Decrypt with private
dec = rsa_decrypt(y,d,n)

print("Decrypted Message  : "+str(dec))
print("Is ok? [True/False]: "+str(dec == x))
