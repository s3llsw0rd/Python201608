# import the urlopen function from the urllib2 module
from urllib2 import urlopen
# import the BeautifulSoup function from the bs4 module
from bs4 import BeautifulSoup
# import pprint to print things out in a pretty way
import pprint
#import re to use regex
import re
# choose the url to crawl
url = 'http://www.codingdojo.com'
# get the result back with the BeautifulSoup crawler
soup = BeautifulSoup(urlopen(url), 'html.parser')
#print soup.prettify() # print soup to see the result!!
# your code here to find all the links from the result
# and complete the challenges below

'''
#setting up the regex
HTML_LINK = re.compile('<a href="(.+/.+)" .+>')
#setting a variable to contain all matches
all_links = HTML_LINK.search(soup)
'''

#variable setup
unique_href = []
all_href = []
link_dict = {}



for link in soup.find_all('a'):
	all_href.append(link.get('href'))

for ele in all_href:
	if not ele in unique_href:
		if not ele == 'javascript:void(0);':
			unique_href.append(ele)
			link_dict[ele] = 1
	else:
		link_dict[ele] += 1

print link_dict

