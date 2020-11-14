package sample;
	
import javafx.scene.control.ScrollPane;
import javafx.scene.control.ScrollPane.ScrollBarPolicy;
import javafx.scene.control.TextField;
import javafx.scene.input.KeyCode;
import javafx.scene.input.KeyEvent;
import javafx.animation.Animation;
import javafx.animation.FadeTransition;
import javafx.animation.KeyFrame;
import javafx.animation.KeyValue;
import javafx.animation.Timeline;
import javafx.application.Application;
import javafx.embed.swing.JFXPanel;
import javafx.event.EventHandler;
import javafx.geometry.Insets;
import javafx.geometry.Pos;
import javafx.stage.Stage;
import javafx.util.Duration;
import javafx.scene.Scene;
import javafx.scene.layout.ColumnConstraints;
import javafx.scene.layout.GridPane;
import javafx.scene.layout.VBox;
import javafx.scene.paint.Color;
import javafx.scene.text.Font;
import javafx.scene.text.Text;

public class Main extends Application {
	
	final JFXPanel fxPanel = new JFXPanel();
	
	public static void main(String[] args) {
		final JFXPanel fxPanel = new JFXPanel();
		launch(args);
	}
	
	// Create Scene
	public static Scene scene2;
	
	// Create text fields
	public static Text outputText = new Text();
	public static Text topText = new Text();
	public static TextField inputText = new TextField();
	
	// Grid test
	public static Text room = new Text();
	public static Text roomItems = new Text();
	public static Text inventory = new Text();
	public static Text moves = new Text();
	public static Text border = new Text();
	public static Text border2 = new Text();
	
	@Override
	public void start(Stage primaryStage) {
		
		final JFXPanel fxPanel = new JFXPanel();
		
		GridPane grid = new GridPane();
	    grid.setHgap(0);
	    grid.setVgap(5);
	    grid.setPadding(new Insets(0, 0, 0, 0));
	    
	    ColumnConstraints col1 = new ColumnConstraints();
        col1.setPercentWidth(25);
        ColumnConstraints col2 = new ColumnConstraints();
        col2.setPercentWidth(25);
        grid.getColumnConstraints().addAll(col1,col2);
        
	    // Category in column 2, row 1
	    room.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
	    grid.add(inventory, 0, 0);
	    
	    // Category in column 2, row 1
	    moves.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
	    grid.add(roomItems, 0, 1);
	    
	    // Category in column 2, row 1
	    inventory.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
	    grid.add(room, 1, 0);
	    
	    // Category in column 2, row 1
	    roomItems.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
	    grid.add(moves, 1, 1);
	    
	    // Category in column 2, row 1
	    border.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
	    grid.add(border, 0, 2);
	    
	    // Category in column 2, row 1
	    border2.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
	    grid.add(border2, 1, 2);
		
	    
	    
		// Text Field
		inputText.setPromptText("Type a command...");
		
		// Text display
		outputText.setFill(Color.BLACK);
		outputText.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
		
		// Top bar
		topText.setFill(Color.BLACK);
		topText.setFont(Font.loadFont("file:Resources/basis33.ttf", 20));
		topText.setText("");
		
		// Scroll
		ScrollPane scroll = new ScrollPane(outputText);
		// scroll.fitToWidthProperty().set(true);
		scroll.setHbarPolicy(ScrollBarPolicy.NEVER);
		scroll.setVbarPolicy(ScrollBarPolicy.NEVER);
		scroll.setVvalue(1D);
		
		// VBox
		VBox layout = new VBox();
		layout.setPadding(new Insets(20, 20, 20, 20));
		layout.setAlignment(Pos.BOTTOM_LEFT);
		layout.getChildren().addAll(grid, topText, scroll, inputText);
		
		// Scene
		scene2 = new Scene(layout, 1000, 600, Color.WHITE);
		scene2.getStylesheets().add("file:Resources/application2.css");
		
		// Responsive text
		outputText.wrappingWidthProperty().bind(scene2.widthProperty().subtract(40));
		
		// EVENTS ================================================
		
		// Take Input
		inputText.setOnKeyPressed(new EventHandler<KeyEvent>() {
		    @Override
		    public void handle(KeyEvent keyEvent) {
		        if (keyEvent.getCode() == KeyCode.ENTER)  {
		            String input = "> " + inputText.getText();
		            
		            // String currentText = outputText.getText() + "\n";
		            // outputText.setText(currentText + input);
		            
		            onInput(input);
		            
		            // Clear input text
		            inputText.setText("");
		            
		            // Scroll to bottom
		            scrollAnimation(scroll);
		        }
		    }
		});
		
		// SET SCENE =============================================
		
		primaryStage.setScene(scene2);
		primaryStage.setTitle("Text-Based Game");
		// primaryStage.setResizable(false);
		primaryStage.show();
		
		// Set up a fade-in animation
        FadeTransition trans = new FadeTransition(Duration.seconds(5), inputText);
        trans.setFromValue(0);
        trans.setToValue(1);
        // Let the animation run forever
        trans.setCycleCount(1);
        // Play the Animation
        trans.play();
        
        // Set up a fade-in animation
        FadeTransition trans2 = new FadeTransition(Duration.seconds(5), outputText);
        trans2.setFromValue(0);
        trans2.setToValue(1);
        // Let the animation run forever
        trans2.setCycleCount(1);
        // Play the Animation
        trans2.play();
		
		initGame();
	}
	
	// Initialize game
	private static void initGame() {
		println("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
				+ "Text Adventure v 0.1\nA text-based, interactive fiction game\n"
				+ "Copyright 2020 Aden Haussmann\n"
				+ "Programmed in Java, GUI in JavaFX\n"
				+ "If you are ever confused, type 'help'.\n\nType 'start' to begin...");
	}
	
	// Print to the text output area
	public static void println(String line) {
		String allText = outputText.getText();
		outputText.setText(allText + line + "\n");
	}
	
	// Take input
	private void onInput(String line) {
		println("\n" + line);
		Command.getInput(line.toLowerCase());
		
		moves.setText("Moves: " + Objects.getCount());
		room.setText("Room: " + Objects.getCurrentRoom().getRoom());
		roomItems.setText("Items in room: " + Objects.getCurrentRoom().getItems());
		inventory.setText("Inventory: " + Objects.getInventory());
		border2.setText("----------------------------");
		border.setText("-------------------------------------------------");
	}
	
	// Scroll animation
	public static void scrollAnimation(ScrollPane scroll)
	{
		Animation animation = new Timeline(
				new KeyFrame(Duration.seconds(.2),
				new KeyValue(scroll.vvalueProperty(), 1)));
				animation.play();
	}
	
	public static Scene getScene()
	{
		return scene2;
	}
	
}
