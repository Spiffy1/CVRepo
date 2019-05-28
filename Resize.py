# ============================ Resize ===============================
from PIL import Image
# Choose output folder
path = '/home/username/Downloads/Data/'
newdir = path + 'Resized/'
# Resizing all images
for filename in os.listdir(path + 'train'):
#     print(filename)
    im = Image.open('/home/username/Downloads/Data/train/' + filename)
    imCopy = im.copy()
    resized = imCopy.resize((128,128))
    resized.save(newdir + filename)


