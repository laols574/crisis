from newsplease import NewsPlease
from newspaper.article import ArticleException

#ny_articles = NewsPlease.from_file("nytimes_urls.txt")
urls = open("urls/con_urls.txt")
urls = urls.readlines()
e_articles = []
for url in urls:
    try:
        e_articles.append(NewsPlease.from_url(url))
    except ArticleException:
        continue

#e_articles = NewsPlease.from_file("epoch_urls.txt")

#ny_file = open("ny_training_text.txt", "w")
e_file = open("training_text/con_training_text.txt", "w")

#ny_articles = [ny_articles[k] for k in ny_articles.keys()]
#e_articles = [e_articles[k] for k in e_articles.keys()]

#ny_str = ""
e_str = ""

'''
for article in ny_articles:
    if(article.maintext == None):
        continue
    ny_str += article.maintext
    ny_file.write(article.maintext)
'''
for article in e_articles:
    if(article.maintext == None):
        continue
    e_str += article.maintext
    e_file.write(article.maintext)


#print(len(ny_str.split()))
#print(len(e_str.split()))

#ny_file.close()
e_file.close()
