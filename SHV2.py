from sys import exit
import random


#INVENTORY

inventory = {
    'last_game_location': None,
    'cell_key': False,
    '2ndbasement': False,
    '2ndhallway': False,
    'hidden_key': False,
    'black_book': False,
    'chest': False,
    'health' : None,
    'damage' : None,
    'enemy': None,
    'enemy_health': None,
    'enemy_damage' : None,
    'medkit_count': None,
    'finish' : None,
}


#UI

UI = {
    'nope':
    """That's not going to work, try something else.
    """,
    'game_over':
    """
GAME OVER
Do you want to continue from checkpoint?
    """,
    'restart':
    """Would you like to restart?
    """
    }


OUTSIDE_UI = {
        'intro':
        """There are rumours of an abandoned house that
has hidden treasures inside, while looking for the house
you see a building appear out of nowhere.
Its small and only has 1 window and 1 door.
What will you do? """,

        'open_door':
        """You open the door and walk inside.
You are greeted by a butler.
He asks you to come have some tea in the kitchen.
As you walk into the kitchen the butler hits you over the head and you lose consciousness.""",

        'open_window':
        """The window is locked, you get hit over the head and lose consciousness.""",

        'knock_door':
        """A butler opens the door but then promptly asks you to leave the property.
You go home having achieved nothing other than having the manners to knock first.""",

        'knock_window':
        """You knock on the window and it shatters.
The butler shoots you on sight.
You died. Normal people knock on doors not windows.""",

        'give_up':
        """That's not going to work, you give up and go home."""
    }


BASEMENT_UI = {
    'intro':
    """You slowly regain consciousness and realize you are in a cell.""",

    'room':
    """
The cell is dark with just one small window for light.
You see a picture on the wall, also a note on the floor.""",

    'frame':
    """You walk over to the picture and see a picture of a landscape.
There is a sign in the painting saying 'flip me over'.
You flip over the picture and find a key and a note saying 'cell key'.
You take the key.""",

    'window':
    """You are too short to look out the window.""",

    'note':
    """You pickup the note, the note says:
\nYou have been detained for trespassing on private property.
You will be released when the master of the house returns.
He will then decide to press charges or not.
The butler""",

    'stairs':
    """You open the cell and head up some stairs.""",

    'locked':
    """The cell door is locked.""",

    'intro2':
    """You slowly regain consciousness and realize you are back in the cell.""",

    'room2':
    """
You see the picture on the wall, also the note on the floor.""",

    'frame2':
    """You walk over to the picture frame and see the words don't let the butler catch you again.
You flip over the frame and take the key to the cell.""",

    'note2':
    """You pickup the note, the note says:
\nYou have been detained for trespassing on private property.
You will be released when the master of the house returns.
If you persist to be a nuisance drastic measures will be taken.
The butler"""
}


HALLWAY_UI = {
    'intro':
    """You walk into a hallway with 3 doors.
The first door is to your left, there seems to be some noise coming from this door.
The second door is straight ahead of you, it looks like the front door.
The third door is to your right.
Which door will you take?""",

    'left_1':
    """You enter the door on your left.
This is the kitchen, you look around and hear someone behind.
You turn around to see the butler.
We Can't have you leaving before the master gets home' the butler says as he knocks you out.""",

    'left_2':
    """You enter the door on your left.
This is the kitchen, you look around and hear someone behind.
You turn around to see the butler.
It seems drastic measures must be taken.
The butler takes drastic measures and you died.
Your journey is over.""",

    'middle':
    """You open the second door and find yourself outside.
You take a couple steps forward and turn around to go back inside but the house has disappeared
You decide to give up and go home.""",

    'right':
    """You enter the door on your right.""",

    'else_1':
    """That is not going to work, you hear someone behind you.
You turn around to see the butler.
'We Can't have you leaving before the master gets home' the butler says as he knocks you out.""",

    'else_2':
    """That is not going to work, you hear someone behind you.
You turn around to see the butler.
It seems drastic measures must be taken.
The butler takes drastic measures and you died.")
Your journey is over."""

}


