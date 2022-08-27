/********************************
 * Product Manager
 * ItemGraphicsCard.java
 * Created by Justin Leonard
********************************/

package product;

import java.awt.GridLayout;
import javax.swing.Box;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

/**
 * Graphics card product type.
*/
public class ItemGraphicsCard extends ComputerProduct {
	// Fields
	private String memorySize, coreClock;
	private final String TYPE = "Graphics Card";
	
	/**
	 * Default constructor.
	 */
	public ItemGraphicsCard() {
		super("","","","");
		this.memorySize = "";
		this.coreClock = "";
	}
	
	/**
	* Class constructor specifying the name, description, brand, model number, memory size and core clock.
	*
	* @param  name the name of the product
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	* @param  memorySize the memory size of the product
	* @param  coreClock the core clock of the product
	*/
	public ItemGraphicsCard(String name, String description, String brand, String modelNumber, String memorySize, String coreClock) {
		super(name,description,brand,modelNumber);
		this.memorySize = memorySize;
		this.coreClock = coreClock;
	}
	
	/**
	* Get the memory size of the product.
	*
	* @return the memory size of the product
	*/
    public String getMemorySize() {
    	return this.memorySize;
    }
	
    /**
    * Set the memory size of the product.
    *
    * @param  memorySize the memory size of the product
    */
    public void setMemorySize(String memorySize) {
    	this.memorySize = memorySize;
    }
	
	/**
	* Get the core clock of the product.
	*
	* @return the core clock of the product
	*/
    public String getCoreClock() {
    	return this.coreClock;
    }
	
    /**
    * Set the core clock of the product.
    *
    * @param  coreClock the core clock of the product
    */
    public void setCoreClock(String coreClock) {
    	this.coreClock = coreClock;
    }
	
	/**
	* Get the information about the product.
	*
	* @return the information about the product
	*/
    public String getInfo() {
    	return "Type: " + this.getType() + "\r\n" +
    			"Name: " + this.getName() + "\r\n" +
    			"Description: " + this.getDescription() + "\r\n" +
    			"Brand: " + this.getBrand() + "\r\n" +
    			"Model Number: " + this.getModelNumber() + "\r\n" +
    			"Memory Size: " + this.getMemorySize() + "\r\n" +
    			"Core Clock: " + this.getCoreClock();
    }
	
	/**
	* Get the type of the product.
	*
	* @return the type of the product
	*/
    public String getType() {
    	return this.TYPE;
    }
	
	/**
	* Edit the information about the product.
	* The modified information with be the description, brand, model number, memory size and core clock.
	*
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	* @param  memorySize the memory size of the product
	* @param  coreClock the core clock of the product
	*/
    public void edit(String description, String brand, String modelNumber, String memorySize, String coreClock) {
    	this.setDescription(description);
    	this.setBrand(brand);
    	this.setModelNumber(modelNumber);
    	this.setMemorySize(memorySize);
    	this.setCoreClock(coreClock);
    }
	
