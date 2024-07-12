"""Read SQL tables from """

# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query = """
SELECT * 
  FROM hpd311calls;
"""

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())


"""Read the entire weather table using the select *"""

# Create the database engine
engine = create_engine("sqlite:///data.db")

# Create a SQL query to load the entire weather table
query =""" SELECT * FROM weather""";

# Load weather with the SQL query
weather = pd.read_sql(query, engine)

# View the first few rows of data
print(weather.head())


"""oeprators and where clause in sql"""

# Create query for records with max temps <= 32 or snow >= 1
query = """
SELECT *
  FROM weather
  where
  tmax<=32 or snow>=1;
"""

# Query database and assign result to wintry_days
wintry_days = pd.read_sql(query,engine)

# View summary stats about the temperatures
print(wintry_days.describe())


"""Group by clause"""

# Create query to get call counts by complaint_type
query = """
SELECT complaint_type, 
     count(*)
  FROM hpd311calls
  GROUP BY complaint_type;
"""

# Create dataframe of call counts by issue
calls_by_issue = pd.read_sql(query, engine)

# Graph the number of calls for each housing issue
calls_by_issue.plot.barh(x="complaint_type")
plt.show()
