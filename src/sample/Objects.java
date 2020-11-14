package sample;

import java.util.ArrayList;

public class Objects {
	
	// Create item arrays
	private static ArrayList<String> itemsInStartRoom = new ArrayList<String>() { 
        { 
            add("parchment");
            add("sword");
            add("bottle"); 
        }
    };
    
    private static ArrayList<String> itemsInSecondRoom = new ArrayList<String>() { 
        { 
            add("armor");
            add("bread");
            add("cap"); 
        } 
    };
    
    private static ArrayList<String> inventory = new ArrayList<String>();

    // Create rooms
	public static GameState startRoom = new GameState("Start Room", itemsInStartRoom, 
			"You are in a dark and mouldy dungeon.\nThe only illumination is coming from a small "
			+ "barred window,\ntoo high for you to reach.\nTo the west, however, there is a doorway.");
	public static GameState secondRoom = new GameState("Second Room", itemsInSecondRoom, 
			"You are in another dungeon!");
	public static GameState currentRoom = startRoom;
	
	// Move counter
	public static int count;
	
	// Methods
	public static int getCount() {
		return count;
	}
	
	public static void incrementCount() {
		count += 1;
	}
	
	public static GameState getCurrentRoom() {
		return currentRoom;
	}
	
	public static GameState getStartRoom() {
		return startRoom;
	}
	
	public static GameState getSecondRoom() {
		return secondRoom;
	}
	
	public static void setCurrentRoom(GameState room) {
		currentRoom = room;
	}
	
	public static ArrayList<String> getInventory() {
		return inventory;
	}
	
	public static void addItem(String item)
	{
		inventory.add(item);
	}
	
	public static void removeItem(String item)
	{
		inventory.remove(item);
	}


}
