# Section A – Basics (Short questions)

# Write a Python program to input a number and check whether it is even or odd.
num=int(input("Enter a number: "))
if num%2==0:
  print("Even")
else:
  print("Odd")
# Input a character and check whether it is a vowel or consonant.
vowel=["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
char=input("Enter a character")
if char in vowel:
  print("Vowel")
else: 
  print("Constant")

# Input a number and print its multiplication table from 1 to 10.
num=int(input("Enter a number: "))
for i in range(1,11):
  print(num*i, end=" ")

# Write a program to count digits in a given integer.
digits=0
intStr=input("Enter a number: ")
for i in intStr:
  digits+=1
print(digits)
