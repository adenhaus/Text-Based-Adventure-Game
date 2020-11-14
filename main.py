from random import random

# LISTS ================================================================================================================
inventory = []

move_verbs = ["walk", "go", "advance", "move", "run", "head"]
take_verbs = ["take", "grab", "steal"]
drop_verbs = ["abandon", "leave", "drop"]
use_verbs = ["use"]

items_in_dungeon = ["parchment", "sword"]
items_in_passage = ["lantern"]
items_in_armor_room = ["armor"]
items_in_key_room = ["key"]
items_in_locked_room = []
items_in_secret_passage = []
items_in_monster_room = []

riddles = ["I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, but water kills me. "
           "What am I?",

           "What runs around the whole yard without moving?",

           "A bus driver was heading down a street in Colorado. He went right past a stop sign without stopping, "
           "he turned left where there was a 'no left turn' sign, and he went the wrong way on a one-way street. Then "
           "he went on the left side of the road past a cop car. Still - he didn't break any traffic laws. Why not?",

           "What can you catch but never throw?",
           ]

# FUNCTIONS ============================================================================================================

# Dungeon --------------------------------------------------------------------------------------------------------------


def dungeon():
    print("You find yourself in a dungeon.\nThere is a passageway to "
          "the North and a door to the East.")
    if len(items_in_dungeon) > 0:
        print("You see the following items in the room: " + ", ".join(items_in_dungeon))
    else:
        print("There are no items in the room.")

    not_moved = True
    while not_moved:
        move = input("> ").lower()

        verb = "/"

        # Drop
        drop_verb = "/"
        for b in drop_verbs:

            if b in move:
                drop_verb = b
                break

        # Take Items
        take_verb = "/"
        for i in take_verbs:

            if i in move:
                take_verb = i
                break

        # Move Around
        for i in move_verbs:
            if i in move and "north" in move:
                verb = i
                break

            elif i in move and "east" in move:
                verb = i
                break

        # Move Rooms
        if verb in move and "north" in move:
            print("You head North into the passageway.\n")
            not_moved = False
            passage()

        elif verb in move and "east" in move:
            print("You head East through the doorway.\n")
            not_moved = False
            key_room()

        elif verb in move and "west" in move or "south" in move:
            print("You can't do that.")

        # Take Items
        elif take_verb in move:
            while True:

                for x in items_in_dungeon:

                    if x in move and "read" not in move:
                        take_item = x
                        if len(inventory) < 3:
                            print("You " + take_verb + " the " + take_item + ".")
                            inventory.append(take_item)
                            items_in_dungeon.remove(take_item)
                            break
                        else:
                            print("You can only have 3 items in your inventory at a time.")
                    else:
                        pass
                break

        # Drop Items
        elif drop_verb in move:
            dropped = True
            while dropped:

                for a in inventory:

                    if a in move and "read" not in move:
                        drop_item = a
                        print("You " + drop_verb + " the " + drop_item + ".")
                        inventory.remove(drop_item)
                        items_in_dungeon.append(drop_item)
                break

        # Read parchment
        elif "read" in move and "parchment" in move and "parchment" in inventory:
            print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                  "escape.\n")

        elif "read" in move and "parchment" in move and "parchment" not in inventory:
            print("You don't have the parchment in your inventory.")

        # View Inventory
        elif "inventory" in move:
            if len(inventory) > 0:
                print("Your inventory contains: \n" + "\n".join(inventory))
            else:
                print("Your inventory is empty.")

        else:
            print("You cannot do that.")


# Passage --------------------------------------------------------------------------------------------------------------


