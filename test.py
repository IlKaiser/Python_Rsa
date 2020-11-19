from Crypto.PublicKey import RSA
e,d,n = rsa_keypair(2048)
key=RSA.construct((n,e,d), consistency_check=True)
print(key.export_key())
print(key.publickey().export_key())
print(key.size_in_bits())

# 1K test
x=b'a'*1000

#print("Message           X: "+str(x))

# Encrypt with public
y   = rsa_encrypt(x,e,n)
print("Encryption Done!")

# Decrypt with private
dec = rsa_decrypt(y,d,n)

#print("Decrypted Message  : "+str(dec))
print("Is ok? [True/False]: "+str(dec == x)) 
