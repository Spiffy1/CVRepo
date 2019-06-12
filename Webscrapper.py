# web scrapping shell script

import os
import sys
import threading
import time

downloadlist = [1,2,3,4,5,6]

def runOsSys(num):
	os.system('googleimagesdownload -k ' + num + ' -l 1000')
i = 0
threads = []

for i in range(len(downloadlist)):
	print(i)
	downloadThread = threading.Thread(target=runOsSys, args=[i])
	threads.append(downloadThread)
	downloadThread.start()