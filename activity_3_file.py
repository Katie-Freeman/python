with open("dishes.txt", "a") as file:
    while True:
        answer = input("What is your favorite dish? press q to quit: ")
        if answer == "q":
            break
        file.write(answer)
        file.write("\n")

with open("dishes.txt", "r") as file:
    lines = file.readlines()
    print(lines)