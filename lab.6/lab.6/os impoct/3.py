import os
paths = r"C:\Users\noutstorekz\Desktop\githowto\repositories\work\lab6"
for root, directories, files in os.walk(paths):
    print(root)
    for directory in directories:
        print(directory)
    for file in files:
        print(file)
# os.R_OK для проверки чтения,
print(os.access(paths, os.R_OK))
#os.W_OK для записи
print(os.access(paths, os.W_OK))
#os.X_OK для исполнения
print(os.access(paths, os.X_OK))