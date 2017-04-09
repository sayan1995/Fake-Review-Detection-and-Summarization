import os
import re
import json
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

def analyze():
	documents=[]
	for i in docs:
		documents.append(docs[i]['text'])
	tfidf_vectorizer = TfidfVectorizer()
	tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
	m,n = tfidf_matrix.shape
	doneflag=[0 for i in range(m)]
	reviewer = {}
	for i in range(m-1):
		cos_sim = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix)
		for j in range(len(cos_sim[0])):
			if cos_sim[0][j] > 0.75 and i!=j and docs[i]['reviewerID']==docs[j]['reviewerID'] and not doneflag[i] and not doneflag[j]:
				doneflag[i] = doneflag[j] = 1
				print docs[i]['asin']
				print docs[i]['text']
				print "\nis similar to\n"
				print docs[j]['asin']
				print docs[j]['text']

with open('../../datasets/Musical_Instruments_5.json', 'r') as f:
	json_data = f.read()
	list=re.findall(r'(\{.*})',json_data)
	for i in list:
		data = json.loads(i)
		reviews = "reviewerID"+":"+data["reviewerID"]+".\n"+"asin"+":"+data["asin"]+".\n"+data["reviewText"]
		reviewList.append(reviews);

	for i in range(len(reviewList)):
		docs[i] = {'freq': {}, 'tf': {}, 'idf': {},
				'tf-idf': {}, 'tokens': [], 'reviewerID':"",'text':"",'asin':""}
		sent=""
		reviewerID = "None";
		if(len(reviewList[i])!=0):
			sentences = tokenize.sent_tokenize(reviewList[i])
			for j in sentences:
				if j.split(":")[0]=="reviewerID":
					reviewerID = j.split(":")[1].split(".")[0]
				elif j.split(":")[0]=="asin":
					asin = j.split(":")[1].split(".")[0]
				else:
					sent+=j
			docs[i]["reviewerID"] = reviewerID
			docs[i]["text"] = sent
			docs[i]["asin"] = asin
analyze()

				

		
