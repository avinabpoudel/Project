product_name = "Chips"
Price = 10.50
Quantity = 5
Good = True
#types
print(type(product_name))
print(type(Price))
print(type(Quantity))
print(type(Good))

#Arithmetic Operators
print(Price * Quantity)
print("Double quantity: ", Quantity * 2 )
print("Something: ", Quantity + Price)

#Comparision Operators
print(Price > Quantity)
print(Price == Quantity)
print(Price < Quantity)

#String Operations
print("String operation: " "Arthur"+" "+"Morgan")
print(len(product_name))
print("Letter: ", product_name[4])

#Swapping In python
a = 12
b = 5
temp = b
b = a
a = temp
print(a)
print(b)