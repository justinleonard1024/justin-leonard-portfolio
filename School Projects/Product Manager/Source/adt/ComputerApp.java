/********************************
 * Product Manager
 * ComputerApp.java
 * Created by Justin Leonard
********************************/

package adt;

import product.ProductManager;
import product.ProductMenu;

/**
 * Justin Leonard
 * 
 * This is the starting point for the application.
 * There is a user interface with a product list and options.
 * The product list contains all information about the current products.
 * 
 * I am using the main program to test the program because all tools necessary for testing are there.
 * This main method will use the ProductMenu with the specified type.
 * Edit the argument of the ProductMenu to whatever list adt type you want the program to use.
 * 
 * The main Project1 inventory part has been edited to use any ListADT.
 * All abstract data type files will be stored in the package "adt".
 * All original Project1 inventory files will be stored in the package "product".
 * 
 * I slightly edited the names of the ListADT methods to match the names of the methods of the java "ArrayList".
 * I implemented the original program with an ArrayList so it was easier and more efficient just to change the names.
 * The code is still mostly the same. I just fixed and edited a few problems with the original code.
*/
public class ComputerApp {
	/**
	 * The main entry point for the program.
	 *
	 * @param  args the command line arguments
	 */
    public static void main (String[] args){
		// Start
		ProductMenu app = new ProductMenu(ProductManager.Type.ARRAY_LIST); // Change this to change which adt is used
		app.start();
    }
}