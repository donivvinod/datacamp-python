#!/usr/bin/python

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin', 'norway':'oslo' }

# Add italy to europe
europe['italy'] ='rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] ='warsaw'

# Remove norway
del europe['norway']

# Print europe
print(europe)

# Dictionary of dictionaries
europe2 = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }

# Print out the capital of France
print(europe2['france']['capital'])

# Create sub-dictionary data
data = { 'capital':'rome', 'population':59.83 } 

# Add data to europe under key 'italy'
europe2['italy'] = data

# Print europe
print(europe2)

#iterate and print dictionary contents
for key,value in europe2.items() :
    print(key + "----->" + str(value))

