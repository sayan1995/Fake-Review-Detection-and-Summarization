import re
import os
import json
import pandas

with open('../../datasets/Cell_Phones_and_Accessories_5.json', 'r') as f:
	json_data = f.read()
	list=re.findall(r'(\{.*})',json_data)
	path = 'b.csv'
	cols = pandas.read_csv(path, nrows=1).columns
	dataset = pandas.read_csv(path,usecols=cols[-1:])
	reviewers = pandas.read_csv(path,usecols=cols[0:1]).values
	ff = open('../../datasets/ML/fake_cellphones.txt','w+')
	for j in range(len(dataset.values)):
		ff.write(reviewers[j][0]+"\n")
		if dataset.values[j][0]==3:
			for i in list:
				data = json.loads(i)
				if data['reviewerID'] == reviewers[j][0]:
					ff.write("\n\n")
					ff.write(str(data))
					ff.write("\n\n")
	

