#Task 01
print("Task 1")
import random
n = int(input("How many dice do you want to roll? "))

sum = 0

for i in range(n):
  roll = random.randint(1, 6)
  sum += roll

print(f"The sum of the numbers is {sum}")

#Task 02
print("Task 2")
numbers = []
while True:
  num = input("Enter a number or press enter to quit: ")
  if num == "":
    break
  else:
    try:
      num = float(num)
      numbers.append(num)
    except ValueError:
      print("Invalid input. Please enter a number or press enter to quit.")

if numbers:
  numbers.sort(reverse=True)
  print("The five greatest numbers are:")
  for i in range(min(5, len(numbers))):
    print(numbers[i])

else:
  print("No numbers were entered.")

#task 03
print("Task 3")
num = int(input("Enter an integer: "))

is_prime = True

for i in range(2, int(num**0.5) + 1):

  if num % i == 0:
    is_prime = False
    break
if is_prime:
  print(num, "is a prime number.")
else:
  print(num, "is not a prime number.")

#task 04
print("task 4")
city_names = []

for i in range(5):
    city_name = input("Enter the name of city {}: ".format(i + 1))
    city_names.append(city_name)
print("The names of the cities you entered are:")
for city_name in city_names:
    print(city_name)




