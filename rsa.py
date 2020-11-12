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


p = prng()
q = prng()
assert p!=q 
n = p*q
phi = (p-1)*(q-1)

e = public_exp(phi)
one,d = eea(phi,e) 
assert phi > e 
assert (e*d) % phi == 1
assert 1 == one
p = prng()
q = prng()
phi=(p-1)*(q-1)
n = p*q
e = public_exp(phi)
one,d=eea(phi,e)
assert one == (e*d)%phi == 1

print ("p: "+str(p))
print ("q: "+str(q))
print ("n: "+str(n))
print ("phi: "+str(phi))
print ("e: "+str(e))
print ("d: "+str(d))

import base64
x = int(input())
y = (x**e)%n

print(y)
dec = (y**d)%n 
print(dec)

