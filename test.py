from rsa import *
from Crypto.PublicKey import RSA
import time

my_res,res = [],[]

# Init
start = time.time()
e,d,n = rsa_keypair(2048)
elapsed = time.time() - start
my_res.append(elapsed)
key=RSA.construct((n,e,d), consistency_check=True)
print(key.export_key())
print(key.publickey().export_key())
print(key.size_in_bits())

# .1K test
x=b'a'*100

start = time.time()
# Encrypt with public
y   = rsa_encrypt(x,e,n)

# Decrypt with private
dec = rsa_decrypt(y,d,n)
elapsed = time.time() - start
my_res.append(elapsed)


print("Is ok? [True/False]: "+str(dec == x)) 

# Keygen test
start = time.time()
keypy = RSA.generate(2048)
elapsed = time.time() - start
res.append(elapsed)
print(keypy.export_key())
print(keypy.publickey().export_key())
print(keypy.size_in_bits())

from Crypto.Cipher import PKCS1_OAEP
# Encryption test
x = b'a'*100
start = time.time()
cipher_rsa = PKCS1_OAEP.new(key.publickey())
encpy = cipher_rsa.encrypt(x)
cipher_rsa = PKCS1_OAEP.new(key)
decpy = cipher_rsa.decrypt(encpy)
elapsed = time.time() - start
res.append(elapsed)
print("Is ok? [True/False]: "+str(decpy == x))


# Plot results
import numpy as np
import matplotlib.pyplot as plt

X = np.arange(2)

ig,ax = plt.subplots(1, 2)

ax[0].bar(X, my_res[0], 0.35, label='my rsa')
ax[0].bar(X + 0.35, res[0], 0.35,label='pycryptodome rsa')
ax[0].legend(loc='best')
ax[0].set_title("keygen test (lower is better)")

ax[1].bar(X, my_res[1], 0.35, label='my rsa')
ax[1].bar(X + 0.35, res[1], 0.35,label='pycryptodome rsa')
ax[1].legend(loc='best')
ax[1].set_title("0.1k test (lower is better)")

plt.show()