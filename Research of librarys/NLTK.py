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

##Dispersion Plot
    ##Dispersion plot shows where words appear in a text based on word count
    #for this,matplot lib has to be installed and imported

# import nltk
# import matplotlib.pyplot as plt
# from nltk.book import text5
# text5.dispersion_plot(["Hello","World","Today","The","And"])
# plt.show()

#this creates a lexical dispersion plot of the words found in the text

##generating Random Text
    ##generates random text based off of an input text and its context

# import nltk
# nltk.download("punkt_tab") ## this is a tokenizer which splits text into grouped sentences and words allowing for analyzing and generation
# from nltk.book import text4
# text4.generate()

#this generates random text based off of the context of the input text (Inaugural Address Corpus)

####Counting Vocabulary
    ##this section describes how to count the vocabulary of a text

##len
    ##len shows how many values are in a list as once tokenized the text becomes a list of words and punctuation

# import nltk
# from nltk.book import text7
# print(len(text7))

#this shows how many words and punctuation are in the text of Wall Street Journal

##set
    ##set shows the unique values in a list as once tokenized the text becomes a list of words and punctuation
    ##shows all different tokens in a text

# import nltk
# from nltk.book import text6
# print(set(text6))

#this shows all unique words and vocabulary used in the script of the movie Monty Python and the Holy Grail

####the lexical richness of a text is the ratio of unique to total words in a text
#### can calculate the percentage/frequency of words occuring in a text by dividing the count of a word in a text by the length of a text
#here are functions for each that i will leave in for further use just in case

def lexical_richness(text):
    return len(set(text)) / len(text)

def percentage_of_word(count, total):
    return (count / total) * 100

####Texts as lists of words


