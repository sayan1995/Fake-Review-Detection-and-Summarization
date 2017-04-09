import re
import os
import nltk
import json
import string
import collections
from nltk import tokenize
from textblob import TextBlob
from collections import Counter
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from progressbar import ProgressBar
pbar = ProgressBar()
import threading

docs={}
vocabulary = []
reviewList = []
stopwords = nltk.corpus.stopwords.words()
tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)

with open('../../datasets/Cell_Phones_and_Accessories_5.json', 'r') as f:
	json_data = f.read()
	list=re.findall(r'(\{.*})',json_data)
	fwrite = open('../../datasets/ML/cellphones_review.csv','w')
	reviewmap = {}
	for i in list:
		rating = 0
		data = json.loads(i)
		review = data["reviewText"]
		asin = data["asin"]
		f=open("../../datasets/CellPhones/"+asin+".txt","r")
	   	for line in f:
	    		if line.split(":")[0]=="score":
		    		rating += float(line.split(":")[1].split(".")[0]+"."+line.split(":")[1].split(".")[1]) 
		ff=open("../../datasets/CellPhones/"+asin+".txt","r")	
		reviewList = ff.read().split("\n\n")
		average_rating = rating/float(len(reviewList))	
		text = nltk.word_tokenize(review)
		pos_tagged = nltk.pos_tag(text)
		counts = Counter(tag for word,tag in pos_tagged)
		caps = len(filter(lambda x: x in string.uppercase, review))
		analyze_text = TextBlob(review)
		review_status = [0 for i in range(6)]
		review_data = [0 for i in range(6)]
		if len(review)!=0:# and abs(average_rating-float(data["overall"]))>2:
			c = Counter(c for c in review if c in ["?","!"])
			review_data[0] = abs(float(data["overall"])-average_rating)
			review_data[1] = analyze_text.subjectivity
			review_data[2] = float(caps)/len(review)
			review_data[3] = float(c["?"]+c["!"])/len(review)
			review_data[4] = len(analyze_text.words)
			helpfulness = float(data['helpful'][0])/float(data['helpful'][1]) if data['helpful'][1] else 0
			review_data[4] = helpfulness						
			if abs(float(data["overall"])-average_rating)>2:
				review_status[0] = 1
			if analyze_text.subjectivity < 0.5:
				review_status[1] = 1
			if float(caps)/len(review) >= 0.5:
				review_status[2] = 1
			if float(c["?"]+c["!"])/len(review) >=0.1:
				review_status[3] = 1
			if len(analyze_text.words) <=135:
				review_status[4] = 1
			if helpfulness == 0:
				review_status[5] = 1
			detection_counter=collections.Counter(review_status)
			if(detection_counter[1]>3):
				label = "y"
			else:
				label = "n"
			fwrite.write(data["reviewerID"]+","+data["asin"]+","+str(review_data[0])+","+str(review_data[1])+","+str(review_data[2])+","+str(review_data[3])+","+str(review_data[4])+","+str(review_data[5])+","+label+"\n")	
		
		#print counts['PRP'],counts['PRP$']
		