def passage():
    print("You are in a narrow hallway.\nFurther North you see some light.")
    if len(items_in_passage) > 0:
        print("You see the following items in the room: " + ", ".join(items_in_passage))
    else:
        print("There are no items in the room.")

    not_moved = True
    while not_moved:
        move = input("> ").lower()

        verb = "/"

        # Drop
        drop_verb = "/"
        for b in drop_verbs:

            if b in move:
                drop_verb = b
                break

        # Take Items
        take_verb = "/"
        for i in take_verbs:

            if i in move:
                take_verb = i
                break

        # Move Around
        for i in move_verbs:
            if i in move and "north" in move:
                verb = i
                break

            elif i in move and "south" in move:
                verb = i
                break

        # Move Rooms
        if verb in move and "north" in move:
            print("You head North towards the light source.\n")
            not_moved = False
            armor_room()

        elif verb in move and "south" in move:
            print("You head back the way you came.\n")
            not_moved = False
            dungeon()

        elif verb in move and "west" in move or "east" in move:
            print("You can't do that.")

        # Take Items
        elif take_verb in move:
            while True:

                for x in items_in_passage:

                    if x in move and "read" not in move:
                        take_item = x
                        if len(inventory) < 3:
                            print("You " + take_verb + " the " + take_item + ".")
                            inventory.append(take_item)
                            items_in_passage.remove(take_item)
                            break
                        else:
                            print("You can only have 3 items in your inventory at a time.")
                break

        # Drop Items
        elif drop_verb in move:
            dropped = True
            while dropped:

                for a in inventory:

                    if a in move and "read" not in move:
                        drop_item = a
                        print("You " + drop_verb + " the " + drop_item + ".")
                        inventory.remove(drop_item)
                        items_in_passage.append(drop_item)
                break

        # Read parchment
        elif "read" in move and "parchment" in move and "parchment" in inventory:
            print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                  "escape.\n")

        elif "read" in move and "parchment" in move and "parchment" not in inventory:
            print("You don't have the parchment in your inventory.")

        # View Inventory
        elif "inventory" in move:
            if len(inventory) > 0:
                print("Your inventory contains: \n" + "\n".join(inventory))
            else:
                print("Your inventory is empty.")

        else:
            print("You cannot do that.")


# Armor Room -----------------------------------------------------------------------------------------------------------


def armor_room():
    print("You are in another cell. The light you saw was coming from a window, which is too high to reach.\n"
          "To the West there is a door, but it is barred shut.\nTo your surprise, you see another prisoner "
          "chained to the wall. He has some armor.")
    if len(items_in_armor_room) > 0:
        print("You see the following items in the room: " + ", ".join(items_in_armor_room))
    else:
        print("There are no items in the room.")

    not_moved = True
    while not_moved:
        move = input("> ").lower()

        verb = "/"

        # Drop
        drop_verb = "/"
        for b in drop_verbs:

            if b in move:
                drop_verb = b
                break

        # Take Items
        take_verb = "/"
        for i in take_verbs:

            if i in move:
                take_verb = i
                break

        # Move Around
        for i in move_verbs:
            if i in move and "west" in move:
                verb = i
                break

            elif i in move and "south" in move:
                verb = i
                break

        # Move Rooms
        if verb in move and "west" in move:
            print("The door is barred shut.")

        elif verb in move and "south" in move:
            print("You head back into the passage.\n")
            not_moved = False
            passage()

        elif verb in move and "east" in move or "north" in move:
            print("You can't do that.")

        # Take Items
        elif take_verb in move:
            while True:

                for x in items_in_armor_room:

                    if x in move and "read" not in move:
                        take_item = x
                        if len(inventory) < 3:
                            if x != "armor":
                                print("You " + take_verb + " the " + take_item + ".")
                                inventory.append(take_item)
                                items_in_armor_room.remove(take_item)
                                break
                            elif x == "armor":
                                print("The prisoner will not give you his armor. You must negotiate with him.")
                        else:
                            print("You can only have 3 items in your inventory at a time.")
                break

        # Drop Items
        elif drop_verb in move:
            dropped = True
            while dropped:

                for a in inventory:

                    if a in move and "read" not in move:
                        drop_item = a
                        print("You " + drop_verb + " the " + drop_item + ".")
                        inventory.remove(drop_item)
                        items_in_armor_room.append(drop_item)
                break

        # Read parchment
        elif "read" in move and "parchment" in move and "parchment" in inventory:
            print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                  "escape.\n")

        elif "read" in move and "parchment" in move and "parchment" not in inventory:
            print("You don't have the parchment in your inventory.")

        # View Inventory
        elif "inventory" in move:
            if len(inventory) > 0:
                print("Your inventory contains: \n" + "\n".join(inventory))
            else:
                print("Your inventory is empty.")

        elif "negotiate" in move or "speak" in move:
            print("The prisoner says, 'I have been here for years, and I get very bored. I am so pleased to see "
                  "another soul. I assume you want my armor. Well, you'll have to solve a riddle for it!'\nDo you want "
                  "to attempt to solve the old man's riddle?")

            riddle = input("> ").lower()

            if riddle == "yes":
                print("I am not alive, but I grow; I don't have lungs, but I need air; I don't have a mouth, "
                      "but water kills me. What am I?")
                while True:
                    ans = input("> ").lower()
                    if "fire" in ans:
                        print("Correct! The prisoner gives you his armor.")
                        if len(inventory) < 3:
                            inventory.append("armor")
                            items_in_armor_room.remove("armor")
                            break
                        else:
                            print("You can only have 3 items in your inventory at a time!")
                    else:
                        print("Try again...")
            else:
                print("You choose not to engage in riddling.")

        else:
            print("You cannot do that.")


