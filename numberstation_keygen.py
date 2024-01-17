import random
import os
import filepathgen as fg

file_path_key_test = os.path.join(fg.current_directory, 'keytext.txt')
def generator(source):
    letterlist = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ', ',','.',1,2,3,4,5,6,7,8,9,0]
    
    wordlist = []
    for i in range(len(source)):
        wordlist.append(source[i])

    raw_key = [] #raw_key is the encrypted messege, it will be added to the key later on
    for i in range(len(wordlist)):
        temp = []
        randomtemp = random.sample(letterlist, 4)
        temp.append(wordlist[i])
        for ii in range(len(randomtemp)):
            temp.append(randomtemp[ii])
        random.shuffle(temp)
        raw_key.append(temp)

    message = []
    for i in range(len(raw_key)):
        try:
            message.append(str(raw_key[i].index(wordlist[i])))
        except ValueError:
            pass
    
    #generate nested list with of up to ten inner lists with randomly picked characters
    n = random.randint(1,10)
    m = random.randint(3,12)
    random0 = []
    for i in range(n):
        random0.append(random.sample(letterlist, 5))
    
    # append actual keylist
    for i in range(len(raw_key)):
        random0.append(raw_key[i])
    #random number of lists with random characters
    for i in range(m):
        random0.append(random.sample(letterlist, 5))

    #add list after last random list, on index 0 the startindex for the encrypted message is safed
    indlist = []
    indtemp = []
    indlist.append(n)
    for i in range(4):
        indlist.append(random.choice(letterlist))
    random0.append(indlist) 

    text = ''.join(message)
            
    with open(file_path_key_test, 'w') as file_key:
        file_key.write(str(random0))
    return text
