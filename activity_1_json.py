import json

users = []

while True:
        
    name = input("What is your name? ")
    age = int(input("What is your age? "))

    user = {"name": name, "age": age}

    users.append(user)

    choice = input("Enter q to quit, or any key to continue: ")

    if choice == "q":
        break
        
with open ("users.json", "w") as file:
    json.dump(users, file, indent = 4)

for user in users:
    print(user["name"], user["age"])
    
    