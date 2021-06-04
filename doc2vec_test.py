import smart_open
import gensim

def read_corpus(fname, tokens_only=False):
    with smart_open.open(fname, encoding="iso-8859-1") as f:
        for i, line in enumerate(f):
            tokens = gensim.utils.simple_preprocess(line)
            if tokens_only:
                yield tokens
            else:
                # For training data, add tags
                yield gensim.models.doc2vec.TaggedDocument(tokens, [i])

train_corpus = list(read_corpus("training_text/lib_training_text.txt"))
test_corpus = list(read_corpus("training_text/lib_testing_text.txt", tokens_only=True))

print(train_corpus[0:2])
print(test_corpus[0:2])
