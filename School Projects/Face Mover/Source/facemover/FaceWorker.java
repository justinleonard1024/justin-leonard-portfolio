/********************************
 * Face Mover
 * FaceWorker.java
 * Created by Justin Leonard
********************************/

package facemover;

import facemover.Face.Direction;
import java.util.ArrayList;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.SwingWorker;

public class FaceWorker extends SwingWorker<Integer, Integer> {
	// Fields
	private Direction direction;
	private FaceManager faceMain;
	private JFrame frame;
	private ArrayList<JButton> buttons;
	
	/**
	 * Class constructor specifying the direction of the faces,
	 * the face manager that contains the faces and the frame window
	 * to display the faces to.
	 *
	 * @param  dir  the direction to move the faces
	 * @param  am  the face manager containing all the faces
	 * @param  frm  frame window to display the faces
	 */
	public FaceWorker(Direction dir, FaceManager am, JFrame frm) {
		// Get entities
		direction = dir;
		faceMain = am;
		frame = frm;
	}
	
	/**
	 * Class constructor specifying the direction of the faces,
	 * the face manager that contains the faces, the frame window
	 * to display the faces to and all buttons used.
	 *
	 * @param  dir  the direction to move the faces
	 * @param  am  the face manager containing all the faces
	 * @param  frm  frame window to display the faces
	 * @param  btn  the list of all buttons in the frame window
	 */
	public FaceWorker(Direction dir, FaceManager am, JFrame frm, ArrayList<JButton> btn) {
		// Get entities
		direction = dir;
		faceMain = am;
		frame = frm;
		buttons = btn;
		
		// Button list is not empty
		if (buttons.size() > 0) {
			// Disable all buttons
			for (int i = 0; i < buttons.size(); i++) {
				buttons.get(i).setEnabled(false);
			}
		}
	}
	
	/**
	 * All code to run in the background of this separate thread.
	 * This will move all faces in the specified direction.
	 *
	 * @return validation
	 */
	protected Integer doInBackground() throws Exception {
		switch (direction) {
			// Move Horizontal
			case HORIZONTAL:
				faceMain.moveAll(Direction.HORIZONTAL, 2, 2, frame);
				break;
	
			// Move Vertical
			case VERTICAL:
				faceMain.moveAll(Direction.VERTICAL, 2, 2, frame);
				break;
	
			// Move Diagonal
			case DIAGONAL:
				faceMain.moveAll(Direction.DIAGONAL, 4, 3, frame);
				break;
	
			// Invalid Input
			default:
	            break;
		}
		return null;
	}

	/**
	 * All code to run after all background processes have finished.
	 * This will enable all disabled buttons in the specified frame window.
	 */
    protected void done()
    {
		// Button list is not empty
    	if (buttons.size() > 0) {
    		// Enable all buttons
    		for (int i = 0; i < buttons.size(); i++) {
    			buttons.get(i).setEnabled(true);
    		}
    	}
    }
}
