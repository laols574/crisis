#CRISIS
------------

Author: Lauren Olson [laols574](mailto:laols574@email.arizona.edu)  
Date: 6/3/2020


## Notes
This project is a work in progress. As of this commit, I have collected news data from ~1300 conservative and ~1300 liberal news articles. 
After doing so, I used these separate collections of data to train a word2vec model to ascertain an intuitive understanding of the belief
systems behind conservatism and liberalism. So, I've been looking into the sentiment and associated nouns/verbs with terms like "good" and
"bad" with these models. 

The end goal currently is to create a conversational agent which shows understanding of the beliefs of an interlocutor on each side of the 
political spectrum to make said interlocutor feel understood and then espouse beliefs of the other side, hopefully giving the user a 
bit of an existential crisis. 


## Included files

* training_text - folder with the text of the articles
* urls - folder with url lists
* grammar - upenn tags and a set of grammar rules
* generate_grammar - takes the training text and generates random sentences based on the grammar defined in "grammar_rules.txt"
* stop_words - csv files of stopwords and their frequency, text files of just stopwords, "csv_to_text.py"
* doc2vec.py - a program to summarize and compare news articles? (we ain't there yet)
* word2vec_text.py - analyzing word2vec and the training texts
* crisis.py - this will be the file the user interacts with, blending the other programs together 

### Needed packages 

These packages were all installed via `pip3 install <package>` because I use python3 on a Mac (BigSur v 11.4)
* nltk
* gensim 
* afinn
* csv
* sys
* smart_open
* re
* newsplease
* warnings 
  
  
## References
https://www.allsides.com/media-bias/media-bias-chart

https://tedboy.github.io/nlps/generated/generated/gensim.models.Word2Vec.most_similar.html

https://radimrehurek.com/gensim/auto_examples/tutorials/run_word2vec.html

https://www.geeksforgeeks.org/python-word-embedding-using-word2vec/

https://github.com/vikasing/news-stopwords

http://www.nltk.org/_modules/nltk/parse/generate.html

https://pypi.org/project/essential-generators/


