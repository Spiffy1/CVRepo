import cv2
im = 'C:/Users/phannt1/Pictures/sdgsdgs.PNG'

image = cv2.imread(im)
imagem = cv2.bitwise_not(image)

cv2.imwrite('any.png', imagem)
# cv2.imshow('any', imagem)
