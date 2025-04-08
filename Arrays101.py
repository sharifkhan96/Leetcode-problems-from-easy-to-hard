"""
# Defining a class for DVD
class DVD:
    def __init__(self, name, releaseYear, director):
        self.name = name
        self.releaseYear = releaseYear
        self.director = director

    def __str__(self):
        return f"{self.name}, directed by {self.director}, released in {self.releaseYear}"

# Creating a collection of DVD objects
dvd_collection = [
    DVD("Casino Royal", 2006, "James Bond"),
    DVD("IMF1", 1996, "Ethan Hunt"),
    DVD("Movie 3", 2005, "Director 3"),
    DVD("Movie 4", 2007, "Director 4"),
    DVD("Movie 5", 2009, "Director 5"),
    DVD("Movie 6", 2011, "Director 6"),
    DVD("Movie 7", 2013, "Director 7"),
    DVD("Movie 8", 2015, "Director 8"),
    DVD("Movie 9", 2017, "Director 9"),
    DVD("Movie 10", 2019, "Director 10"),
    DVD("Movie 11", 2021, "Director 11"),
    DVD("Movie 12", 2022, "Director 12"),
    DVD("Movie 13", 2020, "Director 13"),
    DVD("Movie 14", 2023, "Director 14"),
    DVD("John Wick4", 2023, "John Wick")
]

dvd_collection[14] = ("John Wick", 2023, "Keanu Reves")

# Printing the DVD collection
for dvd in dvd_collection:
    print(dvd)
"""

square_numbers = [0] * 10

for i in range(10):
    square = (i + 1) * (i + 1)
    square_numbers[i] = square

print(square_numbers)
for i in square_numbers:
    print(i, end="\n")