# Key Room -------------------------------------------------------------------------------------------------------------


def key_room():
    if "armor" in inventory:

        print("You fall into a spiked trap, but luckily you are wearing the old prisoner's armor, and you survive. "
              "Once you climb back out, you notice that you are in a holding cell.\nThere is a door to the North.")

        if len(items_in_key_room) > 0:
            print("You see the following items in the room: " + ", ".join(items_in_key_room))
        else:
            print("There are no items in the room.")

        not_moved = True
        while not_moved:
            move = input("> ").lower()

            verb = "/"

            # Drop
            drop_verb = "/"
            for b in drop_verbs:

                if b in move:
                    drop_verb = b
                    break

            # Take Items
            take_verb = "/"
            for i in take_verbs:

                if i in move:
                    take_verb = i
                    break

            # Move Around
            for i in move_verbs:
                if i in move and "north" in move:
                    verb = i
                    break

                elif i in move and "west" in move:
                    verb = i
                    break

            # Move Rooms
            if verb in move and "north" in move:
                print("The door is locked.")
                door = input("> ").lower()
                if "unlock" in door or "open" in door:
                    if "key" in inventory:
                        print("")
                        not_moved = False
                        locked_room()
                    else:
                        print("You do not have the key.")

            elif verb in move and "west" in move:
                print("You head back into the dungeon.\n")
                not_moved = False
                dungeon()

            elif verb in move and "south" in move or "east" in move:
                print("You can't do that.")

            # Take Items
            elif take_verb in move:
                while True:

                    for x in items_in_key_room:

                        if x in move and "read" not in move:
                            take_item = x
                            if len(inventory) < 3:
                                print("You " + take_verb + " the " + take_item + ".")
                                inventory.append(take_item)
                                items_in_key_room.remove(take_item)
                                break
                            else:
                                print("You can only have 3 items in your inventory at a time.")
                    break

            # Drop Items
            elif drop_verb in move:
                dropped = True
                while dropped:

                    for a in inventory:

                        if a in move and "read" not in move:
                            drop_item = a
                            print("You " + drop_verb + " the " + drop_item + ".")
                            inventory.remove(drop_item)
                            items_in_key_room.append(drop_item)
                    break

            # Read parchment
            elif "read" in move and "parchment" in move and "parchment" in inventory:
                print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                      "escape.\n")

            elif "read" in move and "parchment" in move and "parchment" not in inventory:
                print("You don't have the parchment in your inventory.")

            # View Inventory
            elif "inventory" in move:
                if len(inventory) > 0:
                    print("Your inventory contains: \n" + "\n".join(inventory))
                else:
                    print("Your inventory is empty.")

            else:
                print("You cannot do that.")

    else:
        print("You fall into a hidden trap and die a painful death.\nGAME OVER")


