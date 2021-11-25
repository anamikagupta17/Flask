def my_function():
 print("Hello Anamika !")

my_function()

print("Function with parameter")
def my_function(name):
 print("Hello " + name)
my_function("Anamika")
print("Defaut Parameter")
def my_function(country="India"):
 print("I am from " + country)
my_function("India")
my_function("USA")
print("Return Value from a fuction")
def calculation(x):
 return 5*x
print(calculation(5))
print(calculation(15))
print(calculation(25))
print("Lambda function are used for short period ")
x=lambda a:a*5
print(x(6))
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

 