STUDY_UI = {
    'intro':
    """You are in the study.
There is a single desk in the middle of the room and a bookshelf against the wall.
What will you do next?""",

    'desk_1':
    """You have already checked this.""",

    'desk_2':
    """You walk over to the desk to check the draws.
One draw is empty and the other has a key.
You take the key.""",

    'bookshelf_1':
    """You open the bookshelf and use the master key to open the door.
There is a long set of stairs leading down into the darkness.
Will you walk down the stairs?""",

    'bookshelf_2':
    """You close the hidden door and close the bookshelf.""",

    'bookshelf_3':
    """You walk over to the bookshelf and browse through the books.
You notice that there is a black book with no writing on the cover.
You pull on the book and realize it's a switch, the bookshelf swings open to reveal a door.
The door is locked, you use the master key to open it.
There is a long set of stairs leading down into the darkness.
Will you walk down the stairs?""",

    'bookshelf_4':
    """You close the hidden door and close the bookshelf.""",

    'bookshelf_5':
    """You walk over to the bookshelf and browse through the books.
You notice that there is a black book with no writing on the cover.
You pull on the book and realize it's a switch, the bookshelf swings open to reveal a door.
The door is locked.
You close the bookshelf to look around the rest of the room.""",

    'bookshelf_6':
    """You open the bookshelf but the door is still locked.
You close the bookshelf to look around the rest of the room."""

}


DARK_ROOM_UI = {
    'intro':
    """You walk down the stairs and the door shuts behind you.
You check the door and it is locked, with no way back you continue to walk down the stairs.
Eventually you reach the bottom of the stairs and find yourself in a room.""",

    'room':
    """
In the room is a chest, a note and a door.""",

    'chest':
    """You walk over to the chest and open it.
Inside is 10 medkits, a sword and a key.
You take all the items inside the chest.""",

    'empty_chest':
    """The chest is empty.""",

    'note':
    """The note reads:

There is danger ahead.
Prepare yourself for battle.
Using 'fight' will start a fight.
Using 'attack' will attack the enemy.
Using 'medkit' will heal your wounds.
Using 'talk' will attempt to talk to enemy instead of fighting.
Using 'taunt' will taunt the enemy.""",

    'locked':
    """The door is locked.""",

    'unlocked':
    """You unlock the door and go into the next room."""
}


TROLL_ROOM_UI = {
    'intro':
    """You enter the next room and see a troll standing in front of the door.
You walk up to the troll and he says ' You no pass'.
What will you do?""",

    'fight':
    """You attack the troll and he attacks back, keep fighting to win.""",

    'talk':
    """You attempt to talk to the troll but he doesn't care, keep fighting to win.""",

    'taunt':
    f"""You try to taunt the troll but he hits you. You lose 5 HP.
Your HP is now {inventory['health']}.
Keep fighting to win.""",

    'else':
    f"""You stumble and fall accidently stabbing yourself.
You lose 10 HP, Your HP is now {inventory['health']}.
The troll laughs and swings his club at you manage to dodge him.
Keep fighting to win."""
}


COMBAT_UI = {
        'Guardian':
        """The Guardian has 0 HP left.
The Guardian is defeated.
You are free to take all the treasure you want.
With the guardian defeated a door appears and opens.""",

        'Troll':
         """The Troll has 0 HP left.
The Troll is defeated.
A sword falls from the troll's belt you pick it up and now do increased damage.
You open the door to the next room and carry on with your journey.
"""
}


TREASURE_ROOM_UI = {
    'intro':
    """You enter the next room to find it filled with treasure.
While staring at the treasure someone approaches you.
'Halt you are trespassing, this is a grave error on your part!' bellowed The Guardian.
Seems you are in trouble, now what?""",

    'fight':
    """You attack The Guardian, the fight for your life is on.""",

    'talk':
    """Oh you wish to talk.""",

    'else':
    f"""'What a rude human.' said The Guardian
The Guardian attacks you, you take damage.
You have {inventory['health']} HP left.
The fight for your life is on."""
}


