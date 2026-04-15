from fnmatch import *
mask='12*34?5'
for i in range(2025,10**8,2025):
    if fnmatch(str(i),mask):
        print(i,i//2025)