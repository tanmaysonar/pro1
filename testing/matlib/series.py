def fibo(n):
    series = ''
    a,b = 0,1
    series = series + str(a) + '\t' + str(b) + '\t'
    for i in range(2,n):
        c = a + b
        series = series + str(c) + '\t'
        a,b = b,c
    return(series)
        
def even(n):
    series = ''
    for i in range(0, n+1,2):
        series = series + str(i) + '\t'

    return(series)