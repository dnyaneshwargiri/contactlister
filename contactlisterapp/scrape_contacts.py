import re
import requests
import array
#import httplib.client
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class scrape_contact:
	finalemails =["" for x in range(300)]
	def accept_url(self,url):
			
			regex = re.compile(
					r'^(?:http|ftp)s?://' # http:// or https://
					r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' #domain...
					r'localhost|' #localhost...
					r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
					r'(?::\d+)?' # optional port
					r'(?:/?|[/?]\S+)$', re.IGNORECASE)
			if re.match(regex, url) is not None :
				  print ("valid url")
				  return True
				  
	def scrape_emails(self,url):
		del self.finalemails[:]
		if url  :
			headers = {'User-Agent': 'Mozilla/5.0'}
			
			try:
				s = requests.Session()
				s.max_redirects = 100000
				s.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36'
				r = s.get(url)
			except requests.exceptions.ConnectionError as e: 
				return 0
			soup = BeautifulSoup(r.content, 'html5lib')
			for a in soup.find_all('a', href=True):
						if a.has_attr('href'):
							link = a['href']
							if link.startswith(url):
									headers = {'User-Agent': 'Mozilla/5.0'}
									r = requests.get(link, headers=headers)
									soup = BeautifulSoup(r.content, 'html5lib')
									data = soup. findAll(text=True)
									data=str (data)
									
									temp_emails= re.findall(r'[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+', data,re.I)
									for te in temp_emails:
										if str(te) !='name@email.com':
											te=str(te)
											self.finalemails.append(te)
		
		return self.finalemails

'''sc=scrape_contact()
sc.scrape_emails('https://cits.uwex.uwc.edu/');		

for e in sc.finalemails	:
	if e:
		print(e)
		
'''	
			    
			
