import csv


# Reads csv file and returns list of values
def reader(location):
    return list(csv.reader(open(location)))


# Reads location data specifically
def location_reader():
    return reader("data/location_data.csv")


# Reads distance data specifically
def distance_reader():
    return reader("data/distance_data.csv")


# Reads package data specifically
def package_reader():
    return reader("data/package_data.csv")