# Key Room from Locked Room --------------------------------------------------------------------------------------------


def key_room_2():

    print("The door slams shut behind you and locks again. You are back in the holding cell.\nThere is a door to the "
          "North and a doorway to the West")

    if len(items_in_key_room) > 0:
        print("You see the following items in the room: " + ", ".join(items_in_key_room))
    else:
        print("There are no items in the room.")

    not_moved = True
    while not_moved:
        move = input("> ").lower()

        verb = "/"

        # Drop
        drop_verb = "/"
        for b in drop_verbs:

            if b in move:
                drop_verb = b
                break

        # Take Items
        take_verb = "/"
        for i in take_verbs:

            if i in move:
                take_verb = i
                break

        # Move Around
        for i in move_verbs:
            if i in move and "north" in move:
                verb = i
                break

            elif i in move and "west" in move:
                verb = i
                break

        # Move Rooms
        if verb in move and "north" in move:
            print("The door is locked.")
            door = input("> ").lower()
            if "unlock" in door or "open" in door:
                if "key" in inventory:
                    print("")
                    not_moved = False
                    locked_room()
                else:
                    print("You do not have the key.")

        elif verb in move and "west" in move:
            print("You head back into the dungeon.\n")
            not_moved = False
            dungeon()

        elif verb in move and "south" in move or "east" in move:
            print("You can't do that.")

        # Take Items
        elif take_verb in move:
            while True:

                for x in items_in_key_room:

                    if x in move and "read" not in move:
                        take_item = x
                        if len(inventory) < 3:
                            print("You " + take_verb + " the " + take_item + ".")
                            inventory.append(take_item)
                            items_in_key_room.remove(take_item)
                            break
                        else:
                            print("You can only have 3 items in your inventory at a time.")
                break

        # Drop Items
        elif drop_verb in move:
            dropped = True
            while dropped:

                for a in inventory:

                    if a in move and "read" not in move:
                        drop_item = a
                        print("You " + drop_verb + " the " + drop_item + ".")
                        inventory.remove(drop_item)
                        items_in_key_room.append(drop_item)
                break

        # Read parchment
        elif "read" in move and "parchment" in move and "parchment" in inventory:
            print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                  "escape.\n")

        elif "read" in move and "parchment" in move and "parchment" not in inventory:
            print("You don't have the parchment in your inventory.")

        # View Inventory
        elif "inventory" in move:
            if len(inventory) > 0:
                print("Your inventory contains: \n" + "\n".join(inventory))
            else:
                print("Your inventory is empty.")

        else:
            print("You cannot do that.")


# Locked Room ----------------------------------------------------------------------------------------------------------


