/********************************
 * Face Mover
 * FaceManager.java
 * Created by Justin Leonard
********************************/

package facemover;

import facemover.Face.Direction;
import facemover.Face.Position;
import java.awt.Color;
import java.lang.Thread;
import java.util.ArrayList;
import javax.swing.JFrame;

public class FaceManager {
	// Fields
	private ArrayList<Face> mainFaces = new ArrayList<Face>();
	private int frameRate = 10;

	/**
	 * Default constructor.
	 */
	public FaceManager() {
		frameRate = 10;
	}

	/**
	 * Class constructor specifying the frame rate of the display.
	 *
	 * @param  frmRate  frame rate of the display
	 */
	public FaceManager(int frmRate) {
		frameRate = frmRate;
	}

	/**
	 * Make a face and store it in a list.
	 */
	public void makeFace() {
		mainFaces.add(new Face());
	}

	/**
	 * Make a face and store it in a list.
	 * It will use a specified position.
	 *
	 * @param  pos  position of the face
	 */
	public void makeFace(Position pos) {
		mainFaces.add(new Face(pos));
	}

	/**
	 * Make a face and store it in a list.
	 * It will use a specified position and eye color.
	 *
	 * @param  pos  position of the face
	 * @param  eye  eye color of the face
	 */
	public void makeFace(Position pos, Color eye) {
		mainFaces.add(new Face(pos,eye));
	}
	
	/**
	 * Display all faces in this manager to the specified frame window.
	 * Returns true if there are faces in this manager.
	 * Returns false if there are not any faces in this manager.
	 *
	 * @param  frm  frame window to display the faces
	 * @return if the manager has any faces
	 */
	public boolean displayFaces(JFrame frm) {
		boolean isValid = false;
		
		// Manager has one or more faces
		if (getNumFaces() > 0) {
			// Display faces
			for (int i = 0; i < getNumFaces(); i++) {
				mainFaces.get(i).setSize(400, 400);
				frm.add(mainFaces.get(i));
				frm.setVisible(true);
			}
			isValid = true;
		} else {
			isValid = false;
		}
		
		return isValid;
	}
	
	/**
	 * Get the list of all faces in this manager.
	 *
	 * @return list of faces
	 */
	public ArrayList<Face> getFaces() {
		return mainFaces;
	}
	
	/**
	 * Get the number of faces in this manager.
	 *
	 * @return number of faces
	 */
	public int getNumFaces() {
		return mainFaces.size();
	}
	
	/**
	 * Reset all faces on the specified frame window.
	 *
	 * @param  frm  frame window to display the faces
	 */
	public void resetFaces(JFrame frm) {
		// Manager has one or more faces
		if (getNumFaces() > 0) {
			// Reset and display faces
			for (int i = 0; i < getNumFaces(); i++) {
				mainFaces.get(i).setPosition(mainFaces.get(i).getInitialPosition());
			}
			displayFaces(frm);
		}
	}

	/**
	 * Clear all faces from this manager.
	 */
	public void clear() {
		mainFaces.clear();
	}

