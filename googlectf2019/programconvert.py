import time

ifs=0
def load(p,i):
	varName=ACC[p[i+1]]
	i+=2
	num=''
	while(p[i]!='✋'):
		num+=NUMS[p[i]]
		i=i+1
	return "load "+str(num)+" to "+varName , i+1

def if_zero(p,i):
	global ifs
	ifs+=1
	return "ifzero",i+1
	
def if_not_zero(p,i):
	global ifs
	ifs=ifs+1
	return "if_not_zero",i+1
	
def endif(p,i):
	global ifs
	ifs-=1
	return "endif",i+1

def jump_to(p,i):
	toLabel=p[i+1][1:]
	return "jump_to "+toLabel,i+2
	
def jump_top(p,i):
	return "jump_top ",i+1

def pop(p,i):
	varName=ACC[p[i+1]]
	return "Pop to "+varName,i+2
def pop_out(p,i):
	return "Pop ",i+1
def print_top(p,i):
	return "print_top ",i+1
def push(p,i):
	varName=ACC[p[i+1]]
	return "Push from "+varName,i+2

NUMS={
      '1️⃣ '.strip():'1',
      '2️⃣ '.strip():'2',
      '3️⃣ '.strip():'3',
      '4️⃣ '.strip():'4',
      '5️⃣ '.strip():'5',
      '6️⃣ '.strip():'6',
      '7️⃣ '.strip():'7',
      '8️⃣ '.strip():'8',
      '9️⃣ '.strip():'9',
      '0️⃣ '.strip():'0'}
ACC={
      '🥇' : 'var1',
      '🥈' : 'var2'}
SYMBOLS={
		'🍡': lambda p,i: ('add ',i+1) ,
      '🤡': lambda p,i:('clone ',i+1) ,
      '📐': lambda p,i: ('divide ',i+1),
      '😲': if_zero,
      '😄': if_not_zero,
      '🏀': jump_to,
      '🚛': load,
      '📬': lambda p,i: ('modulo ',i+1),
      '⭐': lambda p,i: ('multiply ',i+1),
      '🍿': pop,
      '📤': pop_out,
      '🎤': print_top,
      '📥': push,
      '🔪': lambda p,i: ('sub ',i+1),
      '🌓': lambda p,i: ('xor ',i+1),
      '⛰': jump_top,
      '⌛': lambda p,i: ('exit ',i+1),
    	  '🖋': lambda p,i: ('--------\n'+p[i]+'\n-------- ',i+1),
    	  '😐':endif
      }
code_sections={}

	
p=open('program1').read().split()
hr=""
ip=0
while(ip<len(p)):
	conv,nextI=SYMBOLS[p[ip][0]](p,ip)
	print(conv)
	hr+=conv+"\n"
	
	ip=nextI
	
open('hrprogram','w+').write(hr)