TALK_UI = {
    'intro':
    """'Hmmm you are a strange human.'
'Alright then if you can answer my riddle I will let you leave with whatever you would like.'
'You measure my life in hours and I serve you by expiring.''
'I’m quick when I’m thin and slow when I’m fat.''
'The wind is my enemy.'""",

    'correct':
    """'Correct, well done human.'
You may take as much treasure as you wish and are free to leave, the exit is just behind me.""",

    'incorrect':
    """'That is incorrect, you fail human.'
'Now you will die' said The Guardian.
The fight for your life is on."""
}


END_UI = {
    'finish':
    """You collect up as much treasure as you can before heading towards the door.
There are stairs leading up towards the surface, you make your way up the stairs.
After a long walk up the stairs you eventually reach a door, you try open the door but feel it is stuck.
You push hard against the door, you manage to open the door and are finally out in the open air again.
You notice the house you entered, the front door opens a shadowy figure appears in the doorway.
You see the butler standing in the doorway waving to you as the house slowly disappears.

The house completely disappears, you head home having had one crazy adventure that no one will believe.

YOU WIN

Would you like to restart the game?
"""
}


#GAME LOCATIONS

OUTSIDE = 'outside'
BASEMENT = 'basement'
HALLWAY = 'hallway'
STUDY = 'study'
DARK_ROOM = 'dark_room'
TROLL_ROOM = 'troll_room'
COMBAT = 'combat'
TREASURE_ROOM = 'treasure_room'
TALK = 'talk'
END = 'end'
DEAD = 'game_over'


VALID_GAME_LOCATIONS = [OUTSIDE, BASEMENT, HALLWAY, STUDY, DARK_ROOM, TROLL_ROOM, COMBAT, TREASURE_ROOM, TALK, END, DEAD]


#GAME ENGINE

def game_loop(initial_game_location):


    current_game_location = initial_game_location


    while True:
        if current_game_location == OUTSIDE:
            current_game_location = outside(inventory)
        elif current_game_location == BASEMENT:
            current_game_location = basement(inventory)
        elif current_game_location == HALLWAY:
            current_game_location = hallway(inventory)
        elif current_game_location == STUDY:
            current_game_location = study(inventory)
        elif current_game_location == DARK_ROOM:
            current_game_location = dark_room(inventory)
        elif current_game_location == TROLL_ROOM:
            current_game_location = troll_room(inventory)
        elif current_game_location == COMBAT:
            current_game_location = combat(inventory)
        elif current_game_location == TREASURE_ROOM:
            current_game_location = treasure_room(inventory)
        elif current_game_location == TALK:
            current_game_location = talk(inventory)
        elif current_game_location == END:
            current_game_location = end(inventory)
        elif current_game_location == DEAD:
            current_game_location == game_over(inventory)


def parse_command(line, allowed_verbs, allowed_nouns):
    word = line.split(' ')
    for a in allowed_verbs:
        if word[0] == a:
            for b in allowed_nouns:
                if word[1] == b:
                    return True


def outside(inventory):
    inventory['last_game_location']= OUTSIDE
    print(OUTSIDE_UI['intro'])
    entry = input("\n> ")

    if parse_command(entry, allowed_verbs=["open","enter"], allowed_nouns=["door"]):
        print(OUTSIDE_UI['open_door'])
        print(BASEMENT_UI['intro'])
        return BASEMENT

    elif parse_command(entry, allowed_verbs=["open","enter"], allowed_nouns=["window"]):
        print(OUTSIDE_UI['open_window'])
        print(BASEMENT_UI['intro'])
        return BASEMENT

    elif parse_command(entry, allowed_verbs=["knock"], allowed_nouns=["door"]):
        print(OUTSIDE_UI['knock_door'])
        return DEAD

    elif parse_command(entry, allowed_verbs=["knock"], allowed_nouns=["window"]):
        print(OUTSIDE_UI['knock_window'])
        return DEAD
    else:
        print(OUTSIDE_UI['give_up'])
        return DEAD


