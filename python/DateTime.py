szimport os

# you can give the file path with \\ or with \, python will automatically convert it to
# \\
mypath="D:\Python\python"
os.chdir(mypath)
mydir=os.getcwd()
print(mydir)

# list files in a directory
lstdir =os.listdir(mydir)

#join function uses os.sep which is operating system dependent
files = [os.path.join(os.getcwd(), files) for files in lstdir if os.path.isdir(os.path.join(mypath,files))]
print(files)

path = os.path.normpath(mypath)
cpath=path.split(os.sep)
print(cpath)

# file and its extension
for dircont in lstdir:
    ext, file =os.path.splitext(dircont)
    print("file :%s has extension %s" %(ext,file))

os.chdir(mypath)
for root, dirs, files in os.walk(".", topdown = False):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
