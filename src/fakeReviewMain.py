import detection
import cosine_similarity

print("1.CellPhones and Accessories")
print("2.Clothes and Accessories")
print("3.Automotive")
print("4.Musical-Instruments")

print "Enter your choice"
dom_choice=int(raw_input())
domain_list=["CellPhones","Clothes&Acc","Automotive","Musical-Instruments"]
if(dom_choice==1):
	f = open('../datasets/cellphone_brands.txt', "r")
	domain=domain_list[0]
elif(dom_choice==2):
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
cosine_similarity.parse(filePath,prod[ch])
