# Section C – Lists 

# Input 10 numbers into a list and find the maximum and minimum.
l=[]
for i in range(10):
  l.append(int(input("Enter a number: ")))
min,max=l[0],l[0]

for i in range(len(l)):
  if min>l[i]:
    min=l[i]
  if max<l[i]:
    max=l[i]
print("Maximum num is:", max)
print("Minimum num is:", min)

# Write a program to count how many even numbers are in a list.
l=[1,2,3,4,5]
evenCount=0
for i in range(len(l)):
  if l[i]%2==0:
    evenCount+=1
print(evenCount)

# Input a list and reverse it without using reverse().
l=[1,2,3,4,5]
revl=[]
for i in range(len(l)-1,-1,-1):
  revl.append(l[i])
print(revl)

# Write a program to search an element in a list and print its position.
l=[1,2,3,4,5]
num=3
for i in range(len(l)):
  if l[i]==num:
    print("Position of the number is:", i)
    break