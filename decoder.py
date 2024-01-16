import ast
import os

key = []
start = []

def filekey(keylist):
    temp = ast.literal_eval(keylist)
    start.append(temp[-1][0])
    for i in range(len(temp)):
        key.append(temp[i])

def decrypter(message):
    try:
        stop = int(start[0])+len(message)
        decrypted = []
        temp = []
        for i in range(start[0], min(stop, len(key))): 
            temp.append(key[i])

        for i in range(len(temp)):
            decrypted.append(temp[i][message[i]])
        text = ''.join(decrypted)
    except IndexError:
        text = 'key and message do not match'
    except TypeError:
        text = 'key and message do not match'
    return text