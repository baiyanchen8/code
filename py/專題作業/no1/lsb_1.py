import  cv2
image = cv2.imread('picture/b1.jpg')
# LSB訊息塹入法

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()

height, width, _ = image.shape
a=[1,0,0,1,0,1,0]
k=0
for y in range(height):
    for x in range(width):
        # Get the pixel value
        pixel = image[y, x]
        # change pixel value
        if(k<len(a)):
            if pixel[0]%2==1:
                pixel[0]-=a[k]
            if pixel[0]%2==0:
                pixel[0]+=a[k]
            k+=1
            image[y,x]=pixel
        
cv2.imshow('Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()