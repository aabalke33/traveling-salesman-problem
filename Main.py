import datetime

from elements.Error import error
from elements.Calculation import all_packages
from elements.Fleet import total_miles, last_delivery_time, truck1, truck2, truck3

# Command Line User Interface
# Summary
print(f'\nData Structures and Algorithms II - C950\n')
print(f'Algorithm Used: Nearest Neighbor\n')
print(f'Total Miles: {round(total_miles, 2)}\n')
print(f'Last Package Delivered at: {last_delivery_time}\n')

# The program will first check for "quit" before entering detailed look
quit_check = input(f'Press Enter - Begin Simulation\n'
                   f'Type "quit" - Quit Application\n')

if quit_check != "quit":
    try:
        # Prints the Trucks and there corresponding packages
        print(f'Truck 1 Packages in Delivery Order: {truck1.packages}')
        print(f'Truck 2 Packages in Delivery Order: {truck2.packages}')
        print(f'Truck 3 Packages in Delivery Order: {truck3.packages}')

        # Enter an input time to exact package statuses
        input_time = input("\nCheck package status at time (HH:MM:SS): ")
        (h, m, s) = input_time.split(":")

        converted_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

        # Choose a specific package or all packages to print to the screen
        input_selection = input("\nType all to get all package statuses, or type\n"
                                "a package ID (1-40) to get an individual package status: ")
        # Print Header
        print(f'\n{"ID": <5}'
              f'{"Address": <30}'
              f'{"City": <20}'
              f'{"State": <5}'
              f'{"Zip": <15}'
              f'{"Deadline": <15}'
              f'{"Weight": <5}'
              f'{"Status": <15}'
              f'{"Delivery Time": >15}'
              f'\t{"Notes": <30}')

        # Logic to print all packages
        if input_selection == "all":

            for id in range(1, 41):
                package = all_packages.get(str(id))
                package.set_status(converted_time)
                print(package)

        # Logic for specific package
        else:
            package = all_packages.get(str(input_selection))
            package.set_status(converted_time)
            print(package)
    except:
        error()
else:
    error()
