import random, sys, os

def main():
   # Step 1: Ask to user for prime

   p_str = raw_input('Write a prime, for example 389:')
   p=int(p_str)

   q_str = raw_input('Write another prime, for example 401:')
   q=int(q_str)

   n = p * q
   phi = (p-1)*(q-1)

   # We check the keySize, if phi > 1024 we limit the size
   if phi > 1024:
       phi = 1024

   publicKey, privateKey = generateKey(phi,p,q,n)
   print('Cryptosystem RSA for p %d and q %d ') % (p, q)
   print 'Public key:', publicKey
   print 'Private key:', privateKey


   print('Message has to be a number up to %d...') % phi
   message_str = raw_input('Choose the message:')
   message=int(message_str)

   signature = sign(message,privateKey,n)
   print 'Signature:', signature

   if valid(signature, publicKey, n, message):
       print 'VALID!!!'
   else:
       print 'NOT VALID!!!'


def gcd(a, b):
    # Return the GCD of a and b using Euclid's Algorithm
    while a != 0:
        a, b = b % a, a
    return b


def findModInverse(a, m):
    # Returns the modular inverse of a % m, which is
    # the number x such that a*x % m = 1

    if gcd(a, m) != 1:
        return None # no mod inverse if a & m aren't relatively prime

    # Calculate using the Extended Euclidean Algorithm:
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3 # // is the integer division operator
        v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m

def generateKey(phi,p,q,n):
   # Step 2: Create a number pseudoprime to (p-1)*(q-1).
   print 'Generating e...'
   while True:
      e = random.randrange(2 ** (phi - 1), 2 ** (phi))
      if gcd(e, (p - 1) * (q - 1)) == 1:
         break

   # Step 3: Calculate d, as a inverse of e.
   print 'Calculating d...'
   d = findModInverse(e, (p - 1) * (q - 1))
   publicKey = (n, e)
   privateKey = (n, d)

   return (publicKey, privateKey)

def sign(message, privateKey, n):
    # Step 3: Calculate signature = message^privateKey % n
    return message**privateKey[1] % n

def valid(signature, publicKey, n, message):
    # Step 4: Validate the signature
    check = signature**publicKey[1] % n
    print 'Check:', check
    if message == check:
        return True
    else:
        return False


if __name__ == '__main__':
   main()
