import os
def parse(reviewFile,prodId):
	directory="../datasets/reviews"
	if not os.path.exists(directory):
		os.makedirs(directory)
	f = open(reviewFile,"r")
	reviews = f.read()
	reviewList = reviews.split("\n\n");
	for i in range(len(reviewList)):
		if(len(reviewList[i])!=0):
			filePath="../datasets/reviews/"+str(i+1)+".txt"
			fwrite = open(filePath,"w+")
			fwrite.write(reviewList[i])
			fwrite.close()

