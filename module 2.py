# Task 01
print("Task 1")
name = input("Please Enter your name: ")
print(f"Hello, {name} ! ")
print("\n")

#Task 02
print("Task 2")
Radius = float(input("Please Enter radius of the circle: "))
import math
Area =float(math.pi* Radius**2)
print("The Area of the circle is ",Area)
print("\n")

#Task 03
print("Task 3")
length = float(input("What is the length of the rectangle? "))
width = float(input("What is the width of the rectangle? "))
perimeter = 2 * ( length + width )
Area = length * width
print("The perimeter is", perimeter)
print("The Area is ", Area)
print("\n")

#Task o4
print("Task 4")
num1 = int(input("Enter 1 st integer number: "))
num2 = int(input("Enter 2 nd integer number: "))
num3 = int(input("Enter 3 rd integer number: "))
sum = num1 + num2 + num3
product = num1 * num2 * num3
average = sum / 3
print("sum = ", sum)
print("product = ", product)
print("average = ", average)
print("\n")

#Task 05
print("Task 5")
lot_to_g = 13.3
pound_to_lot = 32
talent_to_pound = 20
talents = int(input("Enter talents: "))
pounds = int(input("Enter pounds: "))
lots = float(input("Enter lots: "))
total_grams = talents * talent_to_pound * pound_to_lot * lot_to_g+ pounds * pound_to_lot * lot_to_g + lots * lot_to_g
kg = int(total_grams/1000)
g = total_grams % 1000
print(f"The weight in modern units: {kg} kilograms and {g:.2f} grams.")
print("\n")

# Task 06
print("Task 6")
import random
code1 = ""
for i in range(3):
    code1 +=str(random.randint(0,9))

code2 = ""
for i in range(4):
    code2 +=str(random.randint(1,6))
print("The first code is ",code1)
print("The second code is ",code2)

