#import series
from testing.matlib.series import fibo, even
import testing.matlib.math_ops as mo
import math

print math.pi 

while True:
    print '1. Fibo Series'
    print '2. Even Series'
    print '3. Even or Odd'
    print '4. Exit'
    
    choice = int(raw_input('What is your choice: '))
    if choice != 4:
    	n = int(raw_input('Enter the value of N: '))
    
    if choice == 1:
        print fibo(n)
    elif choice == 2:
        print even(n)
    elif choice == 3:
        if mo.evenodd(n):
        	print 'is even'
        else:
        	print 'is odd'
    else:
        break


#add python path to the modules
        

    