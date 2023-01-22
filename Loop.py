# 1. Write a Python program to find those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included).
n1 = []
for i in range(1500,2701):
    if (i % 7 == 0) and (i % 5 == 0):
        n1.append(i)
print(n1)
# 2. Write a Python program to convert temperatures to and from celsius, fahrenheit.
# 3. Write a Python program to guess a number between 1 to 9.
"""
import random
target_num, guess_num = random.randint(1,10),0
while target_num != guess_num:
    guess_num = int(input('Guess a number between 1 to 10 until you get right : '))
print('Well guessed')

"""

# 4. Write a Python program to construct the following pattern, using a nested for loop.
n = 5
for i in range(n):
    for j in range(i):
        print('* ',end="")
    print('')

for i in range(n,0,-1):
    for j in range(i):
        print('* ',end = "")
    print()
# 5. Write a Python program that accepts a word from the user and reverse it.
"""
word = input('Enter the reverse it : ')
for i in range(len(word)-1,-1,-1):
    print(word[i],end="")
"""
# 7. Write a Python program that prints each item and its corresponding type from the following list.
datalist = [1452, 11.23, 1+2j, True, 'w3resource', (0, -1), [5, 12],
{"class":'V', "section":'A'}]
for item in datalist:
    print('Type of',item, "is",type(item))
# 8. Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if i == 3  or i ==6:
        continue
    print(i,end=" ")
# 9. Write a Python program to get the Fibonacci series between 0 to 50.
x, y = 0,1
while y<50:
    print(y)
    x,y = y,(x+y)
# 12. Write a Python program that accepts a sequence of lines (blank line to terminate) as input and prints the lines as output (all characters in lower case).
#14. Write a Python program that accepts a string and calculate the number of digits and letters.
s = 'W3resource'
letters = 0
digits = 0
for i in s:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        pass
print('Letters in string are',letters)
print('Digits in string are',digits)
# 15. Write a Python program to check the validity of password input by users. Go to the editor
# Validation :
"""
import re
x = input('Enter the password : ')
a = True
while a:
    if (len(x)< 6 or len(x) > 12):
        break
    elif not re.search("[a-z]",x):
        break
    elif not re.search("[0-9]",x):
        break
    elif not re.search("[A-Z]",x):
        break
    elif not re.search("[@#$]",x):
        break
    elif re.search("\s",x):
        break
    else:
        print('Valid password')
        a = False
        break
if a:
    print('Not a valid password')
"""
#16. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
num= []
for i in range(100, 401):
    if i % 2 == 0:
        num.append(i)
print(num)

