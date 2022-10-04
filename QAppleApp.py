import Config
import Helper
import RandomNumberGenerator
import time

def QAppleRandomColors():
    startTime = time.time()
    #print("-----------------------Start-----------------------")
    #Config.QiskitVersion()
    # just once is good enough
    #Config.SetupQiskit()

    width = 1
    height = 1
    colorBits = Config.rgbBits
    colorDepth = colorBits / Config.singleColorBits

    randomBits = RandomNumberGenerator.GenerateNBitRandomNumber(width, height, colorBits)
    print(randomBits)
    print("Random number generation successful.")

    hash = Helper.StringHash(randomBits)
    print("Hash generation successful: " + hash)

    imageArray = RandomNumberGenerator.StringBitsToIntArray(randomBits, colorBits, width, height)
    print(imageArray)
    print("Uint array generation successful.")

    #1D Array
    oneDimArray = Helper.NDTo1DArray(imageArray)
    print(oneDimArray)
    #Helper.ArrayToImage(hash, imageArray)
    #print("Image generation successful.")

    #print("-----------------------End-----------------------")
    endTime = time.time()
    print("Time taken:" + str(endTime - startTime))

    return oneDimArray, hash