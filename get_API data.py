api_url = "https://api.yelp.com/v3/businesses/search"

# Get data about NYC cafes from the Yelp API
response = requests.get(api_url, 
                headers=headers, 
                params=params)

# Extract JSON data from the response
data = response.json()

# Load data to a dataframe
cafes = pd.DataFrame(data["businesses"])

# View the data's dtypes
print(cafes.dtypes)


"""API DATA"""

# Create dictionary to query API for cafes in NYC
parameters = {"term" :"cafe" ,
          	  "location" :"NYC"}

# Query the Yelp API with headers and params set
response = requests.get(api_url,
                        parameters,
                        headers=headers)

# Extract JSON data from response
data = response.json()

# Load "businesses" values to a dataframe and print head
cafes = pd.DataFrame(data["businesses"])
print(cafes.head())
