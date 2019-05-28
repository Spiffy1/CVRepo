from PIL import Image
import os
i = 1

# cwd = os.getcwd()
# print(cwd)

# path = (r'C:/Users/phannt1/Desktop/Work Space/Login/JPEG')
path = os.path.join(r"C:/Users/path/to/your/JPEG" )

filenames = os.listdir(path)
print('list', filenames)
print('path is', path)

for filename in filenames:
	print('filename is: ', filename)
	im = Image.open(filename)
	im.save(filename, "PNG")
	i += 1

