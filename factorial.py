
# Write your code here :-)
def factorial(x):
    if x==1:
        return 1
    else:
        return x*factorial(x-1)


x = int(input("enter number: "))
answer=factorial(x)

print (answer)


