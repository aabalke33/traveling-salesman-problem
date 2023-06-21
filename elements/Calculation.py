import datetime
from elements.CsvParser import *
from elements.Package import *

# These members load the location, distance and package data from the csv readers
location_data = location_reader()
distance_data = distance_reader()
all_packages = package_data()


# This function calculates the Nearest Neighbor path for each truck, and updates Truck and Package information
def delivery_calculation(truck):
    # Define variable to list packages in truck
    packages_in_truck = []

    # Update incorrect address for package #9
    all_packages.get('9').address = "410 S State St"

    # Add packages on each truck object into the packages_in_truck list
    for id in truck.packages:
        package = all_packages.get(str(id))
        packages_in_truck.append(package)

    # Delete packages from truck object, they will be added back once the order is figured out
    truck.packages.clear()

    # While there are still packages in the truck, check for the closest package and update truck and package info
    while packages_in_truck:

        # Initialize each segments (edges) chosen distance, and package. When better options are iterated over,
        # these options are updated.
        chosen_distance = 25
        chosen_package = None

        # This is the actual Nearest Neighbor Algorithm. The distance between each packages delivery address,
        # and the current location of the truck is measured. The package with the smallest travel distance is
        for package in packages_in_truck:

            truck_address_id = ""
            package_address_id = ""

            # Gets ID version of address from String version
            for row in location_data:
                if truck.address in row[2]:
                    truck_address_id = int(row[0])
                if package.address in row[2]:
                    package_address_id = int(row[0])

            # Gets distance between current location and packages destination address
            if truck_address_id <= package_address_id:
                distance = float(distance_data[package_address_id][truck_address_id])
            else:
                distance = float(distance_data[truck_address_id][package_address_id])

            # If this packages distance is shorter than already checked distances
            # this distance and package are chosen for the next stop.
            # Otherwise, keep the old distance and package
            if distance < chosen_distance:
                chosen_distance = distance
                chosen_package = package

        # add package id to truck object packages, (This will order them by when they are delivered)
        truck.packages.append(chosen_package.package_id)

        # remove package from package in truck list
        packages_in_truck.remove(chosen_package)

        # add the chosen distance to the miles the truck has traveled
        truck.miles += chosen_distance

        # Set the truck address as the packages delivery address
        truck.address = chosen_package.address

        # Add the time travelled to the new package address, to the total truck travel time
        truck.time += datetime.timedelta(hours=chosen_distance / truck.speed)

        # Set the new time to the packages delivery time
        chosen_package.delivery_time = truck.time
        chosen_package.depart_time = truck.depart_time

    # First Truck has to Return Home before Truck 3 can leave
    # Only will return if it is the first truck, and it has no more packages
    if not packages_in_truck and truck.depart_time == datetime.timedelta(hours=8):
        # Address 0 is the Hub
        truck_address_id = 0

        # Finds the current truck address id from the string version
        for row in location_data:
            if truck.address in row[2]:
                truck_address_id = int(row[0])

        # Gets the distance between the trucks current location and the hub
        distance = float(distance_data[truck_address_id][0])

        # Adds this time to the total miles traveled
        truck.miles += distance

        # Updated String Address
        truck.address = "4001 South 700 East"

        # Adds time traveled to hub to trucks time
        truck.time += datetime.timedelta(hours=distance / truck.speed)
