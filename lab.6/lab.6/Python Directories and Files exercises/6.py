import os
paths = r"C:\Users\akim0\Desktop\PP2work\lab.6\lab.6\Python Directories and Files exercises\os impoct"
for i in range(26):
    name_file = chr(65 + i)
    x = os.path.join(paths, name_file)
    os.mkdir(x)