def basement(inventory):
    inventory['last_game_location']= BASEMENT
    if not inventory['2ndbasement']:
        print(BASEMENT_UI['room'])
        print("Now what?")
        cell = input("\n>")

        if parse_command(cell, allowed_verbs=["look","check","inspect"], allowed_nouns=["picture","frame"]):
            print(BASEMENT_UI['frame'])
            inventory['cell_key'] = True
            return BASEMENT

        elif parse_command(cell, allowed_verbs=["look","check","inspect"], allowed_nouns=["window"]):
            print(BASEMENT_UI['window'])
            return BASEMENT

        elif parse_command(cell, allowed_verbs=["look","check","inspect","read","pickup"], allowed_nouns=["note"]):
            print(BASEMENT_UI['note'])
            return BASEMENT

        elif parse_command(cell, allowed_verbs=["open"], allowed_nouns=["cell","door"]):
            if inventory['cell_key']:
                print(BASEMENT_UI['stairs'])
                inventory['2ndbasement'] = True
                return HALLWAY

            else:
                print(BASEMENT_UI['locked'])
                return BASEMENT

        else:
            print(UI['nope'])
            return BASEMENT
    else:
        print(BASEMENT_UI['room2'])
        print("Now what?")
        cell = input("\n>")

        if parse_command(cell, allowed_verbs=["look","check","inspect"], allowed_nouns=["picture","frame"]):
            print(BASEMENT_UI['frame2'])
            inventory['cell_key'] = True
            return BASEMENT

        elif parse_command(cell, allowed_verbs=["look","check","inspect"], allowed_nouns=["window"]):
            print(BASEMENT_UI['window'])
            return BASEMENT

        elif parse_command(cell, allowed_verbs=["look","check","inspect","read","pickup"], allowed_nouns=["note"]):
            print(BASEMENT_UI['note2'])
            return BASEMENT

        elif parse_command(cell, allowed_verbs=["open"], allowed_nouns=["cell","door"]):
            if inventory['cell_key']:
                print(BASEMENT_UI['stairs'])

                return HALLWAY

            else:
                print(BASEMENT_UI['locked'])
                return BASEMENT

        else:
            print(UI['nope'])
            return BASEMENT


def hallway(inventory):

    inventory['last_game_location']= HALLWAY
    print(HALLWAY_UI['intro'])
    hallway = input("\n>")

    if parse_command(hallway, allowed_verbs=["first","left","1"], allowed_nouns=["door"]):
        if not inventory['2ndhallway']:
            print(HALLWAY_UI['left_1'])
            inventory['2ndhallway'] = True
            inventory['cell_key'] = False
            print(BASEMENT_UI['intro2'])
            return BASEMENT
        else:
            print(HALLWAY_UI['left_2'])
            return DEAD

    elif parse_command(hallway, allowed_verbs=["second","straight","2","middle"], allowed_nouns=["door"]) :
        print(HALLWAY_UI['middle'])
        return DEAD

    elif parse_command(hallway, allowed_verbs=["third","right","3"], allowed_nouns=["door"]):
        print(HALLWAY_UI['right'])
        return STUDY

    else:
        if not inventory['2ndhallway']:
            print(HALLWAY_UI['else_1'])
            inventory['2ndhallway'] = True
            inventory['cell_key'] = False
            print(BASEMENT_UI['intro2'])
            return BASEMENT

        else:
            print(HALLWAY_UI['else_2'])
            return DEAD


