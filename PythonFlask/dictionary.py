dist={
"Name":"Anamika",
"DOB":1996,
"Course":"B.tech"
}
print(dist)
x=dist["DOB"]
print(x)
x=dist.get("Course")
print(x)
dist["Name"]="Anamika Gupta"
print(dist)
for x in dist:
 print(x)
for x in dist:
 print(dist[x])
for x in dist.values():
 print(x) 
 for x,y in dist.items():
  print(x,y)
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
  # popitem delete last items
  # del with key delete particular key and values
 
 