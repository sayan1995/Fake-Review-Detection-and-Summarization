import detection
import reviewer_ml_parse
import reviewer_ml_main
import os.path
import cosine_similarity
import pandas as pd
import numpy as np
import re
import json

print("1.CellPhones and Accessories")
print("2.Clothes and Accessories")
print("3.Automotive")
print("4.Musical-Instruments")

print "Enter your choice"
dom_choice=int(raw_input())
domain_list=["CellPhones","Clothes&Acc","Automotive","Musical-Instruments"]

print "1.Reviewer Based"
print "2.Review Base"
print "3.Cosine similarity"
print "Enter your choice"
choice=int(raw_input())
if(dom_choice==1):
	domain=domain_list[0]
	if choice==1:
		if os.path.exists("../datasets/ML/"+domain.lower()+"_label.csv"):
			df = pd.read_csv("../datasets/ML/"+domain.lower()+"_label.csv")
			#print(df[df['Label'] == 'FAKE']["ReviewerID"].tolist())
			with open('../datasets/Cell_Phones_and_Accessories_5.json', 'r') as f:
				json_data = f.read()
				list=re.findall(r'(\{.*})',json_data)
				for j in df[df['Label'] == 'FAKE']["ReviewerID"].tolist():
					print j
					for i in list:
						data = json.loads(i)
						if data["reviewerID"]==j:
							print data["reviewText"]
							print ""
					print ""
		else:
			reviewer_ml_parse.parse('../datasets/Cell_Phones_and_Accessories_5.json','../datasets/ML/cellphones.csv') 
			#reviewer_ml_parse
	#object_file = pickle.load(f)

'''elif(dom_choice==2):
	f = open('../datasets/clothes_brands.txt', "r")
	domain=domain_list[1]
elif(dom_choice==3):
	f = open('../datasets/automotive_brands.txt', "r")
	domain=domain_list[2]
elif(dom_choice==4):
	f = open('../datasets/musical_brands.txt', "r")
	domain=domain_list[3]
prod=[]
c=0;
for line in iter(f):
	prod.append(line.split('|')[0])
	print str(c+1)+" . "+line.split('|')[1]+"\n"
	c+=1

print "Enter your choice"
ch=int(raw_input())
ch=ch-1
filePath='../datasets/'+domain+'/'+prod[ch]+'.txt'
detection.parse(filePath,prod[ch])
cosine_similarity.parse(filePath,prod[ch])'''
