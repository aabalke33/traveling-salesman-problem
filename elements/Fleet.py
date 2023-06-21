import datetime

from elements.Truck import Truck
from elements.Calculation import delivery_calculation

# Manually chooses which packages go to which truck
truck1_packages = [1, 30, 5, 7, 13, 14, 15, 16, 19, 20, 21, 29, 31, 34, 37, 40]
truck2_packages = [2, 3, 6, 8, 18, 25, 26, 27, 28, 4, 32, 33, 35, 36, 38]
truck3_packages = [10, 11, 12, 17, 22, 23, 24, 39, 9]

# Manually chooses what times trucks leave hub
truck1_time = datetime.timedelta(hours=8, minutes=0, seconds=0)
truck2_time = datetime.timedelta(hours=9, minutes=5, seconds=0)
truck3_time = datetime.timedelta(hours=10, minutes=20, seconds=0)

# Creates 3 Truck objects
truck1 = Truck(truck1_packages, truck1_time)
truck2 = Truck(truck2_packages, truck2_time)
truck3 = Truck(truck3_packages, truck3_time)

# Calculates how to deliver each trucks packages
delivery_calculation(truck1)
delivery_calculation(truck2)
delivery_calculation(truck3)

# Adds up total miles for printing to screen
total_miles = truck1.miles + truck2.miles + truck3.miles

# Gets last delivery time for printing to screen
last_delivery_time = truck3.time
