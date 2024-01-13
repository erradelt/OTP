import random
import os
import filepathgen as fg

file_path_key = os.path.join(fg.current_directory, 'keytext.txt')
def generator(source):
    letterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ', ',','.',1,2,3,4,5,6,7,8,9,0]
    
    wordlist = []
    for i in range(len(source)):
        wordlist.append(source[i])

    decrypt_key = []
    for i in range(len(wordlist)):
        temp = []
        randomtemp = random.sample(letterlist, 4)
        temp.append(wordlist[i])
        for ii in range(len(randomtemp)):
            temp.append(randomtemp[ii])
        random.shuffle(temp)
        decrypt_key.append(temp)

    message = []
    for i in range(len(decrypt_key)):
        try:
            message.append(str(decrypt_key[i].index(wordlist[i])))
        except ValueError:
            pass
    
    text = ''.join(message)
    return text

    for i in range(len(decrypt_key)):
        for ii in range(len(decrypt_key[i])):
            inner = ''.join(str(decrypt_key[i]))
        print(decrypt_key[i])


    with open(file_path_key, 'w') as file_key:
        file_key.write(str(decrypt_key))

