#wap to find the greatest of 3 numbers entered by the user

a = int(input("Enter the first number : "))
b = int(input("Enter the second number : "))
c = int(input("Enter the third number : "))

if(a>b and a>c):
    print("the first number is greater number: ")
elif(b>c):
    print("the second number is greater number: ")
elif(c>b):
    print("the third number is greater number: ")
