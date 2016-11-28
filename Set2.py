import codecs
import numpy as np
import base64
from Crypto.Cipher import AES

" ================ Check 9 =================== "
def PKCS7(block,length):
    if len(block) >= length:
        print('Block is already specified length')
        return
    block += b'\x04'*(length-len(block))
    return block
# print(PKCS7(b'This is a secret key',64))
" ============================================ "

