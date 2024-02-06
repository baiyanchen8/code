import  cv2
image = cv2.imread('picture/b1.jpg')



gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

height, width, _ = image.shape
for y in range(height):
    for x in range(width):
        # Get the pixel value
        pixel = image[y, x]
        # change pixel value
        pixel[1]=round(pixel[1])
        pixel[0]=round(pixel[0])
        pixel[2]=round(pixel[2])
        image[y,x]=pixel
        
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()