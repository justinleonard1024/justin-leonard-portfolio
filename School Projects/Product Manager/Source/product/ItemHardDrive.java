/********************************
 * Product Manager
 * ItemHardDrive.java
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
 * Hard drive product type.
*/
public class ItemHardDrive extends ComputerProduct {
	// Fields
	private String capacity, rpm;
	private final String TYPE = "Hard Drive";
	
	/**
	 * Default constructor.
	 */
	public ItemHardDrive() {
		super("","","","");
		this.capacity = "";
		this.rpm = "";
	}
	
	/**
	* Class constructor specifying the name, description, brand, model number, capacity and rpm.
	*
	* @param  name the name of the product
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	* @param  capacity the capacity of the product
	* @param  rpm the rpm of the product
	*/
	public ItemHardDrive(String name, String description, String brand, String modelNumber, String capacity, String rpm) {
		super(name,description,brand,modelNumber);
		this.capacity = capacity;
		this.rpm = rpm;
	}
	
	/**
	* Get the capacity of the product.
	*
	* @return the capacity of the product
	*/
    public String getCapacity() {
    	return this.capacity;
    }
	
    /**
    * Set the capacity of the product.
    *
    * @param  capacity the capacity of the product
    */
    public void setCapacity(String capacity) {
    	this.capacity = capacity;
    }
	
	/**
	* Get the rpm of the product.
	*
	* @return the rpm of the product
	*/
    public String getRPM() {
    	return this.rpm;
    }
	
    /**
    * Set the rpm of the product.
    *
    * @param  rpm the rpm of the product
    */
    public void setRPM(String rpm) {
    	this.rpm = rpm;
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
    			"Capacity: " + this.getCapacity() + "\r\n" +
    			"RPM: " + this.getRPM();
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
	* The modified information with be the description, brand, model number, capacity and rpm.
	*
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	* @param  capacity the capacity of the product
	* @param  rpm the rpm of the product
	*/
    public void edit(String description, String brand, String modelNumber, String capacity, String rpm) {
    	this.setDescription(description);
    	this.setBrand(brand);
    	this.setModelNumber(modelNumber);
    	this.setCapacity(capacity);
    	this.setRPM(rpm);
    }
	
    /**
    * Create a product based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
    * The user will be asked to enter the name, description, brand, model number, capacity and rpm.
    *
    * @return the created product
    */
    public static ItemHardDrive createProduct() {
		// Variables
		int result;
		boolean checkNameEmpty, checkDescriptionEmpty, checkBrandEmpty,
		checkModelNumberEmpty, checkCapacityEmpty, checkRPMEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelName, labelDescription, labelBrand, labelModelNumber, labelCapacity, labelRPM;
		JTextField inputTextName, inputTextDescription, inputTextBrand, inputTextModelNumber, inputTextCapacity, inputTextRPM;
		ItemHardDrive tempProduct = null;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelName = new JLabel("Name: ",JLabel.RIGHT);
		labelDescription = new JLabel("Description: ",JLabel.RIGHT);
		labelBrand = new JLabel("Brand: ",JLabel.RIGHT);
		labelModelNumber = new JLabel("Model Number: ",JLabel.RIGHT);
		labelCapacity = new JLabel("Capacity: ",JLabel.RIGHT);
		labelRPM = new JLabel("RPM: ",JLabel.RIGHT);

		// Text
		inputTextName = new JTextField(15);
		inputTextDescription = new JTextField(15);
		inputTextBrand = new JTextField(15);
		inputTextModelNumber = new JTextField(15);
		inputTextCapacity = new JTextField(15);
		inputTextRPM = new JTextField(15);

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
		panelMain.add(labelCapacity);
		panelMain.add(inputTextCapacity);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelRPM);
		panelMain.add(inputTextRPM);
		
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
				checkCapacityEmpty = inputTextCapacity.getText().isEmpty();
				checkRPMEmpty = inputTextRPM.getText().isEmpty();
			
				// Error
				if (checkNameEmpty || checkDescriptionEmpty || checkBrandEmpty
						|| checkModelNumberEmpty || checkCapacityEmpty || checkRPMEmpty) {
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
					} else if (checkCapacityEmpty) {
						// Capacity not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the capacity", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkRPMEmpty) {
						// RPM not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the rpm", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					}
				} else {
					// Create product
					isRunning = false;
					tempProduct = new ItemHardDrive(inputTextName.getText(),inputTextDescription.getText(),inputTextBrand.getText(),
							inputTextModelNumber.getText(),inputTextCapacity.getText(),inputTextRPM.getText());
				}
			} else {
				// Pressed cancel
				isRunning = false;
				tempProduct = new ItemHardDrive();
			}
		}
		return tempProduct;
    }
	
    /**
    * Modify a product based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
    * The user will be asked to enter the description, brand, model number, capacity and rpm.
    *
	* @param  tempProduct the product to modify
    */
    public static void modifyProduct(ItemHardDrive tempProduct) {
		// Variables
		int result;
		boolean checkDescriptionEmpty, checkBrandEmpty, checkModelNumberEmpty,
		checkCapacityEmpty, checkRPMEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelDescription, labelBrand, labelModelNumber, labelCapacity, labelRPM;
		JTextField inputTextDescription, inputTextBrand, inputTextModelNumber, inputTextCapacity, inputTextRPM;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelDescription = new JLabel("Description: ",JLabel.RIGHT);
		labelBrand = new JLabel("Brand: ",JLabel.RIGHT);
		labelModelNumber = new JLabel("Model Number: ",JLabel.RIGHT);
		labelCapacity = new JLabel("Capacity: ",JLabel.RIGHT);
		labelRPM = new JLabel("RPM: ",JLabel.RIGHT);

		// Text
		inputTextDescription = new JTextField(tempProduct.getDescription(),15);
		inputTextBrand = new JTextField(tempProduct.getBrand(),15);
		inputTextModelNumber = new JTextField(tempProduct.getModelNumber(),15);
		inputTextCapacity = new JTextField(tempProduct.getCapacity(),15);
		inputTextRPM = new JTextField(tempProduct.getRPM(),15);

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
		panelMain.add(labelCapacity);
		panelMain.add(inputTextCapacity);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelRPM);
		panelMain.add(inputTextRPM);
		
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
				checkCapacityEmpty = inputTextCapacity.getText().isEmpty();
				checkRPMEmpty = inputTextRPM.getText().isEmpty();
			
				// Error
				if (checkDescriptionEmpty || checkBrandEmpty || checkModelNumberEmpty
						|| checkCapacityEmpty || checkRPMEmpty) {
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
					} else if (checkCapacityEmpty) {
						// Capacity not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the capacity", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkRPMEmpty) {
						// RPM not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the rpm", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					}
				} else {
					// Modify product
					isRunning = false;
					tempProduct.edit(inputTextDescription.getText(),inputTextBrand.getText(),
							inputTextModelNumber.getText(),inputTextCapacity.getText(),inputTextRPM.getText());
				}
			} else {
				// Pressed cancel
				isRunning = false;
			}
		}
    }
}
