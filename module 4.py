#Task 01
print("task 1")
number=1
while number <= 1000:
    if number % 3 ==0:
      print(number)
    number=number+1

#Task 02
print("task 2")
def inches_to_cm(inches):
    return inches * 2.54

inches = float(input("Enter a value in inches: "))

while inches >= 0:
    cm = inches_to_cm(inches)
    print(f"{inches} inches = {cm} centimeters")
    inches = float(input("Enter another value in inches: "))
print("Program ended.")

#Task 03
print("Task 3")
numbers = []
while True:
  user_input = input("Enter a number or press enter to quit: ")
  if user_input == "":
    break
  else:
    try:
      number = float(user_input)
      numbers.append(number)
    except ValueError:
      print("Invalid input. Please enter a number or press enter to quit.")
if numbers:
  print("The smallest number is", min(numbers))
  print("The largest number is", max(numbers))
else:
  print("No numbers were entered.")

  #Task 04
print("Task 4")
import random
number = random.randint(1, 10)
guess = None
while guess != number:
    guess = int(input("Enter a number between 1 and 10: "))
    if guess > number:
      print("Too high")
    elif guess < number:
      print("Too low")
    else:
      print("Correct")
print("You guessed the number!")

#Task 05
print("Task 5")
username = "harshi"
password = "81@62har"

attempts = 0

while True:

    user_input = input("Enter your username and password separated by a space: ")

    user_name, user_pass = user_input.split()

    if user_name == username and user_pass == password:
        print("Welcome")
        break
    else:
        attempts += 1
        print(f"Wrong username or password. You have {5 - attempts} attempts left.")

        if attempts == 5:
            print("Access denied")
            break

#Task 06
print("Task 6")
import random

N = int(input("How many random points to generate? "))
n = 0

for i in range(N):
  x = random.uniform(-1, 1)
  y = random.uniform(-1, 1)

  if x**2 + y**2 < 1:
     n += 1
pi = 4 * n / N
print(f"pi is approximately {pi}")

