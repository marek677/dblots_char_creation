import requests
import time
def nick(no):
	a = no-127000
	numbers = {
	'0': "Zero",
	'1': "One",
	'2': "Two",
	'3': "Three",
	'4': "Four",
	'5': "Five",
	'6': "Six",
	'7': "Seven",
	'8': "Eight",
	'9': "Nine"
	}

	nickname = "Mychar"
	for letter in str(a):
		nickname += " "+numbers[letter]
	return nickname
def create(accno, password,name,race):
	link = "http://dblots.org.pl/account.php"
	s = requests.Session()
	
	#login
	try:
		r = s.post(link,data={'account': accno, 'password': password, 'lang':'pl', 's':'classic'})
		#print r.elapsed.total_seconds()
	except:
		print "Error on post!"
		print(r.status_code, r.reason) #HTTP
		return
	with open("output.html","wb") as f:
		f.write(r.text.encode('utf-8').strip())
	#Create character
	try:
		r = s.post(link,data={'name': name, 'race': race, 'lang':'pl', 's':'classic'})
		#print r.elapsed.total_seconds()
	except:
		print "Error on post no2!"
		print(r.status_code, r.reason) #HTTP
		return
	with open("output2.html","wb") as f:
		f.write(r.text.encode('utf-8').strip())
for no in range(127030,127070): #acc number range
	create(str(no),'aaaaaaaa',nick(no),1700) #password here, 1700 is character race - read readme for further information 
	print(nick(no))
	time.sleep(1) # to avoid "ur refreshing site too fast"
