/********************************
 * Product Manager
 * ItemProcessor.java
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
 * Processor product type.
*/
public class ItemProcessor extends ComputerProduct {
	// Fields
	private String cores, frequency;
	private final String TYPE = "Processor";
	
	/**
	 * Default constructor.
	 */
	public ItemProcessor() {
		super("","","","");
		this.cores = "";
		this.frequency = "";
	}
	
	/**
	* Class constructor specifying the name, description, brand, model number, cores and frequency.
	*
	* @param  name the name of the product
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	* @param  cores the cores of the product
	* @param  frequency the frequency of the product
	*/
	public ItemProcessor(String name, String description, String brand, String modelNumber, String cores, String frequency) {
		super(name,description,brand,modelNumber);
		this.cores = cores;
		this.frequency = frequency;
	}
	
	/**
	* Get the cores of the product.
	*
	* @return the cores of the product
	*/
    public String getCores() {
    	return this.cores;
    }
	
    /**
    * Set the cores of the product.
    *
    * @param  cores the cores of the product
    */
    public void setCores(String cores) {
    	this.cores = cores;
    }
	
	/**
	* Get the frequency of the product.
	*
	* @return the frequency of the product
	*/
    public String getFrequency() {
    	return this.frequency;
    }
	
    /**
    * Set the frequency of the product.
    *
    * @param  frequency the frequency of the product
    */
    public void setFrequency(String frequency) {
    	this.frequency = frequency;
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
    			"Cores: " + this.getCores() + "\r\n" +
    			"Frequency: " + this.getFrequency();
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
	* The modified information with be the description, brand, model number, cores and frequency.
	*
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	* @param  cores the cores of the product
	* @param  frequency the frequency of the product
	*/
    public void edit(String description, String brand, String modelNumber, String cores, String frequency) {
    	this.setDescription(description);
    	this.setBrand(brand);
    	this.setModelNumber(modelNumber);
    	this.setCores(cores);
    	this.setFrequency(frequency);
    }
	
    /**
    * Create a product based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
    * The user will be asked to enter the name, description, brand, model number, cores and frequency.
    *
    * @return the created product
    */
    public static ItemProcessor createProduct() {
		// Variables
		int result;
		boolean checkNameEmpty, checkDescriptionEmpty, checkBrandEmpty,
		checkModelNumberEmpty, checkCoresEmpty, checkFrequencyEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelName, labelDescription, labelBrand, labelModelNumber, labelCores, labelFrequency;
		JTextField inputTextName, inputTextDescription, inputTextBrand, inputTextModelNumber, inputTextCores, inputTextFrequency;
		ItemProcessor tempProduct = null;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelName = new JLabel("Name: ",JLabel.RIGHT);
		labelDescription = new JLabel("Description: ",JLabel.RIGHT);
		labelBrand = new JLabel("Brand: ",JLabel.RIGHT);
		labelModelNumber = new JLabel("Model Number: ",JLabel.RIGHT);
		labelCores = new JLabel("Cores: ",JLabel.RIGHT);
		labelFrequency = new JLabel("Frequency: ",JLabel.RIGHT);

		// Text
		inputTextName = new JTextField(15);
		inputTextDescription = new JTextField(15);
		inputTextBrand = new JTextField(15);
		inputTextModelNumber = new JTextField(15);
		inputTextCores = new JTextField(15);
		inputTextFrequency = new JTextField(15);

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
		panelMain.add(labelCores);
		panelMain.add(inputTextCores);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelFrequency);
		panelMain.add(inputTextFrequency);
		
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
				checkCoresEmpty = inputTextCores.getText().isEmpty();
				checkFrequencyEmpty = inputTextFrequency.getText().isEmpty();
			
				// Error
				if (checkNameEmpty || checkDescriptionEmpty || checkBrandEmpty
						|| checkModelNumberEmpty || checkCoresEmpty || checkFrequencyEmpty) {
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
					} else if (checkCoresEmpty) {
						// Cores not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the cores", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkFrequencyEmpty) {
						// Frequency not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the frequency", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					}
				} else {
					// Create product
					isRunning = false;
					tempProduct = new ItemProcessor(inputTextName.getText(),inputTextDescription.getText(),inputTextBrand.getText(),
							inputTextModelNumber.getText(),inputTextCores.getText(),inputTextFrequency.getText());
				}
			} else {
				// Pressed cancel
				isRunning = false;
				tempProduct = new ItemProcessor();
			}
		}
		return tempProduct;
    }
	
    /**
    * Modify a product based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
    * The user will be asked to enter the description, brand, model number, cores and frequency.
    *
	* @param  tempProduct the product to modify
    */
    public static void modifyProduct(ItemProcessor tempProduct) {
		// Variables
		int result;
		boolean checkDescriptionEmpty, checkBrandEmpty, checkModelNumberEmpty,
		checkCoresEmpty, checkFrequencyEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelDescription, labelBrand, labelModelNumber, labelCores, labelFrequency;
		JTextField inputTextDescription, inputTextBrand, inputTextModelNumber, inputTextCores, inputTextFrequency;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelDescription = new JLabel("Description: ",JLabel.RIGHT);
		labelBrand = new JLabel("Brand: ",JLabel.RIGHT);
		labelModelNumber = new JLabel("Model Number: ",JLabel.RIGHT);
		labelCores = new JLabel("Cores: ",JLabel.RIGHT);
		labelFrequency = new JLabel("Frequency: ",JLabel.RIGHT);

		// Text
		inputTextDescription = new JTextField(tempProduct.getDescription(),15);
		inputTextBrand = new JTextField(tempProduct.getBrand(),15);
		inputTextModelNumber = new JTextField(tempProduct.getModelNumber(),15);
		inputTextCores = new JTextField(tempProduct.getCores(),15);
		inputTextFrequency = new JTextField(tempProduct.getFrequency(),15);

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
		panelMain.add(labelCores);
		panelMain.add(inputTextCores);
		panelMain.add(Box.createHorizontalStrut(15));
		panelMain.add(labelFrequency);
		panelMain.add(inputTextFrequency);
		
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
				checkCoresEmpty = inputTextCores.getText().isEmpty();
				checkFrequencyEmpty = inputTextFrequency.getText().isEmpty();
			
				// Error
				if (checkDescriptionEmpty || checkBrandEmpty || checkModelNumberEmpty
						|| checkCoresEmpty || checkFrequencyEmpty) {
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
					} else if (checkCoresEmpty) {
						// Cores not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the cores", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else if (checkFrequencyEmpty) {
						// Frequency not entered
						JOptionPane.showConfirmDialog(null, "Error: Please enter the frequency", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					}
				} else {
					// Modify product
					isRunning = false;
					tempProduct.edit(inputTextDescription.getText(),inputTextBrand.getText(),
							inputTextModelNumber.getText(),inputTextCores.getText(),inputTextFrequency.getText());
				}
			} else {
				// Pressed cancel
				isRunning = false;
			}
		}
    }
}
