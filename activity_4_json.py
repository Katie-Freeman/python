import json

print("Movie title, Year, imdbID and type of movie")
print("*******************************************")

with open("movies.json") as file: 
   movies = json.load(file)

for movie in movies:
    print(f"{movie['Title']} - {movie['Year']} - {movie['imdbID']} - {movie['Type']}")


# print("LISTS OF PERSONS")

# with open("persons.json") as file: 
#    persons = json.load(file)

# for person in persons: 
#   print(f"{person['name']} - {person['email']}")
#   address = person["address"] # address dictionary 
#   print(address["street"])
#   print(address["city"])
#   geo = address["geo"]
#   print(geo["lat"])
