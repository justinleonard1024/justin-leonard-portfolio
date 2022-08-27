/********************************
 * Product Manager
 * ComputerProductApp.java
 * Created by Justin Leonard
********************************/

package product;

/**
 * Justin Leonard
 * 
 * This is the starting point for the application.
 * There is a user interface with a product list and options.
 * The product list contains all information about the current products.
 * 
 * There is one base class ComputerProduct with three derived classes.
 * The base class has the qualities of the name, description, brand and model number.
 * The three types of products are graphics card, hard drive and processor.
 * The user will be asked which type of product to create before it is added.
 * 
 * Each derived class will have two extra qualities unique to their type.
 * The graphics card has memory size and core clock.
 * The hard drive has capacity and rpm.
 * The processor has cores and frequency.
 * 
 * The user can interact with the user interface by pressing the buttons.
 * The button options are:
 * Add - Add a product to the product list
 * Remove - Remove a product from the product list
 * Edit - Edit a product in the product list
 * Info - Get information about a product.
 * Save To File - Save the product list to a file
 * Clear - Clear all products in the product list
 * Exit - Exit the program
*/
public class ComputerProductApp {
	/**
	 * The main entry point for the program.
	 *
	 * @param  args the command line arguments
	 */
	/*
	public static void main(String[] args) {
		// Start
		ProductMenu app = new ProductMenu(ProductManager.Type.ARRAY_LIST); // Change this to change which adt is used
		app.start();
	}
	*/
}
