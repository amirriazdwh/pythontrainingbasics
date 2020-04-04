from subprocess import Popen,PIPE,STDOUT,call

proc=Popen('dir', shell=True, stdout=PIPE, )
output=proc.communicate()[0]
print(str(output))
