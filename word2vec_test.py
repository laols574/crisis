'''
Author: Lauren Olson
Description:
Python program to generate word vectors using Word2Vec
'''
# importing all necessary modules
import re
import numpy

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

nltk.grammar._STANDARD_NONTERM_RE = re.compile('( [\w/][\w$/^<>-]* ) \s*', re.VERBOSE)


NOUNS = ["NN"]
#["NN", "NNS", "NNPS", "NNP"]
VERBS = ["VB","VBD","VBG","VBN","VBP","VBZ"]
GRAMMAR = """S -> NP VP
            DET -> 'a'
            DET -> 'the'
            NP -> DET N
            VP -> V
            VP -> VBD PP
            PP -> P NP
            P -> 'in'
            P -> 'with'
            """

def main():

    file_name = input("con or lib:   ")
    sample = open("training_text/" + file_name + "_training_text.txt", "r")
    s = sample.read()

    # Replaces escape character with space
    corpus = s.replace("\n", " ")

    #remove stopwords
    sw = input("0, 1, 10, 100:   ")
    corpus = remove_stopwords(corpus, sw)

    #tokenize data
    data = tokenize(corpus)

    #ask whether the user wants a skip gram model
    skip_gram = int(input("skip_gram? 1 or 0:   "))


    model = gensim.models.Word2Vec(data, min_count = 1,
                                  vector_size = 100, window = 5, sg=skip_gram)


    #ask for word and print results
    test_word = input("word?   ")
    print(model.wv.most_similar(test_word, topn=10))

    generate_sequence(model, test_word, 20)

    sim_nouns = generate_nouns(model, test_word, 2)

    sim_verbs = generate_verbs(model, test_word, 2)

    custom_grammar = generate_grammar(sim_nouns, sim_verbs)

    generate_sentence(custom_grammar, model)


"""
generate_grammar

takes the generates a grammar from the most similar nouns and verbs

"""
def generate_grammar(nouns, verbs):
    '''
    f = open("grammar/basic_grammar.txt", "r")
    dg = f.read()
    f.close()
    '''
    dg = GRAMMAR
    for noun in nouns:
        noun.replace("'", "")
        dg += "N -> '" + noun + "'\n"

    for verb in verbs:
        noun.replace("'", "")
        dg += "V -> '" + verb + "'\n"

    grammar = CFG.fromstring(dg)

    return grammar

"""
generate_sentence

takes the generated grammar from the most similar nouns and verbs
and creates a sentence
"""
def generate_sentence(grammar, model):
    for sentence in generate(grammar, n=100000):
        #print("word1: ", sentence[1], " word2: ", sentence[2], " similarity: ", cosine_similarity(sentence[1], sentence[2], model))
        #if(cosine_similarity(sentence[1], sentence[2], model) > .98):
        print(' '.join(sentence))
        quit()

"""
generate_sequence

This function takes a word as input and "builds a sentence"
by finding the most likely word given a list of words

input:
model = the word2vec model
word = the word used to start the sequence
 num = the number of words you want to generate
output: printed sentence
"""
def generate_sequence(model, word, num):
    print(word + ": GENERATED SEQUENCE: ")

    sims = set()
    sentence = [word]

    while(len(sims) < num):
        sim_pairs = model.wv.most_similar(positive=sentence, topn=100)

        i = 0
        word = sim_pairs[i][0]
        while(word in sims):
            word = sim_pairs[i][0]
            i += 1

        print(word, end=", ")

        sentence.append(word)
        sims.add(word)

    print("\n\n\n")


"""
generate_nouns
generate nouns most similar to an input word
input:
model = the word2vec model
word = the word
num = the number of nouns you want to generate
output: the printed nouns and return set of nouns
"""
def generate_nouns(model, word, num):
    print(word + ": SIMILAR NOUNS: ")
    sims = set()

    while(len(sims) < num):
        sim_pairs = model.wv.most_similar(positive=word, topn=100)
        words = [pair[0] for pair in sim_pairs]

        pos_tags = nltk.pos_tag(words)

        words = [pos_tag[0] for pos_tag in pos_tags if pos_tag[1] in NOUNS]

        for word in words:
            if(len(sims) >= num):
                break
            sims.add(word)
            print(word, end=", ")

    print("\n\n\n")
    return sims
"""
generate_verbs
generate verbs most similar to an input word
input:
model = the word2vec model
word = the word
num = the number of verbs you want to generate
output: the printed verbs and return set of nouns
"""
def generate_verbs(model, word, num):
    print(word + ": SIMILAR VERBS: ")

    sims = set()

    while(len(sims) < num):
        sim_pairs = model.wv.most_similar(positive=word, topn=100)
        words = [pair[0] for pair in sim_pairs]

        pos_tags = nltk.pos_tag(words)

        words = [pos_tag[0] for pos_tag in pos_tags if pos_tag[1] in VERBS]

        for word in words:
            if(len(sims) >= num):
                break
            sims.add(word)
            print(word, end=", ")

    print("\n\n\n")
    return sims



"""
function: remove stopwords

input: the training text (string)
output: the training text but without the stopwords (string)

"""
def remove_stopwords(text, num):
    if(int(num) == 0):
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

def cosine_similarity(word1, word2, model):
    return numpy.dot(model.wv[word1], model.wv[word2])/(numpy.linalg.norm(model.wv[word1])* numpy.linalg.norm(model.wv[word2]))


if __name__ == "__main__":
    main()
