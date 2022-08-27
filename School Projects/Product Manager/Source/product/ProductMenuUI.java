/********************************
 * Product Manager
 * ProductMenuUI.java
 * Created by Justin Leonard
********************************/

package product;

import java.awt.BasicStroke;
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.geom.Line2D;
import javax.swing.JComponent;

/**
 * Basic user interface components.
*/
public class ProductMenuUI extends JComponent {
	/**
	* Default constructor.
	*/
	public ProductMenuUI() {
		// Default Constructor
	}
	
	/**
	 * This will draw all graphical user interface components to the screen.
	 *
	 * @param  graphicsTemp graphics to draw component
	 */
	public void paintComponent(Graphics graphicsTemp) {
		// Set graphics
		Graphics2D graphicsMain = (Graphics2D) graphicsTemp;
		
		// Draw the divider
		Line2D.Double linedivider = new Line2D.Double(0,0,880,0);
		graphicsMain.setColor(Color.BLACK);
		graphicsMain.setStroke(new BasicStroke(10));
		graphicsMain.draw(linedivider);
	}
}
