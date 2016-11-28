import codecs
import numpy as np
import base64

" ================ Check 1 =================== "
# hexd = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# hexd = codecs.decode(hexd,encoding='hex')
# hexe = codecs.encode(hexd.strip(),encoding='base64')
# hexe = hexe.strip()
# print(hexe)
" ============================================ "

" ================= Check 2 ================== "
#
# hex1 = codecs.decode("1c0111001f010100061a024b53535009181c",encoding='hex')
# hex2 = codecs.decode("686974207468652062756c6c277320657965",encoding='hex')
# hex1 = list(hex1)
# hex2 = list(hex2)
# xor = np.bitwise_xor(hex1,hex2)
# xor = xor.tolist()
# print(codecs.encode(bytes(xor),encoding='hex'))
" ============================================ "

" ================= Check 3 ================== "
# hex = bytes.fromhex("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")
# alph = list(" etaoinshrdlcumwfgypbvkjxqz")
# alph.reverse()
# candidates = list()
#
# for i in range(256):
#     score = 0
#     output = b''
#     for byte in hex:
#         output += bytes([byte^i])
#     output = str(output,encoding='cp437')
#     print(output)
#     for letter in alph:
#         score += output.count(letter) * alph.index(letter)
#     candidates.append([score,output,i])
# candidates.sort(reverse=True)
# print(candidates[0])
" ============================================ "


" ================= Check 4 ================== "
'''
Alternatively I could have used a more accurate weight of each plaintext candidate by comparing the total makeup of the
plaintext candidate to an expected letter distribution
'''
# alph = list(" etaoinshrdlcumwfgypbvkjxqz")
# alph.reverse()
# everyline = list()
#
# for line in open('4.txt'):
#     line = line.strip()
#     hex = bytes.fromhex(line)
#     candidates = list()
#     for i in range(256):
#         score = 0
#         output = b''
#         for byte in hex:
#             output += bytes([byte^i])
#         for byte in output:
#             char = chr(byte)
#             if char in alph:
#                 score += alph.index(char)
#         candidates.append([score,output,i])
#     candidates.sort(reverse=True)
#     everyline.append(candidates[0])
# everyline.sort(reverse=True)
# print(everyline[0])
" ============================================ "

" ================= Check 5 ================== "
# key = input('Please enter a key for use ==> ')
# ciphertext = b''
# plaintext = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
# print('Plaintext\n===========================================')
# print(plaintext)
# print('===========================================')
# bytewise = bytes(plaintext,encoding='cp437')
# hexkey = bytes(key,encoding='cp437')
# for i in range(len(bytewise)):
#     ciphertext += bytes([bytewise[i]^hexkey[i%3]])
#     # print(chr(bytewise[i]))
# print(codecs.encode(ciphertext,encoding='hex'))
# print(len(codecs.encode(ciphertext,encoding='hex')))
" ============================================ "

" ================= Check 6 ================== "
# # str1 = bytes(input("String 1 => "),encoding='cp437')
# # str2 = bytes(input("String 2 => "),encoding='cp437')
#
# def hammerdistance(str1,str2):
#     distance = 0
#     if len(str1) != len(str2):
#         print('Error: Strings not of same length.')
#         return
#     for i in range(len(str1)):
#         # print(bin(str1[i]^str2[i]))
#         distance += bin(str1[i]^str2[i]).count('1')
#     return distance
#
# def normal_distance(ciphertext,keysize):
#     distance = 0
#     for i in range(len(ciphertext)//keysize-1):
#         distance += hammerdistance(ciphertext[i*keysize:(i+1)*keysize],ciphertext[(i+1)*keysize:(i+2)*keysize])
#     return distance/((len(ciphertext)/keysize-1)*keysize)
#
#
# # fname = input('Base64-encoded repeating-key XOR ciphertext file ==> ')
#
# fname = '6.txt'
# ciphertext = base64.b64decode(open(fname).read().strip())
# keysizes = list()
# alph = list(" etaoinshrdlcumwfgypbvkjxqz")
# alph.reverse()
# max = 0
#
# for keysize in range(2,40):
#     candidate = normal_distance(ciphertext,keysize)
#     keysizes.append([candidate,keysize])
# keysizes.sort()
# # loop for top three keysizes
# for p in range(4):
#     avg = 0
#     key = list()
#     blocks = list()
#     for i in range(keysizes[p][1]):
#         blocks.append(ciphertext[i::keysizes[p][1]])
#     for block in blocks:
#         candidates = list()
#         for i in range(256):
#             score = 0
#             output = b''
#             for byte in block:
#                 output += bytes([byte^i])
#             for byte in output:
#                 char = chr(byte)
#                 if char in alph:
#                     score += alph.index(char)
#             candidates.append([score,chr(i),output])
#         candidates.sort(reverse=True)
#         # print(candidates[0])
#         key.append(candidates[0][1])
#         avg += candidates[0][0]
#     avg = avg/keysize
#     if avg > max:
#         max = avg
#         guessed_key = ''.join(key)
#     print('Guessed key {} with average score {}'.format(''.join(key),avg))
#
# print('======= Guessed Key Decryption Confidence: {} ======='.format(max))
# plaintext = ''
# hexkey = bytes(guessed_key,encoding='cp437')
# for i in range(len(ciphertext)):
#     plaintext += chr(ciphertext[i]^hexkey[i%len(hexkey)])
#     # plaintext[i] = ciphertext[i]^hexkey[i%len(hexkey)]
# print(plaintext)
# # print(codecs.encode(''.join(plaintext),encoding='cp437'))
" ============================================ "