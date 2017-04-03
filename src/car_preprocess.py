import re

rating_class = {
    '1.0': 'negative',
    '2.0': 'negative',
    '3.0': 'neutral',
    '4.0': 'positive',
    '5.0': 'positive',
}
brands = {}
with open("../datasets/"
        +"musical_brands.txt", 'r') as fh:
    for line in fh:
        line = line.rstrip()
        (product, brand) = line.split("|", 1)
        brands[product] = brand
#print brands

fout = open("../datasets/musical_instruments_preprocessed.txt", 'w+')
user_id = ""
rating = ""
for k,v in brands.items():
    fin = open("../datasets/Musical-Instruments/"+k+".txt")
    for line in fin:
    	brand = re.sub(" ", "_", brands[k])
	if line.split(":")[0]=="reviewerID":
	    user_id = line.split(":")[1].split(".")[0] 
	elif line.split(":")[0]=="score":
            rating = line.split(":")[1].split(".")[0]+"."+line.split(":")[1].split(".")[1] 
	fout.write(k +" " + brand + " " + user_id + " " + rating_class[rating] +"\n")
	

