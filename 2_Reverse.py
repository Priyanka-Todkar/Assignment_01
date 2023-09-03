#Write a Python program that accepts a word from the user and reverse it.
#Sample Test Case
#Input : Edyoda
#output: adoydE

str = input("Enter a string :")
for i in range(len(str) -1, -1, -1):
    print(str[i], end ="")
    
    