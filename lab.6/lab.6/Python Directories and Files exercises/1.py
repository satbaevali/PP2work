import os

path = r'C:\Users\akim0\Desktop\PP2work\lab.6\lab.6\Python Directories and Files exercises'
list_contents = os.listdir(path)

#directories
print("Directories:")
for item in list_contents:
    if os.path.isdir(os.path.join(path, item)):
        print(f" - {item}")

#files
print("\nFiles:")
for item in list_contents:
    if os.path.isfile(os.path.join(path, item)):
        print(f" - {item}")
