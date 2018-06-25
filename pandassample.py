#!/usr/bin/python
import pandas as pd
import numpy as np

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr =  [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap':cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(data=my_dict)

# Print cars
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JAP', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

#Read the cars.csv
#cars = pd.read_csv('/Users/vinodkumarv/PycharmProjects/datacamp-python/cars.csv',index_col=0)
cars = pd.read_csv('C:/Users/admin/python/datacamp-python/cars.csv',index_col=0)

# Print out cars
print(cars)

# Print out cars_per_cap type 
print(type(cars["cars_per_cap"]))

# Print out country and cars_per_cap
print(cars[["country","cars_per_cap"]])

#print rows 2,3,4  
print(cars[1:4]) #index starts with zero and the end of the slice is not included.

#row access loc
print(cars.loc[["JAP","EG","IN"]])

#row access loc with two columns
print(cars.loc[["JAP","EG","IN"],["country","cars_per_cap"]])


#row access loc all rows with two columns
print(cars.loc[:,["country","cars_per_cap"]])

#row access loc
print(cars.loc[["JAP"]])

#row access loc
print(cars.iloc[[0,1,2]])


#row access loc with two columns
print(cars.iloc[[0,1,2],[0,1]])


#row access loc all rows with two columns
print(cars.iloc[:,[0,1]])


#Filtering pandas dataframe
is_huge = cars["cars_per_cap"] > 500
print(is_huge)
#Subset DF
print(cars[is_huge])

#Filtering DF with numpys
is_medium =  np.logical_and(cars["cars_per_cap"] > 200, cars["cars_per_cap"] < 500)
print(cars[is_medium])

# Extract drives_right column as Series: dr
dr = cars["drives_right"]

# Use dr to subset cars: sel
sel = cars[dr == True]

# Print sel
print(sel)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars["cars_per_cap"]
many_cars = cpc>500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

# Create medium: observations with cars_per_cap between 100 and 500
cpc = cars['cars_per_cap']
between = np.logical_and(cpc > 10, cpc < 80)
medium = cars[between]


# Print medium
print(medium)