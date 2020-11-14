package sample;

import java.util.ArrayList;
import java.util.Arrays;

public class GameState {
	
	// Fields
	private String name;
	private ArrayList<String> items;
	private String description;
	
	// Constructor
	public GameState(String name, ArrayList<String> items, String description) {
		this.name = name;
		this.items = items;
		this.description = description;
	}
	
	// Methods
	public String getRoom() {
		return name;
	}
	
	public ArrayList<String> getItems() {
		return items;
	}
	
	public void addItem(String item)
	{
		items.add(item);
	}
	
	public void removeItem(String item)
	{
		items.remove(item);
	}
	
	public String getDescription() {
		return description;
	}
	
	public String toString() {
		if (Objects.getCurrentRoom().getItems().size() > 0) {
			return "\n" + description + "\n" + "You see the following "
					+ "items in the room:\n" + Arrays.toString(items.toArray());
		} else {
			return "\n" + description;
		}
	}
}
