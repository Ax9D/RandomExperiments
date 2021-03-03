'''
A static site crawler

used like this
c=Crawler("https://www.google.com"),maxSites=10000,updateInterval=30)
c.crawl()

It creates an output file with name in the format: <timestamp><site_url>.txt 

maxSites is the maximum no. of sites that the crawler will check
updateInterval is the amount of time the crawler will wait before updating the output file
An updateInterval of 30 means it will update the output file every 30 seconds


I was pretty new to python when I wrote this, so your code reading displeasure is deeply regretted
'''
import requests
from bs4 import BeautifulSoup
import time

class Crawler:
	def __init__(self, starting, maxSites,updateInterval):
		self.sites = []
		self.sites.append(starting)
		self.maxSites = maxSites
		self.startTime=int(time.time())
		self.updateInterval=updateInterval
		self.prevUpdateTime=time.time()
		self.loggedTillIndex=0

		siteName=starting[starting.find("//")+2:]
		siteName=siteName[0:siteName.find('/')]
		self.filePath=str(self.startTime)+siteName+".txt"

	def parseLinks(self, htm):
		soup = BeautifulSoup(htm, 'html.parser')
		a_elems = soup.find_all('a')
		links = []
		for a_elem in a_elems:
			href=a_elem.get('href')
			if(href!=None):
				href=href.strip()
				if(href.find("https")==0 or href.find("http")==0):
					#print(href)
					links.append(href)

		return links

	def isInList(self,s):

		# TODO: Implement effieicntly
		for site in self.sites:
			if(s==site):
				return True
		return False

	def visit(self,addr):
		resp=None
		try:
			resp=requests.get(addr)
		except:
			print("Failed to get:\n"+addr)
			return
		links=self.parseLinks(resp.text)
		for link in links:
			if(not self.isInList(link)):
				print("Found: "+link)
				self.sites.append(link)

	def crawl(self):
		count=0
		while(count<len(self.sites) and len(self.sites)<=self.maxSites):
			curTime=time.time()
			if(curTime-self.prevUpdateTime>=self.updateInterval):
					self.prevUpdateTime=curTime
					self.logToFile()

			self.visit(self.sites[count])
			count=count+1

		if(self.loggedTillIndex<len(self.sites)-1):
			self.logToFile()
		#print(self.sites)

	def logToFile(self):
		print("No. of sites now: "+str(len(self.sites)))
		f=open(self.filePath,'a+')
		numSites=len(self.sites)
		for i in range(self.loggedTillIndex+1,numSites):
				f.write(self.sites[i]+"\n")
		self.loggedTillIndex=numSites-1
		f.close()


c=Crawler("https://"+input("Enter site address:\n"),maxSites=10000,updateInterval=30)
c.crawl()
