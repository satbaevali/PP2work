import os
path=r"C:\Users\akim0\Desktop\PP2work\lab.6\lab.6\os impoct"
try:
    if os.path.exists(path):
        x,y=os.path.split(path)
        print("path -")
        print(x)
        print(y)
except:
    print("its false")
    