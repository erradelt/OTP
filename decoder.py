import ast
import os
import filepathgen as fg

file_path_key = os.path.join(fg.current_directory, 'keytext.txt') #'/home/robert/Python/02_OTP/keytext.txt'

with open(file_path_key, 'r') as file_key:
    key = file_key.read()
    keylist = ast.literal_eval(key)
#test
def decrypter(message):
    decrypted = []
    for i in range(len(keylist)):
        decrypted.append(keylist[i][message[i]])
    text = ''.join(decrypted)
    return text
    
