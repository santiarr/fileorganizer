#import necessary modules
import shutil
import os
import platform

#Identify the folders you want to organize
paths = ['downloads', 'documents']

#Name the folders in which the files will be place and what filetypes they will have
foldersExt = {'Zips': '.zip',
              'Docs': ['.doc', '.txt', '.docx'],
              'EXEs': '.exe.',
              'PDFs': '.pdf',
              'Images': ['.jpg', '.png', '.mp4']
              }

#Create the folders if they don't already exist

for folder in foldersExt:
    for path in paths:
        if platform.system() == 'Windows':
            if os.path.isdir('C:/Users/santi/{path}/{fname}'.format(fname=folder, path=path)) is not True:
                os.mkdir('C:/Users/santi/{path}/{fname}'.format(fname=folder, path=path))
        elif platform.system() == 'Darwin':
            if os.path.isdir('C:/Users/santi/{path}/{fname}'.format(fname=folder, path=path)) is not True:
                os.mkdir('C:/Users/santi/{path}/{fname}'.format(fname=folder, path=path))


#Loop through the files in a specified path and identify what kind of file they are
#Place files in their respective folders
i = 0
for path in paths:
    if platform.system() == 'Windows':
        src = 'C:/Users/santi/'
        init = 'C:/Users/santi/'
    elif platform.system() == 'Darwin':
        src = '/Users/santi/'
        init = '/Users/santi/'
    init += paths[i]
    i += 1
    for file in os.listdir(init):
        for folderName in foldersExt:
            for num in range(len(foldersExt[folderName])):
                if file.endswith(foldersExt[folderName][num]):
                    try:
                        shutil.move(src + '{path}/{file}'.format(path=paths[i - 1], file=file),
                                    src + '{path}/{folder}'.format(path=paths[i - 1], folder=folderName))
                        break
                    except shutil.Error:
                        pass
                    except FileNotFoundError:
                        pass







