import requests
import bs4
import hashlib

already_visited={'':0}
lk=['https://www.google.com/search?biw=1222&bih=636&tbm=isch&sa=1&ei=FrzqXfDYMYLgrQHp2KKYDQ&q=blender+art']

img_folder='test'
def getLinks(siteText,link):
	nls=[]
	for l in bs4.BeautifulSoup(siteText,features="html5lib").findAll('a',href=True):
		x=l['href']
		if(x.find('http')<0):
			x=link+x
		print(x)
		if(already_visited.get(x,None)==None):
			already_visited[x]=0
			nls.append(x)
	return nls
	
def downloadImages(sT,l):
	for img in bs4.BeautifulSoup(sT,features="html5lib").findAll('img'):
		print(img)
		if(img.get('src')!=None):
			path=img['src']
			if(path.find('http')<0):
				path=l+path
			bs=requests.get(path,stream=True).raw.read()
			#name=path[path.rindex('/')+1:]
			name=hashlib.md5(path[path.rindex('/')+1:].encode()).hexdigest()
			print("Downloaded ",name)
			open(img_folder+"/"+name,'wb+').write(bs)
		

def solve():
	global lk
	fullText=""
	while(len(lk)!=0):
		new_links=[]
		for link in lk:
			sT=requests.get(link,headers={'User-Agent' : 'Mozilla/5.0 (X11 Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}).text
			fullText+=sT
			#print(sT)
			downloadImages(sT,link)
			new_links.extend(getLinks(sT,link))
		lk=new_links
	print(len(already_visited))
	open('fT.txt','w+').write(fullText)
solve()
