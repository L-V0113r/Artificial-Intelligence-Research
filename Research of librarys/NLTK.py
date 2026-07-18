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
    #basic python strings as lists of words etc

#slicing
    #using a (numb:numb) can give a range between two numbers in a list of words
    #can omit the first or last number depending on when it appears in the list

####Computing with language:Statistics!!!!

##Frequency Distribution
    ##frequency distriibution is the number of times a thing has occured

#fdist = FreqDist(text1)

##this produces an object that can be used to analyze the frequency distribution in a text

#fdist.most_common(50)

##this shows the 50 most common words in a text

#fdist.hapaxes()

###this shows the words that only occur once in a text

##Fine Grained selection of words
    ##this section describes how to select words based on their length and frequency of occurance

##using the word equivalent for set notation once the text is turned into a set filters can be applied to recieve certaint things

##Collocations and bigrams
    ##collocations are a sequence of words that occur together unusually often
    #bigrams are a sequence of word pairs

    #bigrams can be an object that can be used to analyze the frequency of word pairs in a text

#list(bigrams[list1])

#this shows the bigrams of a list of words

#collocations are frequent bigrams

##counting other things

# def word_Lengths_Distributions(text):
#     Lengths =[len(word) for word in text]
#     fdist = FreqDist(Lengths)
#     return fdist

##this returns the frequency of word lengths in a text

############Frequency distribution commands

# fdist = FreqDist(text1)

# fdist[text1] += 1
# #this increments the count of a word in the frequency distribution

# fdist["word"]
# #this returns the count of number of times a given sample occured

# fdist.freq("word")
# #frequency of a given sample

# fdist.N()
# #the total number of samples

# fdist.most_common(n)
# #returns the n most common samples and thier freq
# #can also iterate over the samples

# fdist.max()
# #sample with the highest frequency

# fdist.tabulate()
# #tabulates which is when the frequency distribution is displayed in a table format

# fdist.plot()
# fdist.plot(cumulative=True)#the cumulative plot version
# #plots the frequency distribution in a graph format

# fdist1 |= fdist2
# #combines two frequency distributions into one including the counts of each sample

# fdist1 < fdist2
# #determines if 1 is a subset of 2 which would mean samples occur les frequently in 1 than 2


###Word comparison operators

# s.startswith(t)
# s.endswith(t)
# #determines if a variable s ends or starts with a variable t

# t in s
# #determines if a variable t is in a variable s

# s.islower
# s.isupper
# #determines if char contained in s are all upper or all lower not mix

# s.isaplpha
# s.isalnum
# s.isdifit
# #determins if s isnt empty and all char are alphabetic , alphanumeric or digits

# s.istitle
# #are all words capitalised

#####Automatic NL understanding

##word sense disambiguation
    ##which sense a word was intended to give due to the contenxt ie which meaning of the word is implied by the surrounding

##Pronoun Resolution
    ##detecting the subjects and objects of verbs,what words imply based off of previous context ie theat bob is now him
    #find the antecedent to identify how a noun relates to the verb

##General Language output
    ##understanding of the pronouns in different language is required as they have different subsequent inferences depending on tense etc

##Machine translation
    #repeated translation is difficult due to the possible translations of words between languages
    #use text alignment

##Spoken Dialog systems
    ##Turing test,can a system reponding to a user perform naturally enough so that we cannot distinguish it
    
##simple Pipeline

#Phoneology => morphology => syntax => semantics => reasoning

#each step requires analysis and realisation aswell as a database/model to learn/utilise for generation/answering

##Textural entailment
    #how can you determine when a hypothesis can be deemed true or false and how do you determine from your source whether a hypothesis is true

##Limitations
    ##cannot perform reaoning or draw from real world knowledge

##################################################################################################################################################