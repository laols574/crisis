'''
Author: Lauren Olson
Description:
Python program to generate word vectors using Word2Vec
'''
# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger')

import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec
from gensim.parsing.preprocessing import STOPWORDS

from nltk.parse.generate import generate
from nltk import CFG

NOUNS = ["NN", "NNS", "NNPS", "NNP"]
VERBS = ["VB","VBD","VBG","VBN","VBP","VBZ"]
GRAMMAR = CFG.fromstring("""
    S -> NP VB
    NP -> DET N 
    VP -> V""")

def main():
    #  Reads ‘ny_training_text.txt’ file

    file_name = input("con or lib")
    sample = open("training_text/" + file_name + "_training_text.txt", "r")
    s = sample.read()

    # Replaces escape character with space
    corpus = s.replace("\n", " ")

    #remove stopwords
    sw = input("none, 1, 10, 100")
    corpus = remove_stopwords(corpus, sw)

    #tokenize data
    data = tokenize(corpus)

    #ask whether the user wants a skip gram model
    skip_gram = int(input("skip_gram? 1 or 0"))


    model1 = gensim.models.Word2Vec(data, min_count = 1,
                                  vector_size = 100, window = 5, sg=skip_gram)


    #ask for word and print results
    test_word = input("word?")
    print(model1.wv.most_similar(test_word, topn=10))




"""
generate_sequence

This function takes a word as input and "builds a sentence"
by finding the most likely word given a list of words

input: the word used to start the sequence
 num = the number of words you want to generate
output: printed sentence
"""
def generate_sequence(word, num):
    sims = set()
    sentence = [word]

    while(len(sims) < num):
        sim_pairs = model1.wv.most_similar(positive=sentence, topn=100)

        i = 0
        word = sim_pairs[i][0]
        while(word in sims):
            word = sim_pairs[i][0]
            i += 1

        print(word, end=" ")

        sentence.append(word)
        sims.add(word)

    print()

"""
generate_nouns
generate nouns most similar to an input word
input: word, num = the number of words you want to generate
output: the printed nouns and their similarity scores
"""
def generate_nouns(word, num):
    sims = set()

    while(len(sims) < num):
        sim_pairs = model1.wv.most_similar(positive=word, topn=20)
        words = [pair[0] for pair in sim_pairs]

        pos_tags = nltk.pos_tag(words)

        words = [pos_tag[0] for pos_tag in pos_tags if pos_tag[1] in NOUNS]

        for word in words:
            sims.add(word)

"""
generate_verbs
generate verbs most similar to an input word
input: word, num = the number of words you want to generate
output: the printed nouns and their similarity scores
"""
def generate_verbs(word, num):
    sims = set()

    while(len(sims) < num):
        sim_pairs = model1.wv.most_similar(positive=word, topn=20)
        words = [pair[0] for pair in sim_pairs]

        pos_tags = nltk.pos_tag(words)

        words = [pos_tag[0] for pos_tag in pos_tags if pos_tag[1] in VERBS]

        for word in words:
            sims.add(word)


"""
function: remove stopwords

input: the training text (string)
output: the training text but without the stopwords (string)

"""
def remove_stopwords(text, num):
    if(num == 0):
        return text
    new_text = ""

    #remove custom stop words
    text_list = text.split()

    stop = open("stop_words/stopwords" + num + "k.txt")
    stop = stop.readlines()
    my_stop_words = STOPWORDS.union(set(stop))

    for word in text_list:
        if(word in my_stop_words):
            continue
        else:
            new_text += word + " "

    return new_text

if __name__ == "__main__":
    main()


def tokenize(corpus):
    data = []

    # iterate through each sentence in the file
    for i in sent_tokenize(corpus):
        temp = []

        # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())

        data.append(temp)

    return data
