import os
import shutil
def recursive_walk(folder):
    
    for folderName, subfolders, filenames in os.walk(folder):
        if subfolders:
            for subfolder in subfolders:
                recursive_walk(subfolder)
        #print('\nFolder: ' + folderName + '\n')
        for filename in filenames:
            if filename.endswith('.exe'):
                shutil.copy(folderName+"\\"+filename, dir_dst)
                #print(filename)
unallowed = ['desktop.ini','WindowsApps']
l=os.listdir("C:\\Program Files\\")
dir_src = ("C:\\Program Files\\")
dir_dst = ("C:\\BenignFiles\\")
for i in l:
    if i in unallowed:
        continue
    print('C:\\Program Files\\' +i)
    recursive_walk('C:\\Program Files\\'+i)
