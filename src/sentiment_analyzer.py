import os
import math
from nltk.classify import NaiveBayesClassifier
from nltk.corpus import subjectivity
from nltk.sentiment import SentimentAnalyzer
from nltk.sentiment.util import *
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize import RegexpTokenizer
from nltk import tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

'''n_instances = 100
subj_docs = [(sent, 'subj') for sent in subjectivity.sents(categories='subj')[:n_instances]]
obj_docs = [(sent, 'obj') for sent in subjectivity.sents(categories='obj')[:n_instances]]
train_subj_docs = subj_docs[:80]
test_subj_docs = subj_docs[80:100]
train_obj_docs = obj_docs[:80]
test_obj_docs = obj_docs[80:100]
training_docs = train_subj_docs+train_obj_docs
testing_docs = test_subj_docs+test_obj_docs
sentim_analyzer = SentimentAnalyzer()
all_words_neg = sentim_analyzer.all_words([mark_negation(doc) for doc in training_docs])
unigram_feats = sentim_analyzer.unigram_word_feats(all_words_neg, min_freq=4)
sentim_analyzer.add_feat_extractor(extract_unigram_feats, unigrams=unigram_feats)
training_set = sentim_analyzer.apply_features(training_docs)
test_set = sentim_analyzer.apply_features(testing_docs)
trainer = NaiveBayesClassifier.train
classifier = sentim_analyzer.train(trainer, training_set)
for key,value in sorted(sentim_analyzer.evaluate(test_set).items()):
	print('{0}: {1}'.format(key, value))

sid = SentimentIntensityAnalyzer()'''
docs={}
vocabulary = []
stopwords = nltk.corpus.stopwords.words()
tokenizer = RegexpTokenizer("[\w']+", flags=re.UNICODE)
def parse(reviewFile,prodId):
	directory="../datasets/reviews"
	if not os.path.exists(directory):
		os.makedirs(directory)
	f = open(reviewFile,"r")
	reviews = f.read()
	reviewList = reviews.split("\n\n");
	for i in range(len(reviewList)):
		docs[i] = {'freq': {}, 'tf': {}, 'idf': {},
				'tf-idf': {}, 'tokens': [], 'reviewerID':"",'text':""}
		sent=""
		if(len(reviewList[i])!=0):
			sentences = tokenize.sent_tokenize(reviewList[i])
			for j in sentences:
				if j.split(":")[0]=="reviewerID":
					reviewerID = j.split(":")[1].split(".")[0]
				else:
					sent+=j
			docs[i]["reviewerID"] = reviewerID
			docs[i]["text"] = sent
	analyze()

'''def analyze():
	def freq(word, doc):
	    return doc.count(word)

	def word_count(doc):
	    return len(doc)

	def tf(word, doc):
	    return (freq(word, doc) / float(word_count(doc)))

	def num_docs_containing(word, list_of_docs):
	    count = 0
	    for document in list_of_docs:
		if freq(word, document) > 0:
		    count += 1
	    return 1 + count


	def idf(word, list_of_docs):
	    return math.log(len(list_of_docs) /
		    float(num_docs_containing(word, list_of_docs)))


	def tf_idf(word, doc, list_of_docs):
	    return (tf(word, doc) * idf(word, list_of_docs))

	for i in range(len(docs)):
		tokens = tokenizer.tokenize(docs[i]["text"])
		tokens = [token for token in tokens if token not in stopwords]
		for token in tokens:
			#The frequency computed for each tip
			docs[i]['freq'][token] = freq(token, tokens)
			#The term-frequency (Normalized Frequency)
			docs[i]['tf'][token] = tf(token, tokens)
			docs[i]['tokens'] = tokens
		vocabulary.append(tokens)

	for doc in docs:
	    for token in docs[doc]['tf']:
		#The Inverse-Document-Frequency
		docs[doc]['idf'][token] = idf(token, vocabulary)
		#The tf-idf
		docs[doc]['tf-idf'][token] = tf_idf(token, docs[doc]['tokens'], vocabulary)'''
def analyze():
	documents=[]
	for i in docs:
		documents.append(docs[i]['text'])
	tfidf_vectorizer = TfidfVectorizer()
	tfidf_matrix = tfidf_vectorizer.fit_transform(documents)
	m,n = tfidf_matrix.shape
	for i in range(m-1):
		cos_sim = cosine_similarity(tfidf_matrix[i:i+1], tfidf_matrix)
		for j in range(len(cos_sim[0])):
			if cos_sim[0][j] > 0.5 and i!=j and docs[i]['reviewerID']==docs[j]['reviewerID']:
				print docs[i]['text']
				print "\nis similar to\n"
				print docs[j]['text']
				

		