	/**
	 * Moves all faces in this manager in the specified direction.
	 * It will move the faces based on the x and y speed.
	 * Returns true if the direction is valid.
	 * Returns false if the direction is not valid.
	 *
	 * @param  dir  the direction to move the face
	 * @param  speedX  the speed to move the x position of the face
	 * @param  speedY  the speed to move the y position of the face
	 * @param  frm  frame window to display the faces
	 * @return the validity of the input direction
	 */
	public boolean moveAll(Direction dir, int speedX, int speedY, JFrame frm) {
		boolean isValid = false, isRunning = true, stopRunning = false;

		// Manager has one or more faces
		if (getNumFaces() > 0) {
			// Loop to move all faces
			while (isRunning) {
				// Move faces
				for (int i = 0; i < getNumFaces(); i++) {
					// Move face
					mainFaces.get(i).move(dir,speedX,speedY);
				}
				
				// Check if faces have reached window bounds
				for (int i = 0; i < getNumFaces(); i++) {
					switch (dir) {
						case HORIZONTAL:
							switch (mainFaces.get(i).getPosition()) {
								// Position default, left, top, top left, bottom left
								case DEFAULT:
								case LEFT:
								case TOP:
								case TOPLEFT:
								case BOTTOMLEFT:
									if (mainFaces.get(i).getLocation().x > Face.getBound(Position.RIGHT)) {
										stopRunning = true;
									}
									break;
	
								// Position right, bottom, top right, bottom right
								case RIGHT:
								case BOTTOM:
								case TOPRIGHT:
								case BOTTOMRIGHT:
									if (mainFaces.get(i).getLocation().x < Face.getBound(Position.LEFT)) {
										stopRunning = true;
									}
									break;
							}
							break;
							
						case VERTICAL:
							switch (mainFaces.get(i).getPosition()) {
								// Position default, left, top, top left, top right
								case DEFAULT:
								case LEFT:
								case TOP:
								case TOPLEFT:
								case TOPRIGHT:
									if (mainFaces.get(i).getLocation().y > Face.getBound(Position.BOTTOM)) {
										stopRunning = true;
									}
									break;
	
								// Position right, bottom, bottom left, bottom right
								case RIGHT:
								case BOTTOM:
								case BOTTOMLEFT:
								case BOTTOMRIGHT:
									if (mainFaces.get(i).getLocation().y < Face.getBound(Position.TOP)) {
										stopRunning = true;
									}
									break;
							}
							break;
							
						case DIAGONAL:
							switch (mainFaces.get(i).getPosition()) {
								// Position default, left, top left
								case DEFAULT:
								case LEFT:
								case TOPLEFT:
									if (mainFaces.get(i).getLocation().x > Face.getBound(Position.RIGHT) ||
											mainFaces.get(i).getLocation().y > Face.getBound(Position.BOTTOM)) {
										stopRunning = true;
									}
									break;
	
								// Position right, bottom right
								case RIGHT:
								case BOTTOMRIGHT:
									if (mainFaces.get(i).getLocation().x < Face.getBound(Position.LEFT) ||
											mainFaces.get(i).getLocation().y < Face.getBound(Position.TOP)) {
										stopRunning = true;
									}
									break;
	
								// Position top, top right
								case TOP:
								case TOPRIGHT:
									if (mainFaces.get(i).getLocation().x < Face.getBound(Position.LEFT) ||
											mainFaces.get(i).getLocation().y > Face.getBound(Position.BOTTOM)) {
										stopRunning = true;
									}
									break;
	
								// Position bottom, bottom left
								case BOTTOM:	
								case BOTTOMLEFT:
									if (mainFaces.get(i).getLocation().x > Face.getBound(Position.RIGHT) ||
											mainFaces.get(i).getLocation().y < Face.getBound(Position.TOP)) {
										stopRunning = true;
									}
									break;
							}
							break;
							
						case DEFAULT:
							break;
					}
				}
				
				// Clean up and end loop
				if (stopRunning) {
					isRunning = false;
					
					// Set absolute face positions
					for (int i = 0; i < getNumFaces(); i++) {
						switch (dir) {
							case HORIZONTAL:
								switch (mainFaces.get(i).getPosition()) {
									// Position default
									case DEFAULT:
										mainFaces.get(i).setPosition(Position.RIGHT);
										break;
										
									// Position left
									case LEFT:
										mainFaces.get(i).setPosition(Position.RIGHT);
										break;
	
									// Position right
									case RIGHT:
										mainFaces.get(i).setPosition(Position.LEFT);
										break;
	
									// Position top
									case TOP:
										mainFaces.get(i).setPosition(Position.TOPRIGHT);
										break;
	
									// Position bottom
									case BOTTOM:
										mainFaces.get(i).setPosition(Position.BOTTOMLEFT);
										break;
	
									// Position top left
									case TOPLEFT:
										mainFaces.get(i).setPosition(Position.TOPRIGHT);
										break;
	
									// Position top right
									case TOPRIGHT:
										mainFaces.get(i).setPosition(Position.TOPLEFT);
										break;
	
									// Position bottom left
									case BOTTOMLEFT:
										mainFaces.get(i).setPosition(Position.BOTTOMRIGHT);
										break;
	
									// Position bottom right
									case BOTTOMRIGHT:
										mainFaces.get(i).setPosition(Position.BOTTOMLEFT);
										break;
								}
								break;
								
							case VERTICAL:
								switch (mainFaces.get(i).getPosition()) {
									// Position default
									case DEFAULT:
										mainFaces.get(i).setPosition(Position.BOTTOM);
										break;
										
									// Position left
									case LEFT:
										mainFaces.get(i).setPosition(Position.BOTTOMLEFT);
										break;
	
									// Position right
									case RIGHT:
										mainFaces.get(i).setPosition(Position.TOPRIGHT);
										break;
	
									// Position top
									case TOP:
										mainFaces.get(i).setPosition(Position.BOTTOM);
										break;
	
									// Position bottom
									case BOTTOM:
										mainFaces.get(i).setPosition(Position.TOP);
										break;
	
									// Position top left
									case TOPLEFT:
										mainFaces.get(i).setPosition(Position.BOTTOMLEFT);
										break;
	
									// Position top right
									case TOPRIGHT:
										mainFaces.get(i).setPosition(Position.BOTTOMRIGHT);
										break;
	
									// Position bottom left
									case BOTTOMLEFT:
										mainFaces.get(i).setPosition(Position.TOPLEFT);
										break;
	
									// Position bottom right
									case BOTTOMRIGHT:
										mainFaces.get(i).setPosition(Position.TOPRIGHT);
										break;
								}
								break;
								
							case DIAGONAL:
								switch (mainFaces.get(i).getPosition()) {
									// Position default
									case DEFAULT:
										mainFaces.get(i).setPosition(Position.BOTTOMRIGHT);
										break;
										
									// Position left
									case LEFT:
										mainFaces.get(i).setPosition(Position.BOTTOM);
										break;
	
									// Position right
									case RIGHT:
										mainFaces.get(i).setPosition(Position.TOP);
										break;
	
									// Position top
									case TOP:
										mainFaces.get(i).setPosition(Position.LEFT);
										break;
	
									// Position bottom
									case BOTTOM:
										mainFaces.get(i).setPosition(Position.RIGHT);
										break;
	
									// Position top left
									case TOPLEFT:
										mainFaces.get(i).setPosition(Position.BOTTOMRIGHT);
										break;
	
									// Position top right
									case TOPRIGHT:
										mainFaces.get(i).setPosition(Position.BOTTOMLEFT);
										break;
	
									// Position bottom left
									case BOTTOMLEFT:
										mainFaces.get(i).setPosition(Position.TOPRIGHT);
										break;
	
									// Position bottom right
									case BOTTOMRIGHT:
										mainFaces.get(i).setPosition(Position.TOPLEFT);
										break;
								}
								break;
								
							case DEFAULT:
								break;
						}
					}
				}

				// Display faces
				displayFaces(frm);
				
				// Pause
				try {
				  Thread.sleep(frameRate);
				} catch(InterruptedException ex) {}
			}
			isValid = true;
		} else {
			isValid = false;
		}

		return isValid;
	}
}
