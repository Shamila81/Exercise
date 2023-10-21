#Task 1
print("Task 1")
seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter a number of a month (1-12): "))

if month < 1 or month > 12:
    print("Invalid input. Please enter a number between 1 and 12.")
else:
    index = (month - 1) // 3 % 4
    print(f"The season for month {month} is {seasons[index]}.")

#Task 2
print ("Task 2")
names = set()

while True:
    name = input("Enter a name or press enter to stop: ")
    if name == "":

        break
    elif name in names:

        print("Existing name")
    else:

        names.add(name)
        print("New name")

print()
for name in names:
    print(name)

#Task 3
print("Task 3")
import requests

airport_data = {}
def fetch_airport_data(icao_code):

    url = "https://aviation-edge.com/v2/public/airport?iataCode={icao_code}".format(icao_code=icao_code)
    response = requests.get(url)

    airport_data = response.json()

    return airport_data
def store_airport_data(icao_code, airport_name):
    airport_data[icao_code] = airport_name
def print_airport_data(icao_code):

     airport_name = airport_data.get(icao_code)

    if airport_name is None:
        print("Airport data not found for ICAO code:", icao_code)
    else:
        print("Airport name:", airport_name)

while True:
    # Ask the user what they want to do.
    print("What do you want to do?")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        icao_code = input("Enter the ICAO code of the airport: ")
        airport_name = input("Enter the name of the airport: ")

        store_airport_data(icao_code, airport_name)


    elif choice == 2:
        icao_code = input("Enter the ICAO code of the airport: ")

        print_airport_data(icao_code)

    elif choice == 3:
        break

    else:
        print("Invalid choice.")

print("Goodbye!")