def locked_room():
    if "lantern" in inventory:

        print("You enter a room that is totally dark.")

        not_moved = True
        while not_moved:
            move = input("> ").lower()

            if "lantern" in move:

                print("The lantern flickers into life, and to the West, you can barely make out what looks "
                      "like a tunnel.")
                if len(items_in_locked_room) > 0:
                    print("You see the following items in the room: " + ", ".join(items_in_locked_room))
                else:
                    print("There are no items in the room.")

                not_moved = True
                while not_moved:

                    lantern = input("> ").lower()

                    verb = "/"

                    # Drop
                    drop_verb = "/"
                    for b in drop_verbs:

                        if b in lantern:
                            drop_verb = b
                            break

                    # Take Items
                    take_verb = "/"
                    for i in take_verbs:

                        if i in lantern:
                            take_verb = i
                            break

                    # Move Around
                    for i in move_verbs:
                        if i in lantern and "south" in lantern:
                            verb = i
                            break

                        elif i in lantern and "west" in lantern:
                            verb = i
                            break

                    # Move Rooms
                    if verb in lantern and "west" in lantern:
                        print("You enter the dark tunnel...")
                        not_moved = False
                        secret_passage()

                    elif verb in lantern and "south" in lantern:
                        print("You head back into the holding cell.\n")
                        not_moved = False
                        key_room_2()

                    elif verb in lantern and "east" in lantern or "north" in lantern:
                        print("You can't do that.")

                    # Take Items
                    elif take_verb in lantern:
                        while True:

                            for x in items_in_locked_room:

                                if x in lantern and "read" not in lantern:
                                    take_item = x
                                    if len(inventory) < 3:
                                        print("You " + take_verb + " the " + take_item + ".")
                                        inventory.append(take_item)
                                        items_in_locked_room.remove(take_item)
                                        break
                                    else:
                                        print("You can only have 3 items in your inventory at a time.")
                            break

                    # Drop Items
                    elif drop_verb in lantern:
                        dropped = True
                        while dropped:

                            for a in inventory:

                                if a in lantern and "read" not in lantern:
                                    drop_item = a
                                    print("You " + drop_verb + " the " + drop_item + ".")
                                    inventory.remove(drop_item)
                                    items_in_locked_room.append(drop_item)
                            break

                    # Read parchment
                    elif "read" in lantern and "parchment" in lantern and "parchment" in inventory:
                        print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that "
                              "will help you "
                              "escape.\n")

                    elif "read" in lantern and "parchment" in lantern and "parchment" not in inventory:
                        print("You don't have the parchment in your inventory.")

                    # View Inventory
                    elif "inventory" in lantern:
                        if len(inventory) > 0:
                            print("Your inventory contains: \n" + "\n".join(inventory))
                        else:
                            print("Your inventory is empty.")

            else:
                print("It is too dark to do that.")
    else:
        print("You enter a room that is totally dark.")

        not_moved = True
        while not_moved:
            move = input("> ")

            verb = "/"

            # Move Around
            for i in move_verbs:
                if i in move and "south" in move:
                    verb = i
                    break

            if verb in move and "south" in move:
                print("You head back into the room where you found the key.\n")
                not_moved = False
                key_room()

            else:
                print("It is too dark to do that.")


# Secret Passage -------------------------------------------------------------------------------------------------------


def secret_passage():
    print("\nYou are in a secret passageway with a low ceiling.\nIt is very long, and you cannot see what "
          "lies further West.")
    if len(items_in_secret_passage) > 0:
        print("You see the following items in the room: " + ", ".join(items_in_secret_passage))
    else:
        print("There are no items in the room.")

    not_moved = True
    while not_moved:
        move = input("> ").lower()

        verb = "/"

        # Drop
        drop_verb = "/"
        for b in drop_verbs:

            if b in move:
                drop_verb = b
                break

        # Take Items
        take_verb = "/"
        for i in take_verbs:

            if i in move:
                take_verb = i
                break

        # Move Around
        for i in move_verbs:
            if i in move and "west" in move:
                verb = i
                break

            elif i in move and "east" in move:
                verb = i
                break

        # Move Rooms
        if verb in move and "west" in move:
            print("You continue West down the tunnel into the unknown....\n")
            not_moved = False
            monster_room()

        elif verb in move and "east" in move:
            print("You flee back into the locked room.\n")
            not_moved = False
            key_room()

        elif verb in move and "north" in move or "south" in move:
            print("You can't do that.")

        # Take Items
        elif take_verb in move:
            while True:

                for x in items_in_secret_passage:

                    if x in move and "read" not in move:
                        take_item = x
                        if len(inventory) < 3:
                            print("You " + take_verb + " the " + take_item + ".")
                            inventory.append(take_item)
                            items_in_secret_passage.remove(take_item)
                            break
                        else:
                            print("You can only have 3 items in your inventory at a time.")
                    else:
                        pass
                break

        # Drop Items
        elif drop_verb in move:
            dropped = True
            while dropped:

                for a in inventory:

                    if a in move and "read" not in move:
                        drop_item = a
                        print("You " + drop_verb + " the " + drop_item + ".")
                        inventory.remove(drop_item)
                        items_in_secret_passage.append(drop_item)
                break

        # Read parchment
        elif "read" in move and "parchment" in move and "parchment" in inventory:
            print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                  "escape.\n")

        elif "read" in move and "parchment" in move and "parchment" not in inventory:
            print("You don't have the parchment in your inventory.")

        # View Inventory
        elif "inventory" in move:
            if len(inventory) > 0:
                print("Your inventory contains: \n" + "\n".join(inventory))
            else:
                print("Your inventory is empty.")

        else:
            print("You cannot do that.")


