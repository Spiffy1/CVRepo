import os 

path = os.path.join('C:\Users\account\Desktop\Test')


filenames = os.listdir(path)

for filename in filenames:
	os.rename(filename, path + 'filename'+ '.png')
