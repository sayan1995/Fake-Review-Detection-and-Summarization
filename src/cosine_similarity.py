import os
import re
import nltk
import math
from nltk import tokenize
from nltk.tokenize import RegexpTokenizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

docs={}
vocabulary = []
reviewList = []
stopwords = nltk.corpus.stopwords.words()
tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)

def parse(reviewFile,prodId):
	global reviewList
	directory="../datasets/reviews/"
	if not os.path.exists(directory):
		os.makedirs(directory)

	for _, _, files in os.walk(directory):
    		for file in files:
        		filepath = directory + file
			f = open(filepath,"r")
			reviews = f.read()
			reviewList.append(reviews);

	if len(reviewList)==0:
		f = open(reviewFile,"r")
		reviews = f.read()
		reviewList = reviews.split("\n\n");

	for i in range(len(reviewList)):
		docs[i] = {'freq': {}, 'tf': {}, 'idf': {},
				'tf-idf': {}, 'tokens': [], 'reviewerID':"",'text':""}
		sent=""
		reviewerID = "None";
		if(len(reviewList[i])!=0):
			sentences = tokenize.sent_tokenize(reviewList[i])
			for j in sentences:
				if j.split(":")[0]=="reviewerID":
					reviewerID = j.split(":")[1].split(".")[0]
				elif j.split(":")[0]=="score":
					score = j.split(":")[1].split(".")[0]
				else:
					sent+=j
			docs[i]["reviewerID"] = reviewerID
			docs[i]["text"] = sent
	analyze()
def analyze():
	documents=[]
	for i in docs:
		documents.append(docs[i]['text'])
	tfidf_vectorizer = TfidfVectorizer()
	tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
	m,n = tfidf_matrix.shape
	doneflag=[0 for i in range(m)]
	for i in range(m-1):
		cos_sim = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix)
		for j in range(len(cos_sim[0])):
			if cos_sim[0][j] > 0.5 and i!=j and docs[i]['reviewerID']==docs[j]['reviewerID'] and not doneflag[i] and not doneflag[j]:
				doneflag[i] = doneflag[j] = 1
				print docs[i]['text']
				print "\nis similar to\n"
				print docs[j]['text']
				

		
