import requests
import math

url="http://drivetothetarget.web.ctfcompetition.com"
token="&token=gAAAAABdTXqB_-Q1-C-Bmh4zG3QzlUWKsFmxfnImRcmmaL2vjSh7p_Y36e8BnD_9tMOVI74SplaZIeTXu-FXjlG0SeT6Dnq3t1MvjX5svZnxJo8UUOi6JTenFgrEtcfZDlxRxYHmibkh"
start_lat=51.6487
start_lon=0.0993

#def to_cords(theta,rad):
	

def checkOutcome(lat,lon):
	site=requests.get(url+"/?lat="+str(lat)+"&lon="+str(lon)+token).text
	resStart=site.find("You went")
	resEnd=site.find("<",resStart)
	res=site[resStart:resEnd]
	if(resStart>0):
		dist=res[res.index('went')+4:res.index('m')]
		vel=res[res.index('of')+2:res.index('km/h')]
		direction=True if res[res.rindex(' ')+1:]=='closer…' else False
		print(dist,vel,direction)
		return [dist,vel,direction]
	else:
		print(site)
		
def sweep():
	theta=0
	k=0.001
	prevdc=False
	tdir=0.1
	while(theta<=6.28):
		print(theta*180/math.pi)
		d,v,dc=checkOutcome( start_lat+k*math.cos(theta) , start_lon+k*math.sin(theta) )
		if(prevdc==True and dc==False):
			tdir=-tdir*1.01
			k+=0.001
		if(prevdc==False and dc==True):
			tdir=tdir*1.01
			k+=0.001
		theta+=tdir
		prevdc=dc
sweep()
