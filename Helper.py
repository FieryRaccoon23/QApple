import hashlib
import numpy as np
#from PIL import Image

#2D Array allowed only
def ArrayToHash(arr):
    ret = ''
    randomStr = 'UYugOpyuXB'
    for parent in arr:
        for idx, val in enumerate(parent):
            ret = ret + str(val) + randomStr

    return hashlib.md5(ret.encode('utf-8')).hexdigest()

def StringHash(string):
    return hashlib.md5(string.encode('utf-8')).hexdigest()

#2D Array to Image
""" def ArrayToPNG(arr, width, height, file):
    arrVals = np.array(arr).astype(np.uint32)
    RGB= np.zeros((height,width,3),dtype=np.uint8)
    RGB[:,:,0] = arrVals>>16            # Take red from top
    RGB[:,:,1] = (arrVals>>8) & 0xff    # Take green from middle
    RGB[:,:,2] = arrVals & 0xff         # Take blue from bottom
    pIm = Image.fromarray(RGB).save(file + ".png")

def ImageToArray(imgLoc):
    img = Image.open(imgLoc)
    np_im = np.array(img)
    print (np_im)

def ArrayToImage(imgName, imgArray):
    Image.fromarray(imgArray).save(imgName + ".png") """

def NDTo1DArray(array):
    return np.reshape(array, (1,np.product(array.shape)))