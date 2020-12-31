print(
    """
***************

  ,.
  \-'__
 / o.__o____
 \/_/ /.___/--,
   ||\' 
   | /
   \_\
   -''

****************
""")
print("Welcome to Jiu-Jitsu Island!")
print("Your mission is to armbar the boss!\n")
print("Its a beautiful island, full of dangers. You must be ready for anything.\n")

def belt_check():
    belt_question = str(input("Did you tie your belt before arriving? Yes or No ")).upper()
    if belt_question == "YES":
        print("\nYou are a true martial artist.")
        print("With belt tied, Gi ready, you begin exploring. You come upon a striker on the side of the road.")
        print("The striker stares at you.\n")
        cross_roads()
    elif belt_question == "NO":
        print("\nAs you begin to tie your belt you get ambushed by a group of berimbolo savages. You are dead.\n")
    else: 
        print("\nPlease respond with Yes or No\n")
        belt_check()

def cross_roads():
    road_question = str(input("Do you ask for directions to the boss? Yes or No ")).upper()
    if road_question == "YES":
        print("\nThe striker insults you and throws a headkick. You block it but then he throws a 1-2 combo which KO's you and shatters your jaw.\n")
    elif road_question == "NO":
        print("\nYou sense that you are a target and you don't hesitate. You go for a double leg and you take the striker down. You pass guard and go to full mount.")
        print("The striker bumps you off and gives his back. You put in a Mata Leao choke and he gets put to sleep.")
        print("A piece of paper falls out of the strikers shorts. On it there are directions to the boss location. Off you go!\n")
        print("You make it to the boss location.")
        print("The boss is massive, you must have a strategy for attack!")
        boss_fight()
    else: 
        print("\nPlease respond with Yes or No\n")
        cross_roads()

def boss_fight():
        try:
            fight_question = int(input('''
            How do you attack? Please select and input a number:
            1.Flying Armbar 
            2.Mounted Armbar 
            3.Armbar from Guard 
            4.Inverted Armbar \n'''))
        except ValueError:
            print("Please input only 1, 2, 3 or 4")
            boss_fight()
        else:
            if fight_question == 1:
                print("\nAs you attempt a flying armbar the boss smacks you midair and you land on your head. You are dead.")
            elif fight_question == 2:
                print("\nYou try a single leg and its successful. The boss falls to the ground")
                print("You pass his guard and get full mount. You attempt a mounted armbar")
                print("Your attempt fails and the boss ends up on top. He ground and pounds you into dust. You are dead.")
            elif fight_question == 4: 
                print("\nAs you attempt an inverted armbar from standing you fall on your neck and die.")
            elif fight_question == 3:
                print("\nYou do a guard pull from standing and you fall the the ground with the boss in your guard. The boss begins to throw strikes at you.")
                print("You cover up as several huge strikes are coming at you.")
                print("As the boss overextends on a punch you reach for it and you attempt an armbar from guard.")
                print("Its succesful! The boss screams in agony as he is forced to tap. You let go.")
                print("....")
                print("....")
                print("'You have defeated me...' the boss says.")
                print("The boss hands you keys to the Jiu-Jitsu Island Academy.\n")
                print("\nYOU\n")
                print("\nARE\n")
                print("\nNOW\n")
                print("\nTHE\n")
                print("\nBOSS\n")
            else:
                print("Please input only 1, 2, 3 or 4")
                boss_fight()

belt_check()