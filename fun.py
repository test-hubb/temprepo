import os 
k=os.popen("ifconfig").read()
print(k)
l=os.popen("ls -l").read()
print(l)
m=os.popen("git --version").read()
print(m)
j=os.popen("hostname").read()
print(j)
print(m)
