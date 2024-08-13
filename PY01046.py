def moveColums(a,b):
    print(a + '->'+b)
def call(n,a,b,c):
    if n == 1: moveColums(a,c)
    else:
        call(n-1,a,c,b)
        moveColums(a,c)
        call(n-1,b,a,c)
n = int(input())
call(n,'A', 'B', 'C')