# Monster Room ---------------------------------------------------------------------------------------------------------


def monster_room():

    print("You reach the end of the secret tunnel and find yourself in a massive underground cavern.\nTo the "
          "North you see an archway, and through it - light! You have found the way out!")
    if len(items_in_monster_room) > 0:
        print("You see the following items in the room: " + ", ".join(items_in_monster_room))
    else:
        pass

    not_moved = True
    while not_moved:
        move = input("> ").lower()

        verb = "/"

        # Drop
        drop_verb = "/"
        for b in drop_verbs:

            if b in move:
                drop_verb = b
                break

        # Take Items
        take_verb = "/"
        for i in take_verbs:

            if i in move:
                take_verb = i
                break

        # Move Around
        for i in move_verbs:
            if i in move and "north" in move:
                verb = i
                break

            elif i in move and "south" in move:
                verb = i
                break

        # Move Rooms
        if verb in move and "north" in move:
            print("You run towards the exit, freedom is within your sight!\n")

            if "armor" in inventory and "sword" in inventory:
                print("But suddenly, the ground begins to shake beneath your feet. A monstrous wail shakes the "
                      "cavern's stone walls.\nA monster appears from the dark, blocking your path to the arch!")

                monster = input("> ").lower()

                if "north" in monster or "fight" in monster:
                    print("You use your sword and armor to fight and kill the demon! Now you can escape the dungeon."
                          "\n\nYOU WIN")
                    not_moved = False
                elif "south" in monster:
                    print("You cower back into the secret passage.\n")
                    not_moved = False
                    secret_passage()
                else:
                    print("You can't do that.")

            else:
                print("But suddenly, the ground begins to shake beneath your feet. A monstrous wail shakes the "
                      "cavern's stone walls.\nA monster appears from the dark, blocking your path to the arch!")
                monster = input("> ").lower()
                print("It is no use, you can neither fight the demon nor escape before it catches you. It rips "
                      "you apart.")
                break

        elif verb in move and "south" in move:
            print("You cower back into the secret passage.\n")
            not_moved = False
            secret_passage()

        elif verb in move and "north" in move or "south" in move:
            print("You can't do that.")

        # Take Items
        elif take_verb in move:
            while True:

                for x in items_in_monster_room:

                    if x in move and "read" not in move:
                        take_item = x
                        if len(inventory) < 3:
                            print("You " + take_verb + " the " + take_item + ".")
                            inventory.append(take_item)
                            items_in_monster_room.remove(take_item)
                            break
                        else:
                            print("You can only have 3 items in your inventory at a time.")
                break

        # Drop Items
        elif drop_verb in move:
            dropped = True
            while dropped:

                for a in inventory:

                    if a in move and "read" not in move:
                        drop_item = a
                        print("You " + drop_verb + " the " + drop_item + ".")
                        inventory.remove(drop_item)
                        items_in_monster_room.append(drop_item)
                break

        # Read parchment
        elif "read" in move and "parchment" in move and "parchment" in inventory:
            print("You read the parchment. It says:\n\nWelcome to the dungeon. This is a manual that will help you "
                  "escape.\n")

        elif "read" in move and "parchment" in move and "parchment" not in inventory:
            print("You don't have the parchment in your inventory.")

        # View Inventory
        elif "inventory" in move:
            if len(inventory) > 0:
                print("Your inventory contains: \n" + "\n".join(inventory))
            else:
                print("Your inventory is empty.")

        else:
            print("You cannot do that.")


# GAME =================================================================================================================

print("Welcome to Dungeon Escape, a Text-Based Adventure Game.\n\nType 'start' to begin...")
start = input("> ")
if start == "start":
    print("\n")
    dungeon()
