def cinema_simulator():
    films = {"Finding Dory": [3, 5],
             "Bourne": [18, 5],
             "Tarzan": [15, 5],
             "Ghost Busters": [12, 5]
             }

    while True:
        choice = input("What film you would like to watch?: ").strip().title()
        print(choice)
        if choice in films:
            age = int(input("How old are you?: ").strip())
            print(age)
            # check user age
            if age >= films[choice][0]:
                # check enough seats
                num_seats = films[choice][1]
                if num_seats > 0:
                    print("Here is your Ticket! Enjoy the film")
                    films[choice][1] = num_seats - 1
                    print(films)
                else:
                    print("Sorry...We are sold out!")
            else:
                print("You are too young to see the film...")
                print(films)

        else:
            print("We don't have that film...")


if __name__ == '__main__':
    cinema_simulator()
