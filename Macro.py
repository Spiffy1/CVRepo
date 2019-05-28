# ==================== Pre Process training image ===============
from scipy import ndimage
from imageio import imread
# from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img

filenames = os.listdir(path + "Cvt")

train_files = []
categories = []

image_width = 128
image_height = 128
channels = 3
nb_classes = 1

# append stringlist to ndarray type
for filename in filenames:
    category = filename.split('.')[0]
    if category == 'dog':
        train_files.append(filename)
        categories.append(1)
    else:
        train_files.append(filename)
        categories.append(0)
    
trainfiles = np.array(train_files)    
category = np.array(categories)    

# ===================== Split Data ===========================
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(trainfiles, category, test_size = .5, random_state = 55)
Save split data to file
np.save ('x_train.npy', x_train)
np.save ('y_train.npy', y_train)
np.save ('x_test.npy', x_test)
np.save ('y_test.npy', y_test)

# ================== put data into dataframe ===================
import cv2
import time

print('Converting images into array')
i = 0
rawdata = []
for file in x_train:
    img = cv2.imread(path + "Cvt/" + file, 0)
    rawdata.append(img.flatten())
    i += 1
    if i % 2500 == 0:
        print("%d images to array" % i)
        
print('Saving progress')
start = time.time()
np.save('dataframe.npy', rawdata)
end = time.time()
print(end - start)

# ====================== Process test data ========================
print('Converting images into array')
i = 0
rawdat = []
for file in x_test:
    img = cv2.imread(path + "Cvt/" + file, 0)
    rawdat.append(img.flatten())
    i += 1
    if i % 2500 == 0:
        print("%d images to array" % i)
        
import time
print('Saving progress')
start = time.time()
# df.to_csv('rawtest.csv', index = False)
np.save('rawtest.npy', rawdat)
end = time.time()
print(end - start)