import re
import nltk
import pickle
import keywords
import summary_file
import summarization
from time import sleep
from nltk.tokenize import RegexpTokenizer

def load_stop_words(stop_word_file):
    """
    Utility function to load stop words from a file and return as a list of words
    @param stop_word_file Path and file name of a file containing stop words.
    @return list A list of stop words.
    """
    stop_words = []
    for line in open(stop_word_file):
        if line.strip()[0:1] != "#":
            for word in line.split():  # in case more than one per line
                stop_words.append(word)
    return stop_words	

print("1.CellPhones and Accessories")
print("2.Clothes and Accessories")
print("3.Automotive")
print "Enter your choice"
dom_choice=int(raw_input())

domain_list=["CellPhones","Clothes&Acc","Automotive"]

if(dom_choice==1):
	f = open("../datasets/Brands/cellphones.pickle",'rb')
	object_file = pickle.load(f)
	domain=domain_list[0]
elif(dom_choice==2):
	f = open('../datasets/clothes_brands.txt', "r")
	domain=domain_list[1]
elif(dom_choice==3):
	f = open('../datasets/automotive_brands.txt', "r")
	domain=domain_list[2]

prodslist={}
c=0;
brandslist={}
prodslist={}
for brand in object_file.keys():
	#brand.append(line.split('|')[0])
	brandslist[c+1]=brand
	print str(c+1)+". "+brand+"\n"
	c+=1
	
print "Enter your choice"
ch=int(raw_input())
#ch=ch-1
selectedBrand = brandslist[ch]
print selectedBrand
c=0
for prods in range(len(object_file[selectedBrand])):
	for prod in object_file[selectedBrand][prods].keys():
		prodslist[c+1]=object_file[selectedBrand][prods][prod]
		print str(c+1)+". "+prod+"\n"
	c+=1

print "Enter your choice"
ch=int(raw_input())
#ch=ch-1	
print "1.Summary using Text Rank"
print "2.Summary using TF-IDF"
print "Enter your choice"
choice=int(raw_input())

summary=""

if choice==1:
	print "Do you want to enable debugging (Y/N)?"
	ch_debug=raw_input().lower()
	if ch_debug=="y" or ch_debug=="yes":
		rankedText = summarization.summaryGen(prodslist[ch],domain,debugging=True)
	else:
		rankedText = summarization.summaryGen(prodslist[ch],domain)	

	
	f.close()
	sleep(3)
	#rankedText=rankedText[:len(rankedText)/3]

if choice==2:
	print "Do you want to enable debugging (Y/N)?"
	ch_debug=raw_input().lower()
	print "Do you want to enter the token size (Y/N)?"
	ch_token=raw_input().lower()
	if ch_debug=="y" or ch_debug=="yes":
		if ch_token=="y" or ch_token=="yes":
			print "Enter token size"
			token=int(raw_input())
			rankedText=summary_file.summaryGen(prodslist[ch],domain,gram=token,debug=True)
		else:
			rankedText=summary_file.summaryGen(prodslist[ch],domain,debug=True)
	else:
		if ch_token=="y" or ch_token=="yes":
			print "Enter token size"
			token=int(raw_input())
			rankedText=summary_file.summaryGen(prodslist[ch],domain,gram=token)
		else:
			rankedText=summary_file.summaryGen(prodslist[ch],domain)

keys=keywords.extract_keywords(domain,prodslist[ch])
rankedSummary=""
for i in range(len(rankedText)):
	rankedSummary+=rankedText[i]
stopwords=load_stop_words("../stoplist.txt")
tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)
tokens = tokenizer.tokenize(rankedSummary)
tokens = [token for token in tokens if token.lower() not in stopwords]
precision = float(len(set(tokens).intersection(set(keys))))/float(len(tokens))
recall = float(len(set(tokens).intersection(set(keys))))/float(len(keys))
fmeasure = 2*(precision*recall)/(precision+recall)
print "\n\n"
print "Precision =",precision
print "Recall =",recall
print "F-Measure =",fmeasure
