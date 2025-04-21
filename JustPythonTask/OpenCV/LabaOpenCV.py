import cv2

# 1. Объединение изображений 
landscape = cv2.imread('hex1.jpg')
portrait = cv2.imread('hex2.jpg')
    
# Изменение размера для совместимости
portrait = cv2.resize(portrait, (landscape.shape[1], landscape.shape[0]))
    
# Объединение изображений
merged = cv2.addWeighted(landscape, 0.5, portrait, 0.5, 0)
       
cv2.imshow('Объединенный!!!', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('merged.jpg', merged)

# 2. Коррекция изображения
img = cv2.imread('hex1.jpg')
    
# Размытие
blurred = cv2.GaussianBlur(img, (15, 15), 0)
    
alpha = 1.5 
beta = 30
adjusted = cv2.convertScaleAbs(img, alpha = alpha, beta = beta)
    
cv2.imshow('Размытый!!!', blurred)
cv2.imshow('Скорректированный!!!', adjusted)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('blurred.jpg', blurred)
cv2.imwrite('adjusted.jpg', adjusted)

# 3. Создание детского изображения
img = cv2.imread('sun.jpg')
    
# Добавление смайлика
smiley = cv2.imread('pixel.png', -1)  # PNG с прозрачностью
x_offset = 50
y_offset = 50
    
# Наложение смайлика
for c in range(0, 3):
    img[ y_offset:y_offset + smiley.shape[0], 
        x_offset:x_offset + smiley.shape[1], c ] = \
        smiley[:, :, c] * ( smiley[:, :, 2] / 255.0 ) + \
        img[y_offset:y_offset + smiley.shape[0], 
            x_offset:x_offset + smiley.shape[1], c] * (1.0 - smiley[:, :, 2] / 255.0)
    
# Добавление мультяшного эффекта
cartoon = cv2.stylization(img, sigma_s = 150, sigma_r = 0.25)
    
cv2.imshow('Детское изображение!!!', cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('kidImage.jpg', cartoon)    