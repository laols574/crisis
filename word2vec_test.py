# Python program to generate word vectors using Word2Vec

# importing all necessary modules
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('averaged_perceptron_tagger')

import warnings

warnings.filterwarnings(action = 'ignore')

import gensim
from gensim.models import Word2Vec
from gensim.parsing.preprocessing import STOPWORDS

def main():
    #  Reads ‘ny_training_text.txt’ file

    file_name = input("con or lib")
    sample = open(file_name + "_training_text.txt", "r")
    s = sample.read()

    # Replaces escape character with space
    f = s.replace("\n", " ")

    sw = input("none, 1, 10, 100")
    f = remove_stopwords(f, sw)

    data = []

    # iterate through each sentence in the file
    for i in sent_tokenize(f):
        temp = []

        # tokenize the sentence into words
        for j in word_tokenize(i):
            temp.append(j.lower())

        data.append(temp)

    skip_gram = int(input("skip_gram? 1 or 0"))
    # Create CBOW model
    model1 = gensim.models.Word2Vec(data, min_count = 1,
                                  vector_size = 100, window = 5, sg=skip_gram)


    # Print results
    sims = set()

    num = 20
    nouns = ["NN", "NNS", "NNPS", "NNP"]
    verbs = ["VB","VBD","VBG","VBN","VBP","VBZ"]
    sentence = ["good"]
    test_word = input("word?")
    print(model1.wv.most_similar(test_word, topn=10))
'''
    while(len(sims) < num):
        sim_pairs = model1.wv.most_similar(positive=sentence, topn=100)

        i = 0
        word = sim_pairs[i][0]
        while(word in sims):
            word = sim_pairs[i][0]
            i += 1

        print(word)
        #pos_tags = nltk.pos_tag(words)

        #words = [pos_tag[0] for pos_tag in pos_tags if pos_tag[1] in nouns]
        sentence.append(word)
        sims.add(word)

    print(sims)
'''

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

    stop = open("stopwords" + num + "k.txt")
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
