import requests
import bs4


base_url="http://emoji-t0anaxnr3nacpt4na.web.ctfcompetition.com"
already_visited={'':0}
lk=['']
def getLinks(siteText):
	nls=[]
	for l in bs4.BeautifulSoup(siteText,features="html5lib").findAll('a',href=True):
		x=l['href']
		#print(x)
		if(already_visited.get(x,None)==None):
			already_visited[x]=0
			nls.append(x)
	return nls
	
def downloadImages(sT):
	for img in bs4.BeautifulSoup(sT,features="html5lib").findAll('img',src=True):
		path=img['src']
		bs=requests.get(base_url+"/"+path,stream=True).raw.read()
		name=path[path.rindex('/')+1:]
		print("Downloaded ",name)
		open("catpics/"+name,'wb+').write(bs)
		

def solve():
	global lk
	fullText=""
	while(len(lk)!=0):
		new_links=[]
		for link in lk:
			sT=requests.get(base_url+'/'+link).text
			fullText+=sT
			#print(sT)
			downloadImages(sT)
			ss=sT.find('flag')
			if(ss>0):
				print(sT[ss:50])
				break
			else:
				new_links.extend(getLinks(sT))
		lk=new_links
	print(len(already_visited))
	open('fT.txt','w+').write(fullText)
solve()
