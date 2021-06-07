"""
Author: Lauren Olson

Description: This file will contain the implementation
allowing for prediction of sentences by using BERT
"""

#needed packages
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score
import torch
import transformers as ppb

import warnings
warnings.filterwarnings('ignore')

import pytest


def main():

    df = pd.read_csv("train.csv", header=None)

    #df = pd.read_csv('https://github.com/clairett/pytorch-sentiment-classification/raw/master/data/SST2/train.tsv', delimiter='\t', header=None)

    df = df.sample(frac=1).reset_index(drop=True)

    df = df[:2000]


    model_class, tokenizer_class, pretrained_weights = (ppb.DistilBertModel, ppb.DistilBertTokenizer, 'distilbert-base-uncased')


    tokenizer = tokenizer_class.from_pretrained(pretrained_weights)
    model = model_class.from_pretrained(pretrained_weights)

    #PREPARE THE DATASET

    #tokenize
    tokenized = df[0].apply((lambda x: tokenizer.encode(x, add_special_tokens=True)))


    max_len = 0
    for i in tokenized.values:
        if len(i) > max_len:
            max_len = len(i)


    #pad lists to be the same size
    padded = np.array([i + [0]*(max_len-len(i)) for i in tokenized.values])


    #ignore the pad
    attention_mask = np.where(padded != 0, 1, 0)


    #RUN THE MODEL
    input_ids = torch.tensor(padded)
    attention_mask = torch.tensor(attention_mask)


    with torch.no_grad():
        last_hidden_states = model(input_ids, attention_mask=attention_mask)

    #slice part of ouput and use as features
    features = last_hidden_states[0][:,0,:].numpy()
    labels = df[1]
    #TRAIN/TEST SPLIT
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels)

    lr_clf = LogisticRegression()
    lr_clf.fit(train_features, train_labels)

    #meant to use pytest 
    assert lr_clf.score(test_features, test_labels) > .9

    #SCORE THE CLASSIFIER
    print(lr_clf.score(test_features, test_labels))


if __name__ == "__main__":
    main()
