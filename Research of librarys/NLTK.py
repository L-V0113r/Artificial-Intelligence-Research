#this file is the research of code snippets for nltk natural language processing library


####this snippet opens a menu which allows for the selection of download of various corpora and models for natural language processing tasks

# import nltk  
# nltk.download() 
#from nltk.book import *


####this allows for users to select the data or model used for their NLP tasks
####corpora is a collection of texts and models that can be used for natural language processing tasks.
##using this to recieve the text data for the task write it as a variable
##Type: 'texts()' or 'sents()' to list the materials.

####data must be downloaded to be seen/used
####i downloaded :
####the book module, which contains a collection of texts from various sources, including literature, news articles, and scientific papers.
#### when nltk.book is imported it shows introductory examples for the nltk boo module get around by importing indivual texts

####this shows what texts(only) are available in the book module/downloaded
# import nltk  
# from nltk.book import *
# texts()

#### sents shows the sentences and textsavailable in the book module/downloaded 

# import nltk
# from nltk.book import *
# sents()

####SEARCHING TEXTS
####this section describes how to search texts

##Cordance
    ##Cordance view shows every occurance of a given word with some contect

# import nltk
# from nltk.book import text2
# text2.concordance("Man")

#this code specifically shows all the occasions where man appears in text 2 (Jane austen) and applies context to it aswell

##Similar
    ##Similar shows where texts hold similar contexts to a similar word ie synonyms found in the text

# import nltk
# from nltk.book import text1
# text1.similar("Love")

#this snippet shows all synonyms where the context of the input word is presented in moby dick

##Common Contexts
    ##Common contexts shows where two words are used in similar contexts

# import nltk
# from nltk.book import text3
# text3.common_contexts(["fish", "God"])

#finds where fish and God are used in similar contexts in the text of the book of Genesis

##
