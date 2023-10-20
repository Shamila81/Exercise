#Task 01
print("Task 1 ")
length = int(input("What is the length of a Zander in centimeters? "))
if length<42:
    print(f"\n{42-length} centimeters below the size limit" )
    print("Lets release the fish back in to the lake.")
else:
    print ("\nYou can keep the zander.")

#Task 02
print("Task 2")

cabin_class= input ("Please Enter the cabin class (LUX ,A, B, C): ")
if cabin_class == "LUX":
    print("upper-deck cabin with a balcony")
elif cabin_class == "A":
    print("above the car deck, equipped with a window")
elif cabin_class == "B":
    print("windowless cabin above the car deck")
elif cabin_class == "C":
    print("windowless cabin below the car deck")
else :
    print("Invalied cabin class")

    #Task 03
print("Task 3")
gender = input("Are you a male or Female? ")
hemoglobin = float(input("What is the Hemoglobin value (g/l)? "))


if gender.lower() == "male":
  low = 134
  high = 167
elif gender.lower() == "female":
  low = 117
  high = 155
else:
  print("Invalid input")
  exit()


if hemoglobin < low:
  print("Your hemoglobin value is low.")
elif hemoglobin > high:
  print("Your hemoglobin value is high.")
else:
  print("Your hemoglobin value is normal.")

  #Task 04
print("Task 04")
year = int(input("Enter a year: "))

if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print(year, "is a leap year.")
    else:
      print(year, "is not a leap year.")
  else:
    print(year, "is a leap year.")
else:
  print(year, "is not a leap year.")
