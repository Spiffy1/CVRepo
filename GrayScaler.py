# ================ Convert to Grayscale =========================
import cv2
path = '/home/username/Downloads/Data/'
newdir = path + 'Cvt/'
# Convert all images
for filename in os.listdir(path + 'Resized'):
    im = cv2.imread('/home/username/Downloads/Data/Resized/' + filename)
    #Convert to GrayScale
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # Reduce Dimension of array
    cv2.imwrite(newdir + filename, gray)
print('Conversion complete...')
