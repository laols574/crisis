"""
generate sentence
"""

import re
import nltk

nltk.grammar._STANDARD_NONTERM_RE = re.compile('( [\w/][\w$/^<>-]* ) \s*', re.VERBOSE)

from nltk.parse.generate import generate
from nltk import CFG

f = open("grammar/grammar_rules.txt", "r")

dg = f.read()

grammar = CFG.fromstring(dg)


for sentence in generate(grammar, n=10):
    print(' '.join(sentence))
