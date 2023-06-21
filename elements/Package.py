from elements.CsvParser import package_reader
from elements.HashTable import HashTable


# Class to define a Package and it's members
class Package:
    # Initializer
    def __init__(self, package_id, address, city, state, zip_code, deadline, weight, status, notes):
        self.package_id = package_id
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.deadline = deadline
        self.weight = weight
        self.status = status
        self.notes = notes
        self.depart_time = None
        self.delivery_time = None

    # Print Cleanup, makes it nicer to print a package to the screen
    def __str__(self):

        return f'{str(self.package_id): <5}' \
               f'{str(self.address): <30}' \
               f'{str(self.city): <20}' \
               f'{str(self.state): <5}' \
               f'{str(self.zip_code): <15}' \
               f'{str(self.deadline): <15}' \
               f'{str(self.weight): <5}' \
               f'{str(self.status): <15}' \
               f'{str(self.delivery_time): >15}' \
               f'\t{str(self.notes): <30}'

    # This function checks the input time to the delivery and departure times to update the string status
    def set_status(self, converted_time):
        if converted_time > self.delivery_time:
            self.status = "Delivered"
        elif self.depart_time > converted_time:
            self.status = "En Route"
        else:
            self.status = "At the Hub"


# This function takes the package data from the csv reader, and converts it into a Hash Table of package objects
def package_data():
    package_list = package_reader()
    packages = HashTable()

    for record in package_list:
        package = Package(record[0], record[1], record[2], record[3],
                          record[4], record[5], record[6], "At Hub", record[7])

        packages.add(record[0], package)

    return packages
