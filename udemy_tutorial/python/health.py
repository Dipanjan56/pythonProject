import random


def healthPortion1():

    difficulty = 3

    health = 50
    old_health_text = "old value: {}"
    print(old_health_text.format(health))

    portion_health = int(random.randint(25, 50) / difficulty)
    portion_health_text = "portion value: {}"
    print(portion_health_text.format(portion_health))

    health = health + portion_health
    new_health_text = "new value value: {}"
    print(new_health_text.format(health))


if __name__ == '__main__':
    healthPortion1()
