# Text-Based Adventure Game

> 2 versions of a retro text-based adventure game, inspired by the Netflix film Bandersnatch and games from before my time like Zork.

#### Versions
There are 2 versions of the game in this repo. One is written in Python - it was essentially my prototype. The other is in Java. Their functionality is not identical.

#### Python Version
This just runs as a console app, but the game is fully-developed. "Rooms" are defined as functions and each function is called when the player moves into a room. Converting this to Java was an interesting exercise because I was transitioning from a semi-functional approach to OOP.

#### Java Version
The game is not fully-fledged. You cannot lose or win, just interact with a few rooms. With this version my focus was on the GUI, which I developed with JavaFX.

#### Gameplay
The player is fed prompts and takes action by typing intuitive commands. You can move between rooms, pick up and drop items - thus adding and removing them from your inventory, interact with fetaures of rooms and other gameplay characters, and fall into traps if you don't have the right items in your inventory to complete certain tasks. Additionally, you can only have a limited number of items in your inventory at a time. This means there is a specific sequence you must follow to win the game. You can type "help" to see some guidance.

#### Files
In this file you will find:
* **Python Version**
  * Just the single main.py file
* **Java Version**
  * *src* containing the Java files
  * Some more JavaFX things
  * A zip file in which you will find a runnable .jar file to demo the game

*Version 2.0*
