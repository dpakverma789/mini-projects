import os
from itertools import product
from datetime import datetime,date
import datetime
try:
	from playsound import playsound
	import zipfile
except ModuleNotFoundError:
	for pack in ('playsound', 'zipfile'):
		os.system('pip install {pack}'.format(pack=pack))
	from playsound import playsound
	import zipfile


# chars = list(string.printable)

chars = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
		 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L','M', 'N','O', 'P',
		 'Q','R','S','T','U','V','W','X','Y','Z','@', '#', '$', '%', '&', '*','0','1','2','3','4','5','6','7','8','9')

path = os.getcwd()
zip_file = "/home/lenovo/Downloads/test.zip"
# ZipFile object initialised
zf = zipfile.ZipFile(zip_file)


# Time Function
def date_diff_in_Seconds(dt2, dt1):
	timedelta = dt2 - dt1
	return timedelta.days * 24 * 3600 + timedelta.seconds


# Attack Function
def brute_force(count):
	for attack in product(chars, repeat=count):
		attack = ''.join(attack)
		try:
			zf.setpassword(attack.encode('utf-8'))
			zf.extractall()
			with open('wordlist.txt', 'a+') as wordlist:
				wordlist.write(attack)
				wordlist.write('\n')
			date2 = date.today()
			print('\nDone!!\nYour PassWord is: ', attack)
			playsound(os.path.join(path, 'tone_alert.mp3'))
			return date2
		except:
			continue
	count += 1
	return brute_force(count)


print('\nAttacking on Password...')
date1 = date.today()
try:
	wordlist = open('wordlist.txt', 'r+')
	wordlist = wordlist.readlines()
	for word in wordlist:
		try:
			word = word.strip()
			zf.setpassword(word.encode('utf-8'))
			zf.extractall()
			print('\nDone!!\nYour PassWord is: ',word)
			date2 = date.today()
			playsound(os.path.join(path, 'tone_alert.mp3'))
		except Exception as e:
			continue
	date2 = brute_force(count=7)
except:
	date2 = brute_force(count=7)
# time_in_sec = date_diff_in_Seconds(date2, date1)
# time_formate = 'seconds'
# if time_in_sec > 60:
# 	time_formate = 'minutes'
# 	time_in_sec = time_in_sec/60
# 	if time_in_sec > 60:
# 		time_formate = 'hours'
# 		time_in_sec = time_in_sec/60
# print('It took %0.2f %s to crack this password'%(time_in_sec,time_formate))

