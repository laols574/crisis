'''
Author: Lauren Olson
Description: This program is intended to induce existential crises.

ELIZA works by forcing people to reconsider what they think, it
encourages participants to share more by asking them to question
what they think and why they think that way.

This is the default behavior, but there are keywords which trigger
certain phrases

ideas:
ask them what they believe about various things
find a piece of information which contradicts what they say
ask them if they still believe it
etc,etc,etc

plan rn:
find opposite article
summarize in their grammar
'''

import nltk
nltk.download('averaged_perceptron_tagger')
import word2vec

def main():
    train_model()

    end = "I gotta go"
    print("type 'I gotta go' to end the conversation")

    user = input("What's up?\n").lower()

    while(user.lower() != end.lower()):
        response = generate_response(user)
        user = input(response + "\n").lower()


"""
function: identify_pos

input: the user's input (string)
ex: "word1 ...wordn"
output: the pos of the user's words (list of tuples)
ex: [(word1, postag1), ... (wordn, postagn)]
"""
def identify_pos(user):
    wordsList = user.split()
    return nltk.pos_tag(wordsList)

"""
function: flip_user

input: the user's input (string), posList (list of tuples)
output: a new flipped string, adjusting the pronouns and their
order to fit

"""
def flip_user(user, posList):
    ret = user
    pronouns = [tup for tup in posList if tup[1] == "PRP" or tup[1] == "PRP$"]

    if(len(pronouns) == 0):
        return ret

    return ret




"""
function: generate_response

input: the user's input
output: the response of CRISIS

description: This function will identify
the correct reponse to the user
"""
def generate_response(user):
    ret = ""
    posList = identify_pos(user)

    question = [j for j in posList if j[1] == 'WRB']


    if len(question) != 0:
    	ret = "I cannot tell you " + flip_user(user, posList) + " only you can. Why don't you know?"

    return ret



#run the program
if __name__ == "__main__":
    main()
