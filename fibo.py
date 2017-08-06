n = int(raw_input('enter n: '))
a,b = 0,1
print a
print b
'''i = 2
while i <= n:
    c = a + b
    print c
    a,b = b,c
    i = i + 1'''
for i in range(2,n):
    c = a + b
    print c
    a,b = b,c 
    
    