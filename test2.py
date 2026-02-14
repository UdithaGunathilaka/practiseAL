# Section B – Loops & Logic

# Write a program to find the sum of first n natural numbers using a for loop.
sum=0
iterCount=int(input("Enter count of number that u need to sum: "))
for i in range(iterCount):
  num=int(input("Enter a number: "))
  sum+=num
print(sum)

# Input a number and reverse it
# Example: 12345 → 54321
intStr=input("Enter a number: ")
revStr=""
for i in range(len(intStr)-1,-1.-1):
  revStr+=intStr[i]
print(revStr)

# Write a program to check whether a number is a palindrome.
num=input("Enter a number: ")
revNum=""
for i in range(len(num)-1,-1,-1):
  revNum+=num[i]
if num==revNum:
  print("Entered number is a palidrome")
else:
  print("Entered number is not a palindrome")

# Write a program to count even and odd numbers in a given range.
start=int(input("Enter a number for the start of the range: "))
end=int(input("Enter a number for the end of the range: "))
oddCount=0
evenCount=0
for i in range(start, end+1):
  if i%2==0:
    evenCount+=1
  else:
    oddCount+=1
print("Even count is:", evenCount )
print("Odd count is:", oddCount )

# Print the following pattern:
# *
# **
# ***
# ****
for i in range(1, 5):
  for j in range(i):
    print("*", end="")
  print(" ")