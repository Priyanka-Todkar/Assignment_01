# The Fibonacci Sequence is the series of numbers :

#0, 1, 1, 2, 3, 5, 8, 13, 21, ....

#Every next number is found by adding up the two numbers before it.

#Expected Output : 1 1 2 3 5 8 13 21 34
num = 10
num1 = 0
num2 = 1
count = 2
if num< 0:
    print("Enter only +ve value")
elif num == 1:
    print(num1)
else:
    print(num1, end=" ")
    print(num2, end=" ")
 
while count < num:
    num3 =num1 + num2
    print(num3,end=" ")
    count += 1
    num1 = num2
    num2 = num3




