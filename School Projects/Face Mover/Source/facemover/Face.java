/********************************
 * Face Mover
 * Face.java
 * Created by Justin Leonard
********************************/

package facemover;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Point;
import java.awt.Rectangle;
import java.awt.geom.Ellipse2D;
import java.awt.geom.Line2D;
import javax.swing.JComponent;

public class Face extends JComponent {
	// Fields
	private Position position = Position.DEFAULT, initialPosition = Position.DEFAULT;
	private Color eyeColor = Color.GREEN;
	private Point positionDefault = new Point(137,95), positionLeft = new Point(-5,95), positionRight = new Point(278,95),
	positionTop = new Point(137,-10), positionBottom = new Point(137,200), positionTopLeft = new Point(-5,-10),
	positionTopRight = new Point(278,-10), positionBottomLeft = new Point(-5,200), positionBottomRight = new Point(278,200);
	private static int boundLeft = -5, boundRight = 278, boundTop = -10, boundBottom = 200;

	/**
	 * Default constructor.
	 */
	public Face() {
		position = Position.DEFAULT;
		initialPosition = Position.DEFAULT;
		eyeColor = Color.GREEN;
		setPosition(position);
	}

	/**
	 * Class constructor specifying the position of the face.
	 *
	 * @param  pos  position of the face
	 */
	public Face(Position pos) {
		position = pos;
		initialPosition = pos;
		eyeColor = Color.GREEN;
		setPosition(position);
	}

	/**
	 * Class constructor specifying the position of the face and the eye color.
	 *
	 * @param  pos  position of the face
	 * @param  eye  eye color of the face
	 */
	public Face(Position pos, Color eye) {
		position = pos;
		initialPosition = pos;
		eyeColor = eye;
		setPosition(position);
	}

	/**
	 * Directions that can be used.
	 */
	public enum Direction {
		DEFAULT,
		HORIZONTAL,
		VERTICAL,
		DIAGONAL
	}

	/**
	 * Positions that can be used.
	 */
	public enum Position {
		DEFAULT,
		LEFT,
		RIGHT,
		TOP,
		BOTTOM,
		TOPLEFT,
		TOPRIGHT,
		BOTTOMLEFT,
		BOTTOMRIGHT
	}
	
	/**
	 * Set the position of the face.
	 * Returns true if the position is valid.
	 * Returns false if the position is not valid.
	 *
	 * @param  pos  position of the face
	 * @return the validity of the input position
	 */
	public boolean setPosition(Position pos) {
		boolean isValid = false;
		position = pos;

		switch (position) {
			// Position default
			case DEFAULT:
				setLocation(positionDefault);
				isValid = true;
				break;
				
			// Position left
			case LEFT:
				setLocation(positionLeft);
				isValid = true;
				break;

			// Position right
			case RIGHT:
				setLocation(positionRight);
				isValid = true;
				break;

			// Position top
			case TOP:
				setLocation(positionTop);
				isValid = true;
				break;

			// Position bottom
			case BOTTOM:
				setLocation(positionBottom);
				isValid = true;
				break;

			// Position top left
			case TOPLEFT:
				setLocation(positionTopLeft);
				isValid = true;
				break;

			// Position top right
			case TOPRIGHT:
				setLocation(positionTopRight);
				isValid = true;
				break;

			// Position bottom left
			case BOTTOMLEFT:
				setLocation(positionBottomLeft);
				isValid = true;
				break;

			// Position bottom right
			case BOTTOMRIGHT:
				setLocation(positionBottomRight);
				isValid = true;
				break;

			// Invalid position
			default:
				isValid = false;
				break;
		}

		return isValid;
	}
	
	/**
	 * Gets the current position of the face.
	 *
	 * @return the current position of the face
	 */
	public Position getPosition() {
		return position;
	}
	
	/**
	 * Gets the initial position of the face when 
	 * it was first created.
	 *
	 * @return the initial position of the face
	 */
	public Position getInitialPosition() {
		return initialPosition;
	}
	
	/**
	 * Returns the screen bounds of the selected position.
	 * The bound can only be left, right, top or bottom.
	 * It will return 0 if the position is invalid.
	 *
	 * @param  pos  position of the face
	 * @return the bounds of the position
	 */
	public static int getBound(Position pos) {
		int boundTemp = 0;
		
		switch (pos) {
			// Position left
			case LEFT:
				boundTemp = boundLeft;
				break;

			// Position right
			case RIGHT:
				boundTemp = boundRight;
				break;

			// Position top
			case TOP:
				boundTemp = boundTop;
				break;

			// Position bottom
			case BOTTOM:
				boundTemp = boundBottom;
				break;

			// Invalid position
			default:
				boundTemp = 0;
				break;
		}
		
		return boundTemp;
	}

