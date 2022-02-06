# im not very good at writing :< so it's short and silly
import os
import random

# comparison to what's in the adventure text
going = "movie"

# flag for try/except
flag_one = False
flag_two = False

# snack list
snacks = {"popcorn", "soda", "candy", "icee", "nachos"}


# def for ridiculous amount of food consumed
def food(num):
    total = 0
    for i in range(num):
        total += random.randint(1, 6)
    if total > 20:
        return 0
    else:
        pass


# adventure text: movie decision to pass through loops
def moviefile():
    file = open('adventure.txt', 'r')
    content = file.read()
    return content


# start = sleep/bed
print("You wake up in the morning. It's a bright, sunny day and you have no obligations. You play and look at news\n"
      "for a little while on your phone. You still feel a little sleepy from staying up late last night, but you're\n"
      "also a little hungry.\n")

dec1 = input("Do you get out of bed?\n"
             "sleep\n"
             "breakfast\n")

while dec1 != "sleep" and dec1 != "breakfast":
    print('Please pick either sleep or breakfast\n')
    dec1 = input()

# dec1 path of sleep. end on bed all day
if dec1 == "sleep":
    print("You stay in bed, sleeping a little longer. You are startled awake when you hear your phone go off. You\n"
          "receive a phone call from a friend, they want you to come with them to the movies, they tell you that\n"
          "the zombie flick that the two of you were waiting for is finally in theaters.\n")

    dec2 = input("Do you go with them to the movies?\n"
                 "bed\n"
                 "movie\n")

    while dec2 != "bed" and dec2 != "movie":
        print("Please pick either bed or movie\n")
        dec2 = input()

    # if dec2 is movie, write movie into adventure text
    if dec2 == "movie":
        addfile = open('adventure.txt', 'w')
        addfile.write('movie')
        addfile.close()

    elif dec2 == "bed":
        print("You tell your friend you're not feeling well. They wish you well and you spend the afternoon in bed\n"
              "watching youtube. Before you know it, it's night time and you haven't eaten all day. You get up and\n"
              "head towards the kitchen. You only have cereal and leftovers.\n")

        dec3 = input("What do you eat?\n"
                     "cereal\n"
                     "outside\n")

        while dec3 != "cereal" and dec3 != "outside":
            print("Please pick either cereal or outside\n")
            dec3 = input()

        if dec3 == "cereal":
            print("You eat some cereal, take a shower, and go back to bed. Your day was pretty relaxing and you feel\n"
                  "like you can tackle whatever tomorrow brings you.\n"
                  "The End\n")
            exit(0)

        elif dec3 == "outside":
            print("You get dressed and head outside to get dinner. As soon as you step out the door, you're attacked\n"
                  "from behind and everything goes black.\n"
                  "The End\n")
            exit(0)


# if dec1 is breakfast. end on going to the store or after store
elif dec1 == "breakfast":
    print("You head downstairs and rummage through your kitchen. Looks like you'll have to go to the store soon\n"
          "because all you have is cereal and pancake mix.\n")

    dec4 = input("Do you eat cereal or make pancakes?\n"
                 "cereal\n"
                 "pancakes\n")

    while dec4 != "cereal" and dec4 != "pancakes":
        print("You must pick cereal or pancakes\n")
        dec4 = input()

    # eat a lot of food. you eat too much: ends
    # put try/except in here
    if dec4 == "cereal" or dec4 == "pancakes":

        while flag_one == False:
            try:
                if dec4 == "cereal":
                    consumed = input("How many bowls do you eat?: ")
                elif dec4 == "pancakes":
                    consumed = input("How many pancakes do you eat?: ")

                consumed = int(consumed)
                flag_one = True
            except ValueError:
                print("Invalid input, please input a number")

        stomach = food(consumed)

        if stomach == 0:
            print("You ate too much and get a stomach cramp and feel sick. You decide to rest in bed for the\n"
                  "remainder of the day hoping that your stomach settles down by tomorrow.\n"
                  "The End")
            exit(0)

        else:
            print("You had a good breakfast and feel satisfied.\n")

    if dec4 == "cereal" or dec4 == "pancakes":
        print("You decided to tidy up a little bit and that's when your friend calls you and asks if you want to go\n"
              "to the movies with them. You know that you should probably go to the store to get more food, but the\n"
              "newest zombie flick is out and you and your friend have been dying to see it.\n")

        dec5 = input("Do you go to the movies with your friend?\n"
                     "movie\n"
                     "store\n")

        while dec5 != "movie" and dec5 != "store":
            print("Please pick movie or store\n")
            dec5 = input()

        # movie decision, write to file and goes to movie path
        if dec5 == "movie":
            addfile = open('adventure.txt', 'w')
            addfile.write("movie")
            addfile.close()

        elif dec5 == "store":
            print("You tell your friend you have to go to the store. You get ready and head outside, noticing that\n"
                  "there are hardly any people out. You could walk to the store or drive, although your car is low\n"
                  "on gas.\n")

            dec9 = input("Do you walk or drive?\n"
                         "walk\n"
                         "drive\n")

            while dec9 != "walk" and dec9 != "drive":
                print("Please pick walk or drive\n")
                dec9 = input()

            if dec9 == "walk":
                print("You decide to walk to the store since it's nice outside. As you're walking and thinking\n"
                      "about what to buy, you come across another person who's walking the same direction except\n"
                      "they're kind of shuffling along. As you pass them up, you notice that they smell and you\n"
                      "speed up a little. Suddenly you're attacked from behind and everything goes black.\n"
                      "The End")
                exit(0)

            elif dec9 == "drive":
                print("You decide to drive, there's a gas station at the store and you can buy a lot more groceries.\n"
                      "As you're driving, you see a few people out and about. At the store, there's a lot more people\n"
                      "and some of them look like they're dressed for the new zombie flick. You go inside and pick up\n"
                      "everything you need. Suddenly people are screaming and the front doors are being locked. There\n"
                      "are people screaming about zombies. You see one of the people who is dressed up and ask what's\n"
                      "going on. Unfortunately they're a real zombie and they bite you. You're one of them now.\n"
                      "The End")
                exit(0)


