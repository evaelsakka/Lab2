class Car:
    def __init__(self, make, year):
        self.make = make
        self.year = year

    def __lt__(self, other):
        return self.year < other.year

# create a list of Car objects
cars = [Car("Honda", 2018), Car("Toyota", 2016), Car("BMW", 2020)]

# sort the list by year using the sort method of the list
cars.sort()

# print the sorted list
for car in cars:
    print(car.make, car.year)

    
