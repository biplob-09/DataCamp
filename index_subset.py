"""Index Subsetting in DataFrame"""

# Look at temperatures
print(temperatures)

# Set the index of temperatures to city
temperatures_ind = temperatures.set_index('city')

# Look at temperatures_ind
print(temperatures_ind)

# Reset the temperatures_ind index, keeping its contents
print(temperatures_ind.reset_index())

# Reset the temperatures_ind index, dropping its contents
print(temperatures_ind.reset_index(drop=True))


""" loc vs squre bracker subsetting using isin() """

# Make a list of cities to subset on
cities =["Moscow", "Saint Petersburg"] 

# Subset temperatures using square brackets
print(temperatures[temperatures["city"].isin(cities)])

# Subset temperatures_ind using .loc[]
print(temperatures_ind.loc[cities])


"""Index level and sorting """

# Sort temperatures_ind by index values
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level=["city"]))

# Sort temperatures_ind by country then descending city
print(temperatures_ind.sort_index(level=["country","city"],ascending = [True,False]))
