print("Welcome to my ToDo app")
tasks = []
xp = 0
level = 0
while True:
    print("PLAYER STATS")
    print("Level: " + str(level))
    print("XP: " + str(xp) + "/100")
    print("1. See list")
    print("2. Add task")
    print("3. Finish task")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Type a number: ")

    if choice == "1":
        print("MY TASKS")
        count = 0
        for t in tasks:
            count = count + 1
            if t["done"] == True:
                print(str(count) + ". [x] " + t["name"])
            else:
                print(str(count) + ". [ ] " + t["name"])

    elif choice == "2":
        name = input("Task name: ")
        task = {"name": name, "done": False}
        tasks.append(task)
        print("Added!")

    elif choice == "3":
        count = 0
        for t in tasks:
            count = count + 1
            if t["done"] == True:
                print(str(count) + ". [x] " + t["name"])
            else:
                print(str(count) + ". [ ] " + t["name"])

        num = int(input("Which number to finish? "))

        index = num - 1

        if index >= 0 and index < len(tasks):
            if tasks[index]["done"] == False:
                tasks[index]["done"] = True
                print("Finished!")

                xp = xp + 50
                print("You got 50 XP!")

                if xp >= 100:
                    level = level + 1
                    xp = 0
                    print("LEVEL UP! You are now Level " + str(level))
            else:
                print("You already did this task")
        else:
            print("Bad number")

    elif choice == "4":
        count = 0
        for t in tasks:
            count = count + 1
            if t["done"] == True:
                print(str(count) + ". [x] " + t["name"])
            else:
                print(str(count) + ". [ ] " + t["name"])

        num = int(input("Which number to delete? "))
        index = num - 1

        if index >= 0 and index < len(tasks):
            deleted = tasks.pop(index)
            print("Deleted " + deleted["name"])
        else:
            print("Bad number")

    elif choice == "5":
        print("Bye")
        break

    else:
        print("Wrong choice")