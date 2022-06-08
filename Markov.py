import random
from xml.etree.ElementPath import find

# node for the third word in trigram
class NodeLevel1:
    def __init__(self, key=None):
        self.key = key
        self.right = None
        self.next = None

#node for the second work in trigram        
class NodeLevel2:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = 1
        self.right = None

#LinkedList as a value for trigram key       
class LinkedList:
    def __init__(self):
        self.head = None # Initialize head as None
        
uni_word_count = 0
bi_word_count = 0
unigram = {}
bigram = {}
trigram = {}

#build a unigram
def insertUnigram (string):
    global uni_word_count, unigram
    string.lower()
    if (string != ''):
        if(string in unigram):
            uni_word_count += 1
            unigram[string] += 1
        else: 
            uni_word_count += 1
            unigram[string] = 1

#build a bigram
def insertBigram (str_pair):  #[str, str]
    global bi_word_count, bigram
    word = str_pair[0].lower() + " " +str_pair[1].lower()
    if (str_pair != ''):
        if(word in bigram):
            bi_word_count += 1
            bigram[word] += 1
        else:
            bi_word_count += 1
            bigram[word] = 1

#build a trigram              
def inserTrigram (trio):
    if trio[0] in trigram:
        insert_level_1(trigram[trio[0]], trio)
    else: 
        insertLevel_initial(trio)

# insert tree words to the trigram
def insertLevel_initial (trio):  
    trigram[trio[0]] = LinkedList()
    n1 = NodeLevel1(trio[1])
    n2 = NodeLevel2(trio[2])
    n1.right = n2
    n2.value = 1
    trigram[trio[0]].head = n1

# insert two words to the trigram (the first word is already in the table)
def insertLevel_both (trio):
    n1 = NodeLevel1(trio[1])
    n2 = NodeLevel2(trio[2])
    n1.right = n2
    n2.value = 1
    return n1

def check_level_2 (node, trio):
    curr = node
    while (curr.right != None):
        if (curr.right.key == trio[2]):
            curr.right.value += 1
            return
        curr = curr.right
        if (curr.right == None):
            n2 = NodeLevel2(trio[2])
            curr.right = n2

# insert one word to the table (the first two words are already in the table)
def insert_level_1 (self, trio):
    curr = self.head
    while (True):
        if curr.key == trio[1]:
            check_level_2(curr, trio)
            return
        if (curr.next == None):
            curr.next = insertLevel_both(trio) 
            return
        curr = curr.next

# populate all the hash-tables    
def populate_hashtables (str_arr, function): 
    if str_arr != '': 
        if function == 1: 
            for i in str_arr:
                insertUnigram(i)
        if function == 2:
            for i in range (0, len(str_arr) - 1):
                insertBigram([str_arr[i], str_arr[i + 1]])
        if function == 3:
            for i in range (0, len(str_arr) - 2):
                inserTrigram([str_arr[i], str_arr[i + 1], str_arr[i + 2]])

#test cases"
# populate_hashtables(['it','was','nice', 'it','is','cool','it','has','doll','it', 'was', 'ball'], 3)

# populate_hashtables(['it','was','nice', 'it','was','nice','it','has','doll','it', 'was', 'ball'], 3)

# populate_hashtables(['it','was','nice', 'it','was','cool','it','has','doll','it', 'was', 'ball'], 3)

# print('The End')

# searches the third word in the trigram with the biggest value of probability: 
# Example: Consider the following sentence S = “This is a test sentence from a document” P(test|a, is) = Count(is a test) / Count(is a) = 1/1 = 1
def searchLevel2 (node, l1, maxProb):
    max_l1 = l1
    max_l2 = node.key
    max_prob = maxProb
    curr = node
    while curr != None:
        if curr.value/bigram[(l1 + ' ' + curr.key)] > max_prob: 
            max_prob = curr.value/bigram[(l1 + ' ' + curr.key)]
            max_l1 = l1
            max_l2 = curr.key
        curr = curr.right
    return ([max_l1, max_l2, max_prob])

# searches the secind word in the trigram
def searchLevel1 (hash):
    maxProb = 0
    curr = hash.head
    res = []
    while (curr != None):
        res = searchLevel2(curr.right, curr.key, maxProb)
        maxProb = res[2]
        curr = curr.next
    response = [res[0],res[1]]
    return response

word_count = 0
word_limit = 2000
rand_word = ''
# find a tree words phrase. Starts from a random word from the trigram, serches it in trigram, then gets the last word of the tree in order to search it in trigram again. If a word is not in the trigram, then get a gandom word from the trigram.
def getPhrase ():
    global word_count, rand_word
    rand_word = random.choice(list(trigram))
    res = searchLevel1(trigram[rand_word])
    response = (rand_word + ' ' + res[0] + ' ' + res[1] + ' ')
    word_count = word_count + 3
    return response

#write to ReadMe.txt file
def writeToFile ():
    global word_limit
    while (word_count < word_limit):
        file = open("Readme.txt","a")
        temp = getPhrase()
        file.write(temp)
        file.close()
    
    
 
    
    

        

        