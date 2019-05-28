# web scrapping shell script

import os

dir = "/home/user/download/folder"
os.system('cd '+ dir)

os.system('source activate workshop')

words = [1,2,3,4,5,6]

for word in words:
	os.system('googleimagesdownload -k ' + word + ' -l 1000')

