def travis_security_system():
    known_users = ["Alice", "Bob", "Claire", "Dan", "Emma", "Fred", "George", "Harry"]
    print(len(known_users))

    while True:
        print("Hi! me name is Travis")
        name = input("What is ur name?: ").strip().capitalize()
        print(name)

        if name in known_users:
            # print("Hello " + name + "!")
            print("Hello {}!".format(name))
            remove_me = input("Would you like to be removed (y/n)?: ").strip().lower()
            if remove_me == "y":
                known_users.remove(name)
                print("We have successfully removed you from our system")
                print(known_users)
            elif remove_me == "n":
                print("No Problem, I didn't want you to leave anyway!")

        else:
            print("h,, I don't think I met you yet {}".format(name))
            add_me = input("Would you like to be added (y/n)?: ").strip().lower()
            if add_me == "y":
                known_users.append(name)
                print("Congrats! We have successfully added you from our system")
                print(known_users)
            elif add_me == "n":
                print("No worries, see you around!")


if __name__ == '__main__':
    travis_security_system()
