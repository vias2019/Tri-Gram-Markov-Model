import sys
from Markov import *

# Function to remove punctuation
def punctuation(char):
    res = char
    if (char == '\n'):
        res = ''
    punctuations = '''!()[]{};:'"\,<>/?@#$%^&*_~'''
    if res in punctuations:
        res = ''
    return(res)

sentence_array = [] 
str = ''  
# Function to get a sentence in order to populate hash tables.
# The function processes a line by line until "." Each word in a sentence is stored in sentence_array and then calls the function "populate_hashtables"
def processText(file,function):
    global sentence_array, str
    header = 4
    next_line = 1
    Lines = file.readlines()
    for line in Lines:
        if (header != 0):
            header -= 1
            continue
        for i in line:
            temp = punctuation(i)
            if (temp == ' ' and str == '' ): continue
            #get rid of '--'
            if (temp == '-' and (str == '' or str[-1] == '-')):
                if str != '': str = str[:-1]
                if str != '':
                    sentence_array.append(str.lower())
                    str = ''
                continue
            # ignore "CHAPTER"
            if (str == 'CHAPTER' and next_line == 1):
                next_line -= 1
                break
            # ignore a line after "CHAPTER"
            if (next_line == 0):
                next_line = 1
                str = ''
                break
            if (temp == '.' and (str == 'Mr' or str.isupper())):
                str = str + temp
                continue
            if ((temp != '' and temp != ' ') and temp != '.'):
                str = str + temp
                continue
            if (temp == ' ' and str != ''):
                sentence_array.append(str.lower())
                str = ''
                continue
            if (temp == '.' and str != ''):
                sentence_array.append(str.lower())
                str = ''
                #insert in unigram,bigram and trigram
                populate_hashtables(sentence_array, function)
                sentence_array = []
                continue

if __name__=="__main__":
    # to build unigram
    file1 = open('stud.txt', 'r')
    processText(file1, 1)
    file1 = open('vall.txt', 'r')
    processText(file1, 1)
    
    # to build a bigram
    file1 = open('stud.txt','r')
    processText(file1, 2)
    file1 = open('vall.txt','r')
    processText(file1, 2)
   
    # to build a trigram
    file1 = open('stud.txt','r')
    processText(file1, 3)
    file1 = open('vall.txt','r')
    processText(file1, 3)
    
    writeToFile()
    
    print ('The end')
   

    