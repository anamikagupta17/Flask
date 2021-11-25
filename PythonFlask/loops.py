i=1
while i<=6 :
 print(i)
 if i==4 :
   break 
 i+=1
 
z=0
while z < 8:
 z+=1
 if(z==4):
  continue
 print(z) 
 
# for loops
print("For Loops:")
for x in range(5):
 print(x)
 
print("Specific Range in for loops")
for x in range(5,10):
 print(x)
print("Increment in range")
for x in range(2,30,4):
 print(x)
print("Else in for loop")
for x in range(6):
  print(x)
else:
  print("Finally finished!")
print("Nested loops")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
  # print(x)
   #print(y)
   print(x, y)
print("\n Recursion")
def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)
 