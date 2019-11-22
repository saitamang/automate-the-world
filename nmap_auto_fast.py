# /usr/bin/python3

import os
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import re

cb6462b1997e6e59ae9c0c40c41963c6 = ""
p9200624cec713b07939b438a1faaefe8 = []

def a75b59e37ddaead95524079cb557a273(cb6462b1997e6e59ae9c0c40c41963c6):
	p7c36de502f4aa5d7a5fb2292243a2aa9 = os.getcwd()
	p1dd8f006837f1230e42dc6e79e27215c = p7c36de502f4aa5d7a5fb2292243a2aa9+'/'+d656c603994e747a4a39010356a737bb
	a2571565ecf98e6d43f0536c7240880e = pd.read_excel (r''+p1dd8f006837f1230e42dc6e79e27215c+'')
	df = pd.DataFrame(a2571565ecf98e6d43f0536c7240880e)
	cb6462b1997e6e59ae9c0c40c41963c6 = df['IP']
	n35cd13d3378ad23720e4956a9766142d(cb6462b1997e6e59ae9c0c40c41963c6)
	return 0
	
def n35cd13d3378ad23720e4956a9766142d(cb6462b1997e6e59ae9c0c40c41963c6):
	for i in range(len(cb6462b1997e6e59ae9c0c40c41963c6)):
		os.system('nmap -p- -T4 -oN '+cb6462b1997e6e59ae9c0c40c41963c6[i]+'_normal.txt '+cb6462b1997e6e59ae9c0c40c41963c6[i])
	r615066f414b57a28337484938a0128bb(cb6462b1997e6e59ae9c0c40c41963c6)

def r615066f414b57a28337484938a0128bb(cb6462b1997e6e59ae9c0c40c41963c6):
	for i in range(len(cb6462b1997e6e59ae9c0c40c41963c6)):
		f=open(cb6462b1997e6e59ae9c0c40c41963c6[i]+'_normal.txt', 'r').read()
		p9200624cec713b07939b438a1faaefe8=re.findall(r"([0-9]*)\/tcp *open *[a-z-?]* *[a-zA-Z0-9. -]*", f)
		n573f6f9940c44f8211f30b83c65fe21c(cb6462b1997e6e59ae9c0c40c41963c6[i], p9200624cec713b07939b438a1faaefe8)
		
def n573f6f9940c44f8211f30b83c65fe21c(cb6462b1997e6e59ae9c0c40c41963c6, p9200624cec713b07939b438a1faaefe8):
	print("\nAdvance scanning for IP "+cb6462b1997e6e59ae9c0c40c41963c6+"\n")
	p9bb5744bc999ca80dce675af6440f4e1 = ','.join(p9200624cec713b07939b438a1faaefe8)
	s87ed9fbf4288a3bebf159694b4b1ea5e = 'nmap -p '+p9bb5744bc999ca80dce675af6440f4e1+' -sC -sV -oA '+cb6462b1997e6e59ae9c0c40c41963c6+'_adv '+cb6462b1997e6e59ae9c0c40c41963c6
	print(s87ed9fbf4288a3bebf159694b4b1ea5e+"\n")
	os.system(s87ed9fbf4288a3bebf159694b4b1ea5e)
	print("\n##############  Done Scanning Setup  ##############\n")
	print("##############  Check out my github : https://github.com/saitamang  ##############\n")

if __name__ == "__main__":
	print("   _____       _ __                                   ")
	print("  / ___/____ _(_) /_____ _____ ___  ____ _____  ____ _")
	print("  \__ \/ __ `/ / __/ __ `/ __ `__ \/ __ `/ __ \/ __ `/")
	print(" ___/ / /_/ / / /_/ /_/ / / / / / / /_/ / / / / /_/ / ")
	print("/____/\__,_/_/\__/\__,_/_/ /_/ /_/\__,_/_/ /_/\__, /  ")
	print("                                             /____/   \n\n")

	print("Welcome to nmap automation script by Saitamang\n")
	
	d656c603994e747a4a39010356a737bb = input("Enter fullname of the excel filename :\n")
	if ".xlsx" in d656c603994e747a4a39010356a737bb:
		print("File name is :"+ d656c603994e747a4a39010356a737bb+"\n")
	else:
		d656c603994e747a4a39010356a737bb = d656c603994e747a4a39010356a737bb+".xlsx"
		print("File name is :"+ d656c603994e747a4a39010356a737bb+"\n")
	
	a75b59e37ddaead95524079cb557a273(cb6462b1997e6e59ae9c0c40c41963c6)

