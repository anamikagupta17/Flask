a=25
b=24
c=45
if(a>b):
 print ("a is greater than b")
elif(a==b):
 print("A is equals to B") 
else:
 print("B is greater than A")
 
# single line statments
if(a < b):print("A is less then b")
print("A") if(a > b)else print("b")
print("A") if a > b else print("=") if a == b else print("B")
 
 # And OR operators
if b> a and c>a:
  print("Both conditions are true")
else :
  print("Both conditions are not true") 
  
if a>b and c>a:
  print("One Condition is true");