def study(inventory):
    inventory['last_game_location']= STUDY
    print(STUDY_UI['intro'])
    study = input("\n> ")

    if parse_command(study, allowed_verbs=["investigate","look","check","inspect","open"], allowed_nouns=["desk"]):
        if inventory['hidden_key']:
            print(STUDY_UI['desk_1'])
            return STUDY
        else:
            print(STUDY_UI['desk_2'])
            inventory['hidden_key'] = True
            return STUDY

    elif parse_command(study, allowed_verbs=["investigate","look","check","inspect","open"], allowed_nouns=["bookshelf"]):
        if inventory['hidden_key']:
            if inventory['black_book']:
                print(STUDY_UI['bookshelf_1'])
                stairs = input("\n>")
                if stairs == "yes":
                    print(DARK_ROOM_UI['intro'])
                    return DARK_ROOM
                elif stairs == "no":
                    print(STUDY_UI['bookshelf_2'])
                    return STUDY
                else:
                    print(UI['nope'])
                    print(STUDY_UI['bookshelf_4'])
                    return STUDY
            elif not inventory['black_book']:
                inventory['black_book'] = True
                print(STUDY_UI['bookshelf_3'])
                stairs = input("\n>")
                if stairs == "yes":
                    print(DARK_ROOM_UI['intro'])
                    return DARK_ROOM
                elif stairs == "no":
                    print(STUDY_UI['bookshelf_4'])
                    return STUDY
                else:
                    print(UI['nope'])
                    print(STUDY_UI['bookshelf_4'])
                    return STUDY
            else:
                print(UI['nope'])
                return STUDY


        elif not inventory['black_book']:
            inventory['black_book'] = True
            print(STUDY_UI['bookshelf_5'])
            return STUDY
        elif inventory['black_book']:
            print(STUDY_UI['bookshelf_6'])
            return STUDY
        else:
            print(UI['nope'])
            return STUDY

    else:
        print(UI['nope'])
        return STUDY


def dark_room(inventory):
    inventory['last_game_location']= DARK_ROOM
    print(DARK_ROOM_UI['room'])
    dark = input("\n>")

    if parse_command(dark, allowed_verbs=["investigate","look","check","inspect","open"], allowed_nouns=["chest"]):
        if inventory['chest']:
            print(DARK_ROOM_UI['empty_chest'])
            return DARK_ROOM

        else:
            print(DARK_ROOM_UI['chest'])
            inventory['chest'] = True
            return DARK_ROOM


    elif parse_command(dark, allowed_verbs=["investigate","look","check","inspect","read","pickup"], allowed_nouns=["note","sign"]):
        print(DARK_ROOM_UI['note'])
        return DARK_ROOM

    elif parse_command(dark, allowed_verbs=["open","unlock"], allowed_nouns=["door"]):
        if inventory['chest']:
            print(DARK_ROOM_UI['unlocked'])
            return TROLL_ROOM
        else:
            print(DARK_ROOM_UI['locked'])
            return DARK_ROOM
    else:
        print(UI['nope'])
        return DARK_ROOM


def troll_room(inventory):
    inventory['last_game_location']= TROLL_ROOM
    print(TROLL_ROOM_UI['intro'])

    inventory['health'] = 100
    inventory['damage'] = 10
    inventory['enemy'] = "Troll"
    inventory['enemy_health'] = 100
    inventory['enemy_damage'] = 10
    inventory['medkit_count'] = 10
    inventory['finish'] = TREASURE_ROOM

    battle = input("\n>")

    if battle == "fight" or battle == "attack":
        print(TROLL_ROOM_UI['fight'])
        return COMBAT

    elif battle == "talk":
        print(TROLL_ROOM_UI['talk'])
        return COMBAT

    elif battle == "taunt":
        inventory['health'] = inventory['health'] - 5
        print(f"""You try to taunt the troll but he hits you. You lose 5 HP.
Your HP is now {inventory['health']}.
Keep fighting to win.""")
        return COMBAT

    else:
        inventory['health'] = inventory['health'] - 10
        print(f"""You stumble and fall accidently stabbing yourself.
You lose 10 HP, Your HP is now {inventory['health']}.
The troll laughs and swings his club at you manage to dodge him.
Keep fighting to win.""")
        return COMBAT


