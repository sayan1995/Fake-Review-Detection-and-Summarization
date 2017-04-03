import networkx as nx
from time import sleep
from collections import Counter
from nltk.tokenize.punkt import PunktSentenceTokenizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

debug=False
class Summarization:
	def __init__(self,text):
		self.text=text
		self.text = ' '.join(self.text.strip().split('\n'))
		self.sentence_splitter = PunktSentenceTokenizer()
		self.sentences = self.sentence_splitter.tokenize(text)
		if(debug):
			print "After tokenization.....\n"
			sleep(2)
			print self.sentences
	def bag_of_words(self):
    		self.bag_of_words_matrix = CountVectorizer().fit_transform(self.sentences)
		if(debug):
			print "\n\n"
			sleep(2)
			print "Bag of words matrix.....\n"
			sleep(2)
			print self.bag_of_words_matrix
	
	def normalization(self):
		self.normalized_matrix = TfidfTransformer().fit_transform(self.bag_of_words_matrix)
		self.similarity_graph = self.normalized_matrix * self.normalized_matrix.T
		if(debug):
			print "\n\n"
			sleep(2)
			print "Normalization.....\n"
			sleep(2)
			print self.normalized_matrix
			print "\n\n"
			sleep(2)
			print "Similarity graph.....\n"
			sleep(2)
			print self.similarity_graph			

	def textrank(self):
		self.nx_graph = nx.from_scipy_sparse_matrix(self.similarity_graph)
		self.scores = nx.pagerank(self.nx_graph)
		self.sorted_text = sorted(((self.scores[i],s) for i,s in enumerate(self.sentences)),reverse=True)
		if(debug):
			print "\n\n"
			sleep(2)
			print "Scores.....\n"
			sleep(2)
			print self.sorted_text
		return self.sorted_text
		
	def summarized_text(self):
		self.summary=""
		for i in range(len(self.sorted_text)):
			self.summary+=self.sorted_text[i][1]
		self.summary = ' '.join(self.summary.strip().split('\n'))
		self.summary = ' '.join(self.summary.split())		
		return self.summary

#if __name__ == "__main__":
def summaryGen(fileName,domain,debugging=False):
	global debug
	debug=debugging
	f=open("../datasets/"+domain+"/"+fileName+".txt","r")
	content=f.read()
	print "Before summarization.....\n"
	sleep(2)
	print content
	sleep(2)
	summary = Summarization(content)
	summary.bag_of_words()
	summary.normalization()
	rankedText=summary.textrank()
	summarized=summary.summarized_text()
	if(debug):
		print "\n\n"
		sleep(2)
		print "After summarization.....\n"
		sleep(2)
		print summarized
	else:
		print "After summarization.....\n"
		sleep(2)
		print summarized
	return [rankedText[i][1] for i in range(len(rankedText))]
