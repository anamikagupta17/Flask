set = {"Apple","Banana","Orange","Mango","Guava"}
print(set)
for x in set:
 print(x)
 
print("Orange" in set)
set.add("watermelon")
print(set)
set.update(["Anamika","Parul","Annu"])
print(set)
set.remove("Anamika") # if item not exist then gives error
print(set)
set.discard("Annu") # if item not exist  no error occurs
print(set)
set.pop()
print(set)  # remove the last element of set
set.clear()
print(set)
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}

z = x.isdisjoint(y)  # uncomman

print(z)