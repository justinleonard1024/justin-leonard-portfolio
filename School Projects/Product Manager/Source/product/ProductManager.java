/********************************
 * Product Manager
 * ProductManager.java
 * Created by Justin Leonard
********************************/

package product;

import adt.ListADT;
import adt.MyArrayList;
import adt.MyLinkedListList;
import java.awt.Cursor;
import java.awt.Font;
import java.awt.GridLayout;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextArea;

/**
 * Manages a collection of products.
*/
public class ProductManager {
	// Fields
	private ListADT mainProducts;
	
	/**
	* Default constructor.
	*/
	public ProductManager(Type type) {
		switch (type) {
			case ARRAY_LIST:
				this.mainProducts = new MyArrayList();
				break;
			case LINKED_LIST:
				this.mainProducts = new MyLinkedListList();
				break;
			default:
				this.mainProducts = new MyArrayList();
		}
	}
	
	/**
	 * Types that can be used.
	 */
	public enum Type {
		ARRAY_LIST,
		LINKED_LIST
	}
	
	/**
	* Get the list of products.
	*
	* @return the list of products
	*/
	public ListADT getProducts() {
		return this.mainProducts;
	}
	
	/**
	* Get the number of products in the list of products.
	*
	* @return the number of products
	*/
	public int getNumProducts() {
		return this.getProducts().size();
	}
	
	/**
	* Get a product from the list of products that has the input name.
	* It will go through the list until it finds a product that matches the input name.
	*
	* @param  name the name of the product
	* @return the product with the input name
	*/
	public <T extends ComputerProduct> T getProductFromName(String name) {
		// Variables
		boolean productFound = false;
		T tempProduct = null;
		
		// Find matching product
		for (int i = 0; i < this.getNumProducts() && !productFound; i++) {
			// Get product
			if (name.equals(this.getProducts().get(i).getName())) {
				productFound = true;
				tempProduct = (T)this.getProducts().get(i);
			}
		}
		
		return tempProduct;
	}
	
	/**
	* Get the type of a product from the list of products that has the input name.
	* It will go through the list until it finds a product that matches the input name.
	*
	* @param  name the name of the product
	* @return the type of the product
	*/
	public String getTypeFromName(String name) {
		// Variables
		boolean productFound = false;
		String type = "";
		
		// Find matching product
		for (int i = 0; i < this.getNumProducts() && !productFound; i++) {
			// Get type
			if (name.equals(this.getProducts().get(i).getName())) {
				productFound = true;
				type = this.getProducts().get(i).getType();
			}
		}
		
		return type;
	}
	
	/**
	* Add a product to the list of products.
	*
	* @param  tempProduct the product to add
	*/
	public <T extends ComputerProduct> void add(T tempProduct) {
		this.getProducts().add(tempProduct);
	}
	
	/**
	* Remove a product from the list of products.
	*
	* @param  name the name of the product
	*/
	public void remove(String name) {
		// Find matching product
		for (int i = 0; i < this.getNumProducts(); i++) {
			// Remove product
			if (name.equals(this.getProducts().get(i).getName())) {
				this.getProducts().remove(i);
			}
		}
	}
	
	/**
	* Clear the list of products.
	*/
	public void clear() {
		this.getProducts().clear();
	}
	
	/**
	* Check if a product with a specified name exists in the list of products.
	*
	* @param  name the name of the product
	* @return if the product exists in the list of products
	*/
	public boolean checkExists(String name) {
		// Variables
		boolean productFound = false;

		// Find matching product
		for (int i = 0; i < this.getNumProducts() && !productFound; i++) {
			// Product exists
			if (name.equals(this.getProducts().get(i).getName())) {
				productFound = true;
			}
		}

		return productFound;
	}
	
	/**
	* Show information about the product that has the input name.
	* A message dialog will appear showing the user all of the information about the product.
	*
	* @param  name the name of the product
	*/
	public void showInfo(String name) {
		// Variables
		boolean productFound = false;
		JPanel panelMain;
		JTextArea textInfo;

		// Panel
		panelMain = new JPanel();
		
		// Text
		textInfo = new JTextArea();
		
		// Show info
		for (int i = 0; i < this.getNumProducts() && !productFound; i++) {
			// Product exists
			if (name.equals(this.getProducts().get(i).getName())) {
				productFound = true;
				
				// Text
				textInfo.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
				textInfo.setEditable(false);
				textInfo.setFont(new Font("Dialog", Font.PLAIN, 16));
				textInfo.setText("Product Information\r\n\r\n" + this.getProducts().get(i).getInfo());
				
				// Finalize UI
				panelMain.setLayout(new GridLayout(1,1));
				panelMain.add(textInfo);
				
				JOptionPane.showConfirmDialog(null, panelMain, "Product Information", JOptionPane.DEFAULT_OPTION);
			}
		}
	}
}
