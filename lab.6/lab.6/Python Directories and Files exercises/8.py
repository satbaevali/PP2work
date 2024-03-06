import os
name_file = input("write file: ")
pathss = r"C:\Users\akim0\Desktop\PP2work\lab.6\lab.6"
paths = os.path.join(pathss, name_file)
try:
    if os.path.exists(paths) and os.access(paths, os.X_OK):
        os.remove(paths)
except:
    print("mistake")