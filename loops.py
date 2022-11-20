#Print the first 10 natural numbers using while loop.
natural = []
number = 1
while number <= 10:
    natural.append(number)
    number += 1
print(natural)

#2.Calculate the sum of all numbers from 1 to a given number.

# given_number = int(input("Enter the number you want to stop on"))
# list = []
# first = 1
# while first <= given_number:
#     list.append(first)
#     first += 1
# #print(list)
# Sum = sum(list)
# print(Sum)

#3.Write a program to print multiplication table of a given number. 
# eg if number is 2, then output should be 2, 4, 6, 8 ...

l1 = []
multiples = []
given = int(input("Enter a number"))
num = 1
while num < 31:
    l1.append(num)
    num += 1
for i in l1:
    multiple = i * given
    multiples.append(multiple)
print(multiples)

    