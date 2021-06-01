"""
Author Lauren Olson

generate grammar from file

"""

import nltk
nltk.download('averaged_perceptron_tagger')

import re

pos_desired = ['CC', 'CD', 'DT','FW', 'IN','JJ','JJR','JJS','LS','MD','NN','NNP','NNPS','NNS','PDT','POS','PRP','VBZ','VBP','VBN','VBG','UH','VB','VBD','SYM','RP','RBS','RBR','RB', 'PRP$', 'N']

f = open("ny_training_text.txt", "r")
sentList = f.readlines()
wordsList = []
for sent in sentList:
    wordsList += sent.split()

pos_tags = nltk.pos_tag(wordsList)

pos_dict = {}

for pair in pos_tags:
    word = re.sub(r'[^\w\s]','',pair[0])
    pos_tag = pair[1]

    if(pos_tag in pos_dict.keys()):
        pos_dict[pos_tag].add(word)
    else:
        pos_dict[pos_tag] = set()

g = open("ny_grammar.txt", "w")

for key in  pos_dict.keys():
    g.write(key + " -> ")
    i = 0
    for val in pos_dict[key]:
        if(i == len(pos_dict) - 1):
            g.write(" '" + val + "'")
        else:
            g.write("'" + val + "' | ")
        i += 1
    g.write("\n")
