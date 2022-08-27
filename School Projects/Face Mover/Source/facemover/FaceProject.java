/********************************
 * Face Mover
 * FaceProject.java
 * Created by Justin Leonard
********************************/

package facemover;

import facemover.Face.Direction;
import facemover.Face.Position;
import java.awt.Color;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.ArrayList;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class FaceProject {
	/**
	 * The main method to start the program.
	 * This method will create the user interface and faces.
	 * The program will wait for the user input from the button click events.
	 */
	public static void startFace() {
		// Face manager
		FaceManager faceMain = new FaceManager();
		faceMain.makeFace(Position.LEFT);
		faceMain.makeFace(Position.RIGHT,Color.BLUE);
		
		// Frame window
		JFrame frame = new JFrame();
		frame.setSize(390,600);
		frame.setLayout(null);
		frame.setTitle("Alien Face Mover");
		frame.setResizable(false);
		frame.setLocationRelativeTo(null);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		// Program UI
		FaceProjectUI faceUI = new FaceProjectUI();
		JLabel labelTitle = new JLabel("Options",JLabel.CENTER);
		
		// Program UI size
		faceUI.setSize(400, 400);
		faceUI.setLocation(0, 360);
		labelTitle.setSize(50, 50);
		labelTitle.setLocation(165, 370);
		
		// Button
		JButton buttonHorizontal = new JButton("Move Horizontal");
		JButton buttonVertical = new JButton("Move Vertical");
		JButton buttonDiagonal = new JButton("Move Diagonal");
		JButton buttonReset = new JButton("Reset Position");
		JButton buttonExit = new JButton("Exit");
		
		// Button size
		buttonHorizontal.setSize(150, 25);
		buttonHorizontal.setLocation(20,420);
		buttonVertical.setSize(150, 25);
		buttonVertical.setLocation(210,420);
		buttonDiagonal.setSize(150, 25);
		buttonDiagonal.setLocation(20,470);
		buttonReset.setSize(150, 25);
		buttonReset.setLocation(210,470);
		buttonExit.setSize(150, 25);
		buttonExit.setLocation(115,520);

		// Finalize UI
		frame.add(faceUI);
		frame.add(labelTitle);
		frame.add(buttonHorizontal);
		frame.add(buttonVertical);
		frame.add(buttonDiagonal);
		frame.add(buttonReset);
		frame.add(buttonExit);
		faceMain.displayFaces(frame);
        frame.setVisible(true);

		// Events
		
		// Horizontal button click
		buttonHorizontal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				ArrayList<JButton> mainButtons = new ArrayList<JButton>();
				mainButtons.add(buttonHorizontal);
				mainButtons.add(buttonVertical);
				mainButtons.add(buttonDiagonal);
				mainButtons.add(buttonReset);
				mainButtons.add(buttonExit);
				
				// Move all faces horizontally
				new FaceWorker(Direction.HORIZONTAL,faceMain,frame,mainButtons).execute();
			}          
		});

		// Vertical button click
		buttonVertical.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				ArrayList<JButton> mainButtons = new ArrayList<JButton>();
				mainButtons.add(buttonHorizontal);
				mainButtons.add(buttonVertical);
				mainButtons.add(buttonDiagonal);
				mainButtons.add(buttonReset);
				mainButtons.add(buttonExit);
				
				// Move all faces vertically
				new FaceWorker(Direction.VERTICAL,faceMain,frame,mainButtons).execute();
			}
		});

		// Diagonal button click
		buttonDiagonal.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				ArrayList<JButton> mainButtons = new ArrayList<JButton>();
				mainButtons.add(buttonHorizontal);
				mainButtons.add(buttonVertical);
				mainButtons.add(buttonDiagonal);
				mainButtons.add(buttonReset);
				mainButtons.add(buttonExit);
				
				// Move all faces diagonally
				new FaceWorker(Direction.DIAGONAL,faceMain,frame,mainButtons).execute();
			}
		});

		// Reset button click
		buttonReset.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				faceMain.resetFaces(frame);
			}
		});

		// Exit button click
		buttonExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				System.exit(0);
			}
		});
	}
	
	/**
	 * The main entry point for the program.
	 *
	 * @param  args  the command line arguments
	 */
	public static void main(String[] args) {
		startFace();
	}
}