def combat(inventory):

    fight = input("\n>")

    if fight == "attack" or fight == "fight":
        print(f"You attack the {inventory['enemy']}.")

        number = random.randint(0,9)

        if number == 1 or number == 2 or number == 3 or number == 4:
            print(f"You hit the {inventory['enemy']}.")
            inventory['enemy_health'] -= inventory['damage']

            if inventory['enemy_health'] <= 0:
                print(COMBAT_UI[inventory['enemy']])
                return inventory['finish']

            else:
                print(f"The {inventory['enemy']} has {inventory['enemy_health']} HP left.")
                return COMBAT

        elif number == 5 or number == 6 or number == 7:
            print(f"You hit the {inventory['enemy']}, it was a critical hit.")
            inventory['enemy_health'] -= inventory['damage']*2

            if inventory['enemy_health'] <= 0:
                print(COMBAT_UI[inventory['enemy']])
                return inventory['finish']

            else:
                print(f"The {inventory['enemy']} has {inventory['enemy_health']} HP left.")
                return COMBAT

        else:
            print(f"You didnt hit the {inventory['enemy']}.")
            print(f"The {inventory['enemy']} hit you.")
            inventory['health'] -= inventory['enemy_damage']

            if inventory['health'] <= 0:
                print("You have 0 HP left.")
                print(f"The {inventory['enemy']} has killed you.")
                print("Your journey ends here.")
                return DEAD

            else:
                print(f"You have {inventory['health']} HP left")
                print(f"The {inventory['enemy']} has {inventory['enemy_health']} HP left.")
                return COMBAT

    elif fight == "medkit":

        if inventory['medkit_count'] > 0:
            print("You use a medkit.")
            inventory['health'] += 10
            inventory['medkit_count'] -= 1
            print(f"You have {inventory['health']} HP left")
            print(f"You have {inventory['medkit_count']} medkits left.")
            return COMBAT

        else:
            print("You have no more medkits.")
            return COMBAT

    else:
        print("You stab yourself")
        inventory['health'] -= 10

        if inventory['health'] <= 0:
            print("You have 0 HP left.")
            print(f"The {inventory['enemy']} has killed you.")
            print("Your journey ends here.")
            return DEAD

        else:
            print(f"You have {inventory['health']} HP left")
            return COMBAT


def treasure_room(inventory):
    inventory['last_game_location']= TREASURE_ROOM
    inventory['damage'] = 30
    inventory['enemy'] = "Guardian"
    inventory['enemy_health'] = 200
    inventory['enemy_damage'] = 15
    inventory['finish'] = END

    print(TREASURE_ROOM_UI['intro'])
    treasure = input("\n>")

    if treasure == "talk":
        print(TREASURE_ROOM_UI['talk'])
        return TALK

    elif treasure == "attack" or treasure == "fight":
        print(TREASURE_ROOM_UI['fight'])
        return COMBAT

    else:
        inventory['health'] -= 25
        print(f"""'What a rude human.'said The Guardian
The Guardian attacks you, you take damage.
You have {inventory['health']} HP left.
The fight for your life is on.""")
        return COMBAT


def talk(inventory):
    print(TALK_UI['intro'])
    answer = input("\n>")
    if answer == "candle" or answer == "a candle":
        print(TALK_UI['correct'])
        return END

    else:
        print(TALK_UI['incorrect'])
        return COMBAT


def end(inventory):
    print(END_UI['finish'])
    restart = input(">")
    if restart == "yes":
        inventory['cell_key'] = False
        inventory['2ndbasement'] = False
        inventory['2ndhallway'] = False
        inventory['hidden_key'] = False
        inventory['black_book'] = False
        inventory['chest'] = False
        game_loop(OUTSIDE)
    else:
        print("Goodbye.")
        exit(0)


def game_over(inventory):
    print(UI['game_over'])
    checkpoint = input(">")

    if checkpoint == "yes":
        game_loop(inventory['last_game_location'])

    elif checkpoint == "no":
        print(UI['restart'])
        restart = input(">")

        if restart == "yes":
            inventory['cell_key'] = False
            inventory['2ndbasement'] = False
            inventory['2ndhallway'] = False
            inventory['hidden_key'] = False
            inventory['black_book'] = False
            inventory['chest'] = False
            game_loop(OUTSIDE)
        else:
            print("Goodbye.")
            exit(0)
    else:
        return DEAD





game_loop(OUTSIDE)
