# Query to join weather to call records by date columns
query = """
SELECT * 
  FROM hpd311calls
  JOIN weather 
  ON hpd311calls.created_date = weather.date;
"""

# Create dataframe of joined tables
calls_with_weather = pd.read_sql(query,engine)

# View the dataframe to make sure all columns were joined
print(calls_with_weather)


"""Filtering on Where Clause"""

# Query to get water leak calls and daily precipitation
query = """
SELECT hpd311calls.*, weather.prcp
  FROM hpd311calls
  JOIN weather
    ON hpd311calls.created_date = weather.date
  Where hpd311calls.complaint_type = 'WATER LEAK';"""

# Load query results into the leak_calls dataframe
leak_calls = pd.read_sql(query, engine)

# View the dataframe
print(leak_calls.head())


"""Joining, filtering, and aggregating
In this exercise, you'll use what you've learned to assemble a dataset to investigate how the number of heating complaints to New York City's 311 line varies with temperature.

In addition to the hpd311calls table, data.db has a weather table with daily high and low temperature readings for NYC. We want to get each day's count of heat/hot water calls with temperatures joined in. This can be done in one query, which we'll build in parts.

In part one, we'll get just the data we want from hpd311calls. Then, in part two, we'll modify the query to join in weather data.

pandas has been imported as pd, and the database engine has been created as engine. """

# Query to get heat/hot water call counts by created_date
query = """
SELECT hpd311calls.created_date, 
       count(*)
  FROM hpd311calls 
  where hpd311calls.complaint_type == "HEAT/HOT WATER"
  group by hpd311calls.created_date;
"""

# Query database and save results as df
df = pd.read_sql(query,engine)

# View first 5 records
print(df.head())
