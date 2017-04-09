import re
import os
import json
import gzip
import pickle
import os.path

def parse(path):
	g = gzip.open(path, 'r')
	brands = {}
	for l in g:
		json_data = json.dumps(eval(l))
		data = re.match(r'(\{.*})',json_data)
		json_obj = json.loads(data.group())
		prod = {}
		if "brand" in json_obj and json_obj["brand"]!="" and "title" in json_obj and os.path.exists("../datasets/CellPhones/"+json_obj["asin"]+".txt"):
			prod[json_obj["title"]] = json_obj["asin"]
			if json_obj["brand"] not in brands:
				brands[json_obj["brand"]] = []
			brands[json_obj["brand"]].append(prod)
			#yield json_obj["asin"]+"|"+json_obj["brand"]+"|"+json_obj["title"]

	filehandler = open("../datasets/Brands/cellphones.pickle","wb")
	pickle.dump(brands,filehandler)		
			
parse("../datasets/Brands/meta_Cell_Phones_and_Accessories.json.gz")

'''f = open("../datasets/Brands/cellphones_brands.txt", 'w')
for l in parse("../datasets/Brands/meta_Cell_Phones_and_Accessories.json.gz"):
	f.write(l + '\n')'''
  

'''with open('../datasets/meta_Musical_Instruments.json', 'r') as f:
	json_data = f.read()
	list=re.findall(r'(\{.*})',json_data)
	print list[0]
	for i in list:	
		filename = '../datasets/Musical-Instruments/brands_musical.txt'
		print i
		if os.path.exists(filename):
			ff = open(filename,"w+")
			ff.write(i["asin"]+"|"+i["title"])'''


