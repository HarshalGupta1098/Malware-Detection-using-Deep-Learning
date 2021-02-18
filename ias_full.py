import numpy as np
from PIL import Image
import sys
import glob
import errno
import os 
result=[]
temp1=np.zeros((256,256))
image = np.zeros((256,256))
i,j,p=0,0,0
path = "C:/Users/admin/Project IAS/Module1/data1/" ## Absolute path for the database.
dirs = os.listdir( path ) ## gets all the directories in the given folder.
path2 = "C:/Users/admin/Project IAS/Module1/image256/" ## Absolute path for storing 256x256 image.
path3 = "C:/Users/admin/Project IAS/Module1/image36/"  ## Absolute path for storing 36x36 image.
for fil in dirs:
    image = np.zeros((256,256))
    with open(path+fil, "rb") as f: ## read byte mode
        byte = f.read(1)  ## reading 1 byte at a time. returns a byte object.
        i,j,p=0,0,0
        print(fil)
        #print (byte)
        while byte != b"": ## itereating till the end of the file
            # print (ord(byte),byte) ## ord gives ASCII value of that char.
            if(i<256):
                if(byte.decode("utf-8")==' ' or byte.decode("utf-8")=='\r' or byte.decode("utf-8")=='\n' or byte.decode("utf-8")=='?' ):
                    byte = f.read(1)
                    continue
                # image[i][p]=0
                #print (byte.decode("utf-8"),int(byte.decode("utf-8"),16),i)
                if(j>8):
                    image[i][p]= int(byte.decode("utf-8"),16) ## byte.decode gives the value of the byte object which is converted into hexa-decimal.
                    p=p+1
                j=j+1
                if(p>255):
                    p=0
                    j=0
                    i=i+1
            byte = f.read(1)
        a=np.matrix(image)
        # a=np.matrix(image)
        print (a)
        result.append(np.array_equal(temp1,a))
        temp1=a
        img = Image.fromarray(image, 'L') ## makes 2D array into an image. L-> The kind of pixel (8-bit pixel black and white)
        #img.show()
        img.save(path2+fil[0:-6]+".bmp")
        img = img.resize((36,36),Image.ANTIALIAS)
        img.save(path3+fil[0:-6]+".bmp")
        #img.show()
print (result)



# with open('C:/Users/admin/Project IAS/data/sample/0fHVZKeTE6iRb1PIQ4au.bytes', 'r') as file1:
#     print(file1.read())
# import pandas as pd
# df = pd.read_csv("C:/Users/admin/Project IAS/data/sample/0fHVZKeTE6iRb1PIQ4au.bytes")
# print(df.drop([0]))
# with open('C:/Users/admin/Project IAS/data/sample/0gDsIvrylX5fPbG7cSBn.bytes', 'r') as file2:
#     print(file2.read())
'''
#same.discard('\n')

# with open('some_output_file.txt', 'w') as file_out:
#     for line in same:
#         file_out.write(line)

with open("apt1/APT1/VirusShare_00dbb9e1c09dbdafb360f3163ba5a3de.json", "rb") as f:
    byte = f.read(1)
    while byte:
        #print ord(byte)
        if(i<256):
            image[i][j]=ord(byte)
            j=j+1
            if(j>255):
                j=0
                i=i+1
        byte = f.read(1)

print(np.matrix(image))
img = Image.fromarray(image, 'L')
img.show()
img = img.resize((36,36),Image.ANTIALIAS)
img.show()

'''