    /**
    * Create a product based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
    * The user will be asked to enter the name, description, brand, model number, memory size and core clock.
    *
    * @return the created product
    */
    public static ItemGraphicsCard createProduct() {
		// Variables
		int result;
		boolean checkNameEmpty, checkDescriptionEmpty, checkBrandEmpty,
		checkModelNumberEmpty, checkMemorySizeEmpty, checkCoreClockEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelName, labelDescription, labelBrand, labelModelNumber, labelMemorySize, labelCoreClock;
		JTextField inputTextName, inputTextDescription, inputTextBrand, inputTextModelNumber, inputTextMemorySize, inputTextCoreClock;
		ItemGraphicsCard tempProduct = null;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelName = new JLabel("Name: ",JLabel.RIGHT);
		labelDescription = new JLabel("Description: ",JLabel.RIGHT);
		labelBrand = new JLabel("Brand: ",JLabel.RIGHT);
		labelModelNumber = new JLabel("Model Number: ",JLabel.RIGHT);
		labelMemorySize = new JLabel("Memory Size: ",JLabel.RIGHT);
		labelCoreClock = new JLabel("Core Clock: ",JLabel.RIGHT);

		// Text
		inputTextName = new JTextField(15);
		inputTextDescription = new JTextField(15);
		inputTextBrand = new JTextField(15);
		inputTextModelNumber = new JTextField(15);
		inputTextMemorySize = new JTextField(15);
		inputTextCoreClock = new JTextField(15);

		// Finalize UI
		panelMain.setLayout(new GridLayout(6,1));
		panelMain.add(labelName);
		panelMain.add(inputTextName);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelDescription);
		panelMain.add(inputTextDescription);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelBrand);
		panelMain.add(inputTextBrand);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelModelNumber);
		panelMain.add(inputTextModelNumber);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelMemorySize);
		panelMain.add(inputTextMemorySize);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelCoreClock);
		panelMain.add(inputTextCoreClock);
		
		// Get result
		while (isRunning) {
			// Open dialog
			result = JOptionPane.showConfirmDialog(null, panelMain, "Please enter product information", 
					JOptionPane.OK_CANCEL_OPTION);
			
			// Pressed OK
			if (result == JOptionPane.OK_OPTION) {
				// Check values
				checkNameEmpty = inputTextName.getText().isEmpty();
				checkDescriptionEmpty = inputTextDescription.getText().isEmpty();
				checkBrandEmpty = inputTextBrand.getText().isEmpty();
				checkModelNumberEmpty = inputTextModelNumber.getText().isEmpty();
				checkMemorySizeEmpty = inputTextMemorySize.getText().isEmpty();
				checkCoreClockEmpty = inputTextCoreClock.getText().isEmpty();
			
				// Error
				if (checkNameEmpty || checkDescriptionEmpty || checkBrandEmpty
						|| checkModelNumberEmpty || checkMemorySizeEmpty || checkCoreClockEmpty) {
					if (checkNameEmpty) {
						// Name not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the name", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkDescriptionEmpty) {
						// Description not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the description", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkBrandEmpty) {
						// Brand not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the brand", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkModelNumberEmpty) {
						// Model number not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the model number", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkMemorySizeEmpty) {
						// Memory size not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the memory size", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkCoreClockEmpty) {
						// Core clock not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the core clock", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					}
				} else {
					// Create product
					isRunning = false;
					tempProduct = new ItemGraphicsCard(inputTextName.getText(),inputTextDescription.getText(),inputTextBrand.getText(),
							inputTextModelNumber.getText(),inputTextMemorySize.getText(),inputTextCoreClock.getText());
				}
			} else {
				// Pressed cancel
				isRunning = false;
				tempProduct = new ItemGraphicsCard();
			}
		}
		return tempProduct;
    }
	
    /**
    * Modify a product based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
    * The user will be asked to enter the description, brand, model number, memory size and core clock.
    *
	* @param  tempProduct the product to modify
    */
    public static void modifyProduct(ItemGraphicsCard tempProduct) {
		// Variables
		int result;
		boolean checkDescriptionEmpty, checkBrandEmpty, checkModelNumberEmpty,
		checkMemorySizeEmpty, checkCoreClockEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelDescription, labelBrand, labelModelNumber, labelMemorySize, labelCoreClock;
		JTextField inputTextDescription, inputTextBrand, inputTextModelNumber, inputTextMemorySize, inputTextCoreClock;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelDescription = new JLabel("Description: ",JLabel.RIGHT);
		labelBrand = new JLabel("Brand: ",JLabel.RIGHT);
		labelModelNumber = new JLabel("Model Number: ",JLabel.RIGHT);
		labelMemorySize = new JLabel("Memory Size: ",JLabel.RIGHT);
		labelCoreClock = new JLabel("Core Clock: ",JLabel.RIGHT);

		// Text
		inputTextDescription = new JTextField(tempProduct.getDescription(),15);
		inputTextBrand = new JTextField(tempProduct.getBrand(),15);
		inputTextModelNumber = new JTextField(tempProduct.getModelNumber(),15);
		inputTextMemorySize = new JTextField(tempProduct.getMemorySize(),15);
		inputTextCoreClock = new JTextField(tempProduct.getCoreClock(),15);

		// Finalize UI
		panelMain.setLayout(new GridLayout(5,1));
		panelMain.add(labelDescription);
		panelMain.add(inputTextDescription);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelBrand);
		panelMain.add(inputTextBrand);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelModelNumber);
		panelMain.add(inputTextModelNumber);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelMemorySize);
		panelMain.add(inputTextMemorySize);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelCoreClock);
		panelMain.add(inputTextCoreClock);
		
		// Get result
		while (isRunning) {
			// Open dialog
			result = JOptionPane.showConfirmDialog(null, panelMain, "Please enter product information", 
					JOptionPane.OK_CANCEL_OPTION);
			
			// Pressed OK
			if (result == JOptionPane.OK_OPTION) {
				// Check values
				checkDescriptionEmpty = inputTextDescription.getText().isEmpty();
				checkBrandEmpty = inputTextBrand.getText().isEmpty();
				checkModelNumberEmpty = inputTextModelNumber.getText().isEmpty();
				checkMemorySizeEmpty = inputTextMemorySize.getText().isEmpty();
				checkCoreClockEmpty = inputTextCoreClock.getText().isEmpty();
			
				// Error
				if (checkDescriptionEmpty || checkBrandEmpty || checkModelNumberEmpty
						|| checkMemorySizeEmpty || checkCoreClockEmpty) {
					if (checkDescriptionEmpty) {
						// Description not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the description", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkBrandEmpty) {
						// Brand not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the brand", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkModelNumberEmpty) {
						// Model number not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the model number", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkMemorySizeEmpty) {
						// Memory size not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the memory size", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkCoreClockEmpty) {
						// Core clock not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the core clock", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					}
				} else {
					// Modify product
					isRunning = false;
					tempProduct.edit(inputTextDescription.getText(),inputTextBrand.getText(),
							inputTextModelNumber.getText(),inputTextMemorySize.getText(),inputTextCoreClock.getText());
				}
			} else {
				// Pressed cancel
				isRunning = false;
			}
		}
    }
}
