import  cv2
image = cv2.imread('picture\ghost.png')
# 圖型轉字符
height, width, _ = image.shape
resized_image = cv2.resize(image, (round(width*0.05), round(height*0.05)))
gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)
height, width, _ = resized_image.shape
cv2.imshow('Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
ax= ['.|.', ':|:', ':|:', '+.+', '?.?', '[]',
     '{\}', '.I.', '.X.', '.h.', '.o.', '.w.', 
     '.#.', '.8.', 'S.S', 'F.F', 'M.M', 'T.T',
     'k.k', 'y.y', 'g.g', 'v.v', 'm.m', 'u.u', 'a.a', '@.@']

a=[1,0,0,1,0,1,0]
k=0
f=open('img.txt',"w")
for x in range (height):
    arr=[]
    for y in range(width):
        pixel=gray_image[x,y]
        k=round(pixel/10)
        f.write(ax[k]+'\t')
        arr.append(ax[k])
    f.write('\n')
    for y in range(width):
        f.write(arr[y]+'\t')
    f.write('\n')
    for y in range(width):
        f.write(arr[y]+'\t')
    f.write('\n')
f.close()