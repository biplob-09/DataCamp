"""Drop Duplicates"""

# Drop duplicate store/type combinations
store_types = sales.drop_duplicates(["store","type"])
print(store_types.head())

# Drop duplicate store/department combinations
store_depts = sales.drop_duplicates(['store','department'])
print(store_depts.head())

# Subset the rows where is_holiday is True and drop duplicate dates
holiday_dates = sales[sales["is_holiday"]].drop_duplicates("date")

# Print date col of holiday_dates
print(holiday_dates["date"])


"""2nd Example"""

# Count the number of stores of each type
store_counts = store_types.value_counts("type")
print(store_counts)

# Get the proportion of stores of each type
store_props = store_types['type'].value_counts(normalize=True)
print(store_props)

# Count the number of each department number and sort
dept_counts_sorted = store_depts['department'].value_counts(sort=True)
print(dept_counts_sorted)

# Get the proportion of departments of each number and sort
dept_props_sorted = store_depts['department'].value_counts(sort=True, normalize=True)
print(dept_props_sorted)
