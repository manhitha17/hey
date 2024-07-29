def factorial(n):
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
    
def fibonacci(n):
    if(n<=0):
        return "positive no"
    elif(n==1):
        return 0
    elif(n==2):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
    
a=int(input('Enter'))
b=int(input('Enter'))
sum=a+b
print(sum)