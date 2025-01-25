import os

ftrg = open('D:\python\listdir.txt', 'w')
try:
    mydir = 'D:\python'
    mylist = os.listdir(mydir)
    mylist.sort()
    for dirOrFile in mylist:
        if os.path.isdir(mydir + os.sep + dirOrFile):
            print >> ftrg, 'DIRECTORY: %s' % dirOrFile
        else:
            print >> ftrg, 'FILE: %s' % dirOrFile
finally:
    ftrg.close()
