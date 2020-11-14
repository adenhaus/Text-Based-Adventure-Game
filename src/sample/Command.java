package sample;

import java.util.Arrays;

import javafx.scene.paint.Color;

public class Command {
	
	public static void getInput(String line)
	{
		if (line.contains("start") && Objects.getCurrentRoom() == Objects.getStartRoom()) {
			Main.println(Objects.getCurrentRoom().toString());
		}
		
		// Move in between rooms
		else if (line.contains("west")) {
			
			if (Objects.getCurrentRoom() == Objects.getStartRoom()) {
				Main.println("You move west.");
				Objects.setCurrentRoom(Objects.getSecondRoom());
				Main.println(Objects.getCurrentRoom().toString());
				Objects.incrementCount();
			} else if (Objects.getCurrentRoom() == Objects.getSecondRoom()) {
				Main.println("You cannot go that way.");
				Objects.incrementCount();
			}
			
		} else if (line.contains("east")) {
			
			if (Objects.getCurrentRoom() == Objects.getStartRoom()) {
				Main.println("You cannot go that way.");
				Objects.incrementCount();
			} else if (Objects.getCurrentRoom() == Objects.getSecondRoom()) {
				Main.println("You move east.");
				Objects.setCurrentRoom(Objects.getStartRoom());
				Main.println(Objects.getCurrentRoom().toString());
				Objects.incrementCount();
			}
			
		} else if (line.contains("south")) {
			
			if (Objects.getCurrentRoom() == Objects.getStartRoom()) {
				Main.println("You cannot go that way.");
				Objects.incrementCount();
			} else if (Objects.getCurrentRoom() == Objects.getSecondRoom()) {
				Main.println("You cannot go that way.");
				Objects.incrementCount();
			}
			
		} else if (line.contains("north")) {
			
			if (Objects.getCurrentRoom() == Objects.getStartRoom()) {
				Main.println("You cannot go that way.");
				Objects.incrementCount();
			} else if (Objects.getCurrentRoom() == Objects.getSecondRoom()) {
				Main.println("You cannot go that way.");
				Objects.incrementCount();
			}
			
		// Print current room
		} else if (line.contains("current room")) {
			
			Main.println(Objects.getCurrentRoom().getRoom());
			Objects.incrementCount();
			
		// Print inventory
		} else if (line.contains("inventory")) {
			
			if (Objects.getInventory().size() == 0) {
				Main.println("Your inventory is empty.");
				Objects.incrementCount();
			} else {
				Main.println(Arrays.toString(Objects.getInventory().toArray()));
				Objects.incrementCount();
			}
			
		// Take items
		} else if (line.contains("take")) {
			
			boolean inList = false;
			
			for (int i=0; i<Objects.getCurrentRoom().getItems().size(); i++) {
				String currentItem1 = Objects.getCurrentRoom().getItems().get(i);
			    if (line.contains(currentItem1)) {
			    	inList = true;
			    } else {
			    	continue;
			    }
			}
			
			if (Objects.getInventory().size() < 3) {
				
				if (inList) {
					for (int i=0; i<Objects.getCurrentRoom().getItems().size(); i++) {
						String currentItem = Objects.getCurrentRoom().getItems().get(i);
					    if (line.contains(currentItem)) {
					    	Objects.getCurrentRoom().removeItem(currentItem);
					    	Objects.addItem(currentItem);
					    	Main.println("You take the " + currentItem);
					    	break;
					    }
					}
					Objects.incrementCount();
				} else {
					Main.println("There is no such item in the room so you cannot take it...");
					Objects.incrementCount();
				}
				
			} else {
				Main.println("You can only carry 3 items at a time...");
			}
		
		// Drop items
		} else if (line.contains("drop")) {
			
			boolean inList = false;
			
			for (int i=0; i<Objects.getInventory().size(); i++) {
				String currentItem1 = Objects.getInventory().get(i);
			    if (line.contains(currentItem1)) {
			    	inList = true;
			    } else {
			    	continue;
			    }
			}
			
			if (inList) {
				for (int i=0; i<Objects.getInventory().size(); i++) {
					String currentItem = Objects.getInventory().get(i);
				    if (line.contains(currentItem)) {
				    	Objects.getCurrentRoom().addItem(currentItem);
				    	Objects.removeItem(currentItem);
				    	Main.println("You drop the " + currentItem);
				    	break;
				    }
				}
				Objects.incrementCount();
			} else {
				Main.println("That is not in your inventory so you cannot drop it...");
				Objects.incrementCount();
			}
		
		// Get help
		} else if (line.contains("help")) {
			
			Main.println("\nHere are some helpful commands you can use:\n"
					+ "- 'take' to add an item in the room to your inventory, e.g. 'take sword'\n"
					+ "- 'drop' to remove an item from your inventory, e.g. 'drop sword'\n"
					+ "- 'inventory' to view your in ventory.\n- move in between rooms by "
					+ "direction, e.g. 'move south'\n"
					+ "- 'dark' to change to dark mode\n"
					+ "- 'light' to change to light mode");
			Objects.incrementCount();
		
		// Dark mode
		} else if (line.contains("dark")) {
			Main.getScene().getStylesheets().add("file:Resources/application.css");
			Main.outputText.setFill(Color.WHITE);
			Main.topText.setFill(Color.WHITE);
			Main.room.setFill(Color.WHITE);
			Main.roomItems.setFill(Color.WHITE);
			Main.inventory.setFill(Color.WHITE);
			Main.moves.setFill(Color.WHITE);
			Main.border.setFill(Color.WHITE);
			Main.border2.setFill(Color.WHITE);
		} 
		
		// Light mode
		else if (line.contains("light")) {
			Main.getScene().getStylesheets().clear();
			Main.getScene().getStylesheets().add("file:Resources/application2.css");
			Main.outputText.setFill(Color.BLACK);
			Main.topText.setFill(Color.BLACK);
			Main.room.setFill(Color.BLACK);
			Main.roomItems.setFill(Color.BLACK);
			Main.inventory.setFill(Color.BLACK);
			Main.moves.setFill(Color.BLACK);
			Main.border.setFill(Color.BLACK);
			Main.border2.setFill(Color.BLACK);
		}
		
		// No errors!
		else {
			
			Main.println("You cannot do that...");
			Objects.incrementCount();
			
		}
	}

}
