import os

ouput = os.popen('dir')
print(tuple(ouput))