import math
def PSNR(orgin,new):
    MSE=0
    h=len(orgin)
    w=len(orgin[0])
    for i in range(h):
        for j in range(w):
            MSE+=(int(orgin[i][j])-int(new[i][j]))**2
    MSE=MSE/(h*w)
    return 10*math.log10((255*255)/MSE)
