#task 01
print("Task 1")
import random
def dice_roll():

  return random.randint(1, 6)
def main():

  result = 0
  while result != 6:
    result = dice_roll()
    print(f"You rolled a {result}")
  print("You got a six!")

main()

# Task 02
print("Task 2")

import random
def roll_dice():
    return random.randint(1, 6)
def main():
    while True:
        roll = roll_dice()
        print(roll)
        if roll == 6:
            break

if __name__ == '__main__':
    main()
    import random
    def roll_dice(sides):
        return random.randint(1, sides)


    import random
    def roll_dice(sides):
        return random.randint(1, sides)
    def main():
        max_sides = int(input("Enter the number of sides on the dice: "))

        while True:
            roll = roll_dice(max_sides)
            print(roll)
            if roll == max_sides:
                break


    if __name__ == '__main__':
        main()
#task 03
print("Task 3")
def gallons_to_liters(gallons):
    return gallons * 3.785411784
def main():
    while True:
        gallons = float(input("Enter a volume in gallons: "))
        if gallons < 0:
            break

        liters = gallons_to_liters(gallons)
        print("{} gallons is equal to {} liters.".format(gallons, liters))

if __name__ == '__main__':
    main()

#task 4
print("Task 4")
def sum_list(list_of_integers):

    sum = 0
    for number in list_of_integers:
        sum += number
    return sum
def main():
    list_of_integers = [1, 2, 3, 4, 5]

    sum = sum_list(list_of_integers)

    print("The sum of the numbers in the list is:", sum)

if __name__ == '__main__':
    main()

#task 05
print("Task 5")
def remove_uneven_numbers(numbers):
  even_numbers = []
  for number in numbers:
    if number % 2 == 0:
      even_numbers.append(number)
    return even_numbers
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cut_down_list = remove_uneven_numbers(original_list)

print("Original list:", original_list)
print("Cut-down list:", cut_down_list)

#TASK 6
print("Task 6")
import math
def calculate_pizza_unit_price(diameter, price):

  radius = diameter / 2
  area = radius * radius * math.pi
  unit_price = price / area

  return unit_price
def main():
  pizza_1_diameter = float(input("Enter the diameter of the first pizza in centimeters: "))
  pizza_1_price = float(input("Enter the price of the first pizza in euros: "))

  pizza_2_diameter = float(input("Enter the diameter of the second pizza in centimeters: "))
  pizza_2_price = float(input("Enter the price of the second pizza in euros: "))

  pizza_1_unit_price = calculate_pizza_unit_price(pizza_1_diameter, pizza_1_price)

  pizza_2_unit_price = calculate_pizza_unit_price(pizza_2_diameter, pizza_2_price)

  if pizza_1_unit_price < pizza_2_unit_price:
    print("The first pizza provides better value for money.")
  elif pizza_1_unit_price > pizza_2_unit_price:
    print("The second pizza provides better value for money.")
  else:
    print("Both pizzas provide the same value for money.")

if __name__ == '__main__':
  main()