	/**
	 * Moves the face in the specified direction.
	 * It will move the face based on the x and y speed.
	 * Returns true if the direction is valid.
	 * Returns false if the direction is not valid.
	 *
	 * @param  dir  the direction to move the face
	 * @param  speedX  the speed to move the x position of the face
	 * @param  speedY  the speed to move the y position of the face
	 * @return the validity of the input direction
	 */
	public boolean move(Direction dir, int speedX, int speedY) {
		boolean isValid = false;
		
		switch (dir) {
			// Move Horizontal
			case HORIZONTAL:
				moveHorizontal(speedX);
				isValid = true;
				break;

			// Move Vertical
			case VERTICAL:
				moveVertical(speedY);
				isValid = true;
				break;

			// Move Diagonal
			case DIAGONAL:
				moveDiagonal(speedX,speedY);
				isValid = true;
				break;

			// Invalid Input
			default:
				isValid = false;
                break;
		}

		return isValid;
	}

	/**
	 * Moves the face in the horizontal direction.
	 * The face will be moved left or right with the
	 * amount of speedX depending upon the face's position.
	 *
	 * @param  speedX  the speed to move the x position of the face
	 */
	private void moveHorizontal(int speedX) {
		switch (position) {
			// Position default, left, top, top left, bottom left
			case DEFAULT:
			case LEFT:
			case TOP:
			case TOPLEFT:
			case BOTTOMLEFT:
				setLocation(getLocation().x + speedX, getLocation().y);
				break;

			// Position right, bottom, top right, bottom right
			case RIGHT:
			case BOTTOM:
			case TOPRIGHT:
			case BOTTOMRIGHT:
				setLocation(getLocation().x - speedX, getLocation().y);
				break;

			// Invalid position
			default:
				break;
		}
	}

	/**
	 * Moves the face in the vertical direction.
	 * The face will be moved up or down with the
	 * amount of speedY depending upon the face's position.
	 *
	 * @param  speedY  the speed to move the y position of the face
	 */
	private void moveVertical(int speedY) {
		switch (position) {
			// Position default, left, top, top left, top right
			case DEFAULT:
			case LEFT:
			case TOP:
			case TOPLEFT:
			case TOPRIGHT:
				setLocation(getLocation().x, getLocation().y + speedY);
				break;

			// Position right, bottom, bottom left, bottom right
			case RIGHT:
			case BOTTOM:
			case BOTTOMLEFT:
			case BOTTOMRIGHT:
				setLocation(getLocation().x, getLocation().y - speedY);
				break;

			// Invalid position
			default:
				break;
		}
	}

	/**
	 * Moves the face in the diagonal direction.
	 * The face will be moved diagonally in multiple directions 
	 * with the amount of speedX and speedY depending upon the face's position.
	 *
	 * @param  speedX  the speed to move the x position of the face
	 * @param  speedY  the speed to move the y position of the face
	 */
	private void moveDiagonal(int speedX, int speedY) {
		switch (position) {
			// Position default, left, top left
			case DEFAULT:
			case LEFT:
			case TOPLEFT:
				setLocation(getLocation().x + speedX, getLocation().y + speedY);
				break;

			// Position right, bottom right
			case RIGHT:
			case BOTTOMRIGHT:
				setLocation(getLocation().x - speedX, getLocation().y - speedY);
				break;

			// Position top, top right
			case TOP:
			case TOPRIGHT:
				setLocation(getLocation().x - speedX, getLocation().y + speedY);
				break;

			// Position bottom, bottom left
			case BOTTOM:	
			case BOTTOMLEFT:
				setLocation(getLocation().x + speedX, getLocation().y - speedY);
				break;
	
			// Invalid position
			default:
				break;
		}
	}
	
	/**
	 * This method is from the JComponent class.
	 * This will draw the face.
	 *
	 * @param  g  graphics to draw component
	 */
	public void paintComponent(Graphics g) {
		// Recover Graphics2D
		Graphics2D g2 = (Graphics2D) g;
		
		// Draw the head
		Ellipse2D.Double head = new Ellipse2D.Double(5,10,100,150);
		g2.draw(head);
		
		// Draw the Eyes
		g2.setColor(eyeColor);
		Rectangle eye = new Rectangle(25,70,15,15);
		g2.fill(eye);
		eye.translate(50,0);
		g2.fill(eye);
		
		// Draw the mouth
		Line2D.Double mouth = new Line2D.Double(30,110,80,110);
		g2.setColor(Color.RED);
		g2.draw(mouth);
	}
}
