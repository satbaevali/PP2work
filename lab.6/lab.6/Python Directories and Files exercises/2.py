import os 
paths=r"C:\Users\akim0\Desktop\PP2work\lab.6\lab.6\Python Directories and Files exercises"
# os.R_OK для проверки чтения,
print(os.access(paths, os.R_OK))
#os.W_OK для записи
print(os.access(paths, os.W_OK))
#os.X_OK для исполнения
print(os.access(paths, os.X_OK))