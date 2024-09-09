bb = bytes(range(0x80, 0x100))
str=bb.decode('cp850',errors='replace')
for i in range(len(str)):
    print(str[i], end=' ' if (i+1)%16 else '\n') 