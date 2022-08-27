/********************************
 * Face Mover
 * FaceProjectUI.java
 * Created by Justin Leonard
********************************/

package facemover;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Line2D;
import javax.swing.JComponent;

public class FaceProjectUI extends JComponent {
	/**
	 * Default constructor.
	 */
	public FaceProjectUI() {
		// Default Constructor
	}
	
	/**
	 * This method is from the JComponent class.
	 * This will draw all graphical user interface components to the screen.
	 *
	 * @param  g  graphics to draw component
	 */
	public void paintComponent(Graphics g) {
		// Recover Graphics2D
		Graphics2D g2 = (Graphics2D) g;
		
		// Draw the divider
		Line2D.Double divider = new Line2D.Double(0,0,400,0);
		g2.setColor(Color.BLACK);
		g2.setStroke(new BasicStroke(10));
		g2.draw(divider);
	}
}
