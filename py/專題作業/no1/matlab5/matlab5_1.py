import  cv2
image = cv2.imread('picture\Lena.png')
# 圖型轉字符
height, width, _ = image.shape
resized_image = cv2.resize(image, (82,82))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
height, width, _ = resized_image.shape
cv2.imshow('Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()


ax= ['@','Q','O','w','v','7',':','.']
a=[31,63,95,127,159,191,223,255]
k=0
f=open('matlab5/img.txt',"w")
for x in range (height):
    arr=[]
    for y in range(width):
        k=0
        pixel=gray_image[x,y]
        while pixel>a[k]:
            k+=1
        f.write(''+ax[k]+' ')
        arr.append(ax[k])
    f.write('\n')
f.close()