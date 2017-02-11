import codecs
import numpy as np
import base64
from Crypto.Cipher import AES
from Set1 import *
from random import SystemRandom
import os

" ================ Check 9 =================== "
def PKCS7(block,length):
    # if len(block) >= length:
    #     print('Block is already specified length')
    #     return
    block += b'0'*length
    return block
# print(PKCS7(b'This is a secret key',64))
" ============================================ "

" ================ Check 10 ================== "
# This check was tricky because of how I was managing my bytes, doesn't actually work how I want it to, yet
# key = "YELLOW SUBMARINE"


def CBC_encrypt(plaintext,IV,key):
    if len(plaintext) % len(key) != 0:
        plaintext = bytes(PKCS7(plaintext,len(key)-len(plaintext)%len(key)))
    cipher = AES.new(key,AES.MODE_ECB)
    # print(len(plaintext))
    ciphertext = b''
    plain = []
    length = 16
    previous = IV
    for i in range(0,len(plaintext),length):
        plain.append(plaintext[i:i+length])
    # print(plain)
    for block in plain:
        # print(block)
        xor = xord(block,previous)
        # print(len(xor))
        crypto_block = cipher.encrypt(xor)
        ciphertext += crypto_block
        # print(crypto_block)
        previous = crypto_block
    return ciphertext

def CBC_decrypt(ciphertext,IV,key):
    cipher = AES.new(key,AES.MODE_ECB)
    plaintext = b''
    previous = IV
    length = 16
    cipherblocks = []
    for i in range(0,len(ciphertext),length):
        cipherblocks.append(ciphertext[i:i+length])
    for block in cipherblocks:
        xor = cipher.decrypt(block)
        plaintextchunk = xord(xor,previous)
        plaintext += plaintextchunk
        previous = block
    return plaintext

# def CBC_encrypt1(plaintext,key,IV):
#     cipher = AES.new(key, AES.MODE_ECB)
#     plain = b''
#     block = 16
#     previous = IV
#     print(IV)
#     ciphertext = b''
#     for i in range(len(plaintext)//block):
#         second = plaintext[i*block:(i+1)*block]
#         if len(previous) > len(second):
#             second = PKCS7(second,len(previous)-len(second))
#         elif len(second) > len(previous):
#             previous = PKCS7(previous, len(second)-len(previous))
#         plain = np.bitwise_xor(list(previous),list(second))
#         previous = cipher.encrypt(plain)
#         print(previous)
#         plain = cipher.encrypt(plain)
#         ciphertext += plain
#     return ciphertext
# IV = b'0'*16
# plaintext = base64.b64decode(open('lyrics.txt').read(),validate=False)
# print(len(plaintext))
# ciphertext = CBC_encrypt(plaintext,b'YELLOW SUBMARINE',IV)
#
# # ciphertext = base64.b64decode(open('10.txt').read())
#
# # print(ciphertext.decode('ascii'),'\n',len(ciphertext))
# print(CBC_decrypt(ciphertext,IV,b'YELLOW SUBMARINE').decode('ascii'))

# def CBC_encrypt(plaintext,key,IV):
#     ciphertext = b''
#     cipher = AES.new(key,AES.MODE_ECB)
#     previous = I
" ============================================ "
def keygen():
    return os.urandom(16)

def tossup_crypt(plaintext):
    cbc = SystemRandom().randrange(2)
    plaintext = os.urandom(SystemRandom().randrange(5,10))+plaintext+os.urandom(SystemRandom().randrange(5,10))
    if cbc:
        IV = keygen()
        key = keygen()
        print(IV,key,'CBC')
        return CBC_encrypt(plaintext,IV,key)
    else:
        if len(plaintext) % 16 != 0:
            plaintext = bytes(PKCS7(plaintext,16-len(plaintext)%16))
        key = keygen()
        print(key,'ECB')
        cipher = AES.new(key,AES.MODE_ECB)
        return cipher.encrypt(plaintext)

def detect(ciphertext):
    for k in range(1,17):
        repeated = list()
        count = 0
        ciphertext = list(ciphertext)
        for i in range(len(ciphertext) - 1):
            repeated.append(ciphertext[i:i + k])
        for block in repeated:
            count += repeated.count(block)
        print(count)

plaintext = codecs.encode(open('lyrics.txt').read(),encoding='ascii')
ciphertext = tossup_crypt(plaintext)
print(ciphertext)
detect(ciphertext)
