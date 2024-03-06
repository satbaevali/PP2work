import shutil
paths = r"C:\Users\akim0\Desktop\PP2work\lab.6\lab.6\os impoct\aaa.txt"
try:
    shutil.copyfile(paths, r"C:\Users\akim0\Desktop\PP2work\lab.6\lab.6\os impoct\demo.txt")
except:
    print("Ошибка")