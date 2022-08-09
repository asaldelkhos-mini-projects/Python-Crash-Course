#exercise 8-5

def describe_city(city, country):
    print(f"{city} is in {country}")

city = input("city name:")
country = input("country name:")

describe_city(city.title(), country.title()) 
