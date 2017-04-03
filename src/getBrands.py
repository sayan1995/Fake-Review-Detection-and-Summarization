from glob import glob
from os.path import basename
from lxml import html  
import json
import requests
import json,re
from dateutil import parser as dateparser
from time import sleep
import random
import requests
#import gray_harvest

USER_AGENTS_FILE="../user_agents.txt"
def LoadUserAgents(uafile=USER_AGENTS_FILE):
    """
    uafile : string
        path to text file of user agents, one per line
    """
    uas = []
    with open(uafile, 'rb') as uaf:
        for ua in uaf.readlines():
            if ua:
                uas.append(ua.strip()[1:-1-1])
    random.shuffle(uas)
    return uas

def parsePage(asin):
	#proxy = {"http": "http://104.131.75.65:80"}
	#This script has only been tested with Amazon.com
	amazon_url  = 'http://www.amazon.com/dp/'+asin
	# load user agents and set headers
	uas = LoadUserAgents(uafile="../user_agents.txt")
	ua = random.choice(uas)  # select a random user agent
	headers = {
	    "Connection" : "close",  # another way to cover tracks
	    "User-Agent" : ua}
	page = requests.get(amazon_url,headers = headers).text
	parser = html.fromstring(page)
	XPATH_AGGREGATE_RATING = '//table[@id="histogramTable"]//tr'
	XPATH_PRODUCT_NAME = '//h1//span[@id="productTitle"]//text()'


	raw_product_name = parser.xpath(XPATH_PRODUCT_NAME)
	product_name = ''.join(raw_product_name).strip()
	total_ratings  = parser.xpath(XPATH_AGGREGATE_RATING)
	
	return product_name


def readAsin():
	#Add your own ASINs here 
	doneflag = {}
	with open("../datasets/musical_brands.txt", 'r') as fh:
	    for line in fh:
		doneflag[line.split('|')[0]] = 1

	fh = open("../datasets/musical_brands.txt", 'a')
	extracted_data = {}
	c=0
	for fn in glob('../datasets/Musical-Instruments/*.txt'):
	    product_id = basename(fn).split('.')[0]
	    if product_id in doneflag:
		continue
	    c+=1
	    if(c<10):
		print "Downloading and processing page http://www.amazon.com/dp/"+product_id
	    	extracted_data[product_id]=parsePage(product_id)
	    	fh.write(product_id.encode('utf8') + "|" + extracted_data[product_id].encode('utf8') + "\n")
	    	sleep(2)

if __name__ == '__main__':
	readAsin()
