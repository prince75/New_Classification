#!usr/bin/python
import urllib2  
from bs4 import BeautifulSoup 
import csv
urls = []
hdr = {'User-Agent':'Mozilla/5.0','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
for i in range(1,100):
	urls.append('http://economictimes.indiatimes.com/industry/media/entertainment/articlelist/msid-13357410,page-' + str(i) + '.cms')

columns = ['Heading', 'Link', 'Summary','Date']
csv_file=open('Eco_Entertainment.csv', 'w')
writer = csv.writer(csv_file)
writer.writerow(columns)


#page = urllib2.urlopen(req)
for url in urls:
	try: 
		req = urllib2.Request(url,headers= hdr)
		page = urllib2.urlopen(req)
	except urllib2.URLError:
		print 'Error in URL ' + url
	soup = BeautifulSoup(page, 'html.parser') 
	contents = soup.find('section', attrs = {'id':'pageContent'})
	a = contents.findAll('div',attrs = {'class' : 'eachStory'})
        #print len(a)
	#print contents.prettify()
	lobbying = {}
	for ele in a:
		try:
			heading_link = ele.find('h3') 
			heading = str(heading_link.text.strip().encode("utf-8"))
			lobbying[heading] = {}

	    		lobbying[heading]['Link'] = 'http://economictimes.indiatimes.com' + ele.a['href']
			print heading
			date_l = ele.find('time', attrs={'class': 'date-format'}) 
			lobbying[heading]['Date'] = date_l.text.strip()
			lobbying[heading]['Summary'] = str(ele.p.get_text().encode("utf-8"))
			#print("------------------------------------")
			#print(ele.prettify()) 
                except AttributeError:
			print 'Attribute error occured'
			del lobbying[heading]	
                 	continue       
	for item in lobbying:         
	      	 writer.writerow([item,lobbying[item]['Link'], lobbying[item]['Summary'],lobbying[item]['Date']])	
	

	
		







