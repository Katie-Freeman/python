with open("programing.txt", "a") as file:
    while True:
        answer = input("What do you like about programing? press q to quit: ")
        if answer == "q":
            break
        file.write(answer)
        file.write("\n")