# compare going key to adventure text. end after movie
if going == moviefile():
    os.remove('adventure.txt')
    print("You tell your friend you'll come out to the movies with them. They tell you that they'll pick you up.\n"
          "You get dressed to go out. Your friend picks you up and you head to the theater. When you get there,\n"
          "you notice that there are a lot of people wearing costumes for the new zombie flick. There is a long\n"
          "line, but you both also want snacks.\n")

    dec6 = input("Do you stand in line or get snacks?\n"
                 "line\n"
                 "snacks\n")

    while dec6 != "line" and dec6 != "snacks":
        print("Please pick line or snacks\n")
        dec6 = input()

    if dec6 == "line":
        print("You decide to wait in line and your friend goes inside to get the snacks. The theater attendant asks\n"
              "you how many for the movie and if you have a membership which you do.\n")

        # put try/except in here. we want float
        while flag_two == False:
            try:
                number = input("How many: ")
                guests = float(number)
                flag_two = True
            except ValueError:
                print("Invalid input, please input a number\n")

        ticket = (lambda x: (x * 12.50) - ((x * 12.50) * 0.1))(guests)

        print(number, "attendees and a membership, your total is", ticket, ".You grab your tickets and meet your\n"
              "friend inside. You find your seats and wait for the movie to start.\n")

    elif dec6 == "snacks":
        print("You go inside and stand in line. While you wait in line, you look over at the menu of snacks.\n")
        print(snacks)
        print("\nThey all sound good so you get one of each for both of you. You meet up with your friend\n"
              "at the entrance and head off to the theater The theater is full and you settle into your\n"
              "seat and dig into your snacks. The movie begins, but you feel a little sleepy.\n")

    dec8 = input("Do you fall asleep?\n"
                 "watch\n"
                 "sleep\n")

    while dec8 != "watch" and dec8 != "sleep":
        print("Please pick watch or asleep")
        dec8 = input()

    if dec8 == "sleep":
        print("You fall asleep halfway through the movie. Maybe you shouldn't have stayed up late last night? You\n"
              "never wake up.\n"
              "The End")

    elif dec8 == "watch":
        print("You are determined to stay awake, you'll go to bed as soon as you get home. Towards the end of the\n"
              "movie, as the group in the movie are fighting off zombies, a fight in the theater breaks out. The\n"
              "people who dressed up are fighting other movie goers. One of them attacks your friend. You have a\n"
              "drink in your hand, but the aisle behind you is empty.\n")

        dec10 = input("Do you help your friend or run?\n"
                      "help\n"
                      "run\n")

        while dec10 != "help" and dec10 != "run":
            print("Please pick help or run\n")
            dec10 = input()

        if dec10 == "help":
            print("You throw your drink at the attacker and grab your friend's hand. You lead them out and you both\n"
                  "make it out of the theater. There are a lot of people fighting. You both get into your friend's\n"
                  "car and start heading to your place since it's closer. You pass by a lot of, what you have\n"
                  "realized, zombies. You make it home and you both barricade the door and windows. You gather\n"
                  "anything that could be used as a weapon and take refuge in the bathroom. You sleep fitfully,\n"
                  "trying to get as much rest as possible before you have to go out tomorrow for supplies.\n"
                  "The End")

        elif dec10 == "run":
            print("You make a run for it as soon as you see the attacker bite your friend's arm. Maybe it was the\n"
                  "movie, but the attackers all looked like real zombies. You run out of the theater, there are more\n"
                  "fights outside and people running. You run to your friend's car and lock it. You have no way of\n"
                  "turning on the car, but you don't want to go back outside.\n")

            dec11 = input("Do you stay in the car or leave?\n"
                          "car\n"
                          "leave\n")

            while dec11 != "car" and dec11 != "leave":
                print("Please pick car or leave\n")
                dec11 = input()

            if dec11 == "leave":
                print("You decide to leave, the sooner the better. You start running towards the mall that's nearby.\n"
                      "You make it, but the doors are locked shut. The zombies have started to swarm you and you get\n"
                      "taken down and turn into a zombie yourself. At least you don't have to worry about the future.\n"
                      "The End")

            if dec11 == "car":
                print("You look around your friend's car, hoping to find something to eat or attack with. You instead\n"
                      "find a spare key under the seat and turn on the car and drive home. There are a lot of zombies\n"
                      "on the way home, but you manage to get into your house without encountering any. You board up\n"
                      "your doors and windows, grab whatever food and weapons you can, and lock yourself in the\n"
                      "bathroom. You try to get as much rest as you can because tomorrow you'll have to find supplies\n"
                      "The End")
