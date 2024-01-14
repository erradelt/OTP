import ast
import os

key = []

def filekey(keylist):
    temp = ast.literal_eval(keylist)
    for i in range(len(temp)):
        key.append(temp[i])

def decrypter(message):
    decrypted = []
    for i in range(len(key)): 
        decrypted.append(key[i][message[i]])
    text = ''.join(decrypted)
    return text