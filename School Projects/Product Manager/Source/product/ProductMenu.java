/********************************
 * Product Manager
 * ProductMenu.java
 * Created by Justin Leonard
********************************/

package product;

import java.awt.Color;
import java.awt.Cursor;
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import javax.swing.BorderFactory;
import javax.swing.JButton;
import javax.swing.JFileChooser;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JSpinner;
import javax.swing.JTextArea;
import javax.swing.SpinnerListModel;
import javax.swing.filechooser.FileNameExtensionFilter;

/**
 * Initializes the user interface and product list.
*/
public class ProductMenu {
	// Fields
	JFrame frameMain;
	JButton buttonAdd, buttonRemove, buttonEdit, buttonInfo, buttonFile, buttonClear, buttonExit;
	JLabel labelInformation, labelOptions, labelName, labelDescription, labelBrand, labelModelNumber, labelType;
	JTextArea textName, textDescription, textBrand, textModelNumber, textType;
	ProductManager productManager;
	ProductMenuUI productUI;
	ArrayList<String> productTypes;
	
	/**
	* Default constructor.
	*/
	public ProductMenu(ProductManager.Type type) {
		// Frame
		this.frameMain = new JFrame();
		
		// Buttons
		this.buttonAdd = new JButton("Add");
		this.buttonRemove = new JButton("Remove");
		this.buttonEdit = new JButton("Edit");
		this.buttonInfo = new JButton("Info");
		this.buttonFile = new JButton("Save To File");
		this.buttonClear = new JButton("Clear");
		this.buttonExit = new JButton("Exit");
		
		// Labels
		this.labelInformation = new JLabel("Information",JLabel.CENTER);
		this.labelOptions = new JLabel("Options",JLabel.CENTER);
		this.labelName = new JLabel("Name",JLabel.CENTER);
		this.labelDescription = new JLabel("Description",JLabel.CENTER);
		this.labelBrand = new JLabel("Brand",JLabel.CENTER);
		this.labelModelNumber = new JLabel("Model Number",JLabel.CENTER);
		this.labelType = new JLabel("Type",JLabel.CENTER);
		
		// Text
		this.textName = new JTextArea();
		this.textDescription = new JTextArea();
		this.textBrand = new JTextArea();
		this.textModelNumber = new JTextArea();
		this.textType = new JTextArea();
		
		// Other
		this.productManager = new ProductManager(type);
		this.productUI = new ProductMenuUI();
		this.productTypes = new ArrayList<String>();
		
		// Product names
		this.productTypes.add("Graphics Card");
		this.productTypes.add("Hard Drive");
		this.productTypes.add("Processor");
	}
	
	/**
	 * The main method to start the product menu.
	 * The user interface and product list will be created.
	 * This will wait for the user input from the button click events.
	 */
	public void start() {
		// Frame
		this.frameMain.setSize(880,820);
		this.frameMain.setLayout(null);
		this.frameMain.setTitle("Computer Company Products");
		this.frameMain.setResizable(false);
		this.frameMain.setLocationRelativeTo(null);
		this.frameMain.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.productUI.setSize(880, 10);
		this.productUI.setLocation(0, 580);
		
		// Buttons
		this.buttonAdd.setSize(150, 25);
		this.buttonAdd.setLocation(172,640);
		this.buttonRemove.setSize(150, 25);
		this.buttonRemove.setLocation(362,640);
		this.buttonEdit.setSize(150, 25);
		this.buttonEdit.setLocation(552,640);
		this.buttonInfo.setSize(150, 25);
		this.buttonInfo.setLocation(172,690);
		this.buttonFile.setSize(150, 25);
		this.buttonFile.setLocation(362,690);
		this.buttonClear.setSize(150, 25);
		this.buttonClear.setLocation(552,690);
		this.buttonExit.setSize(150, 25);
		this.buttonExit.setLocation(362,740);

		// Labels
		this.labelInformation.setSize(150, 25);
		this.labelInformation.setLocation(328, 12);
		this.labelOptions.setSize(150, 25);
		this.labelOptions.setLocation(362, 595);
		this.labelName.setSize(150, 25);
		this.labelName.setLocation(162, 45);
		this.labelDescription.setSize(150, 25);
		this.labelDescription.setLocation(612, 45);
		this.labelBrand.setSize(150, 25);
		this.labelBrand.setLocation(288, 45);
		this.labelModelNumber.setSize(150, 25);
		this.labelModelNumber.setLocation(412, 45);
		this.labelType.setSize(150, 25);
		this.labelType.setLocation(36, 45);
		
		// Text
		this.textName.setSize(125, 460);
		this.textName.setLocation(175, 70);
		this.textName.setBorder(BorderFactory.createLineBorder(Color.BLACK));
		this.textName.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		this.textName.setEditable(false);
		this.textName.setText("");
		
		this.textDescription.setSize(275, 460);
		this.textDescription.setLocation(550, 70);
		this.textDescription.setBorder(BorderFactory.createLineBorder(Color.BLACK));
		this.textDescription.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		this.textDescription.setEditable(false);
		this.textDescription.setText("");
		
		this.textBrand.setSize(125, 460);
		this.textBrand.setLocation(300, 70);
		this.textBrand.setBorder(BorderFactory.createLineBorder(Color.BLACK));
		this.textBrand.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		this.textBrand.setEditable(false);
		this.textBrand.setText("");
		
		this.textModelNumber.setSize(125, 460);
		this.textModelNumber.setLocation(425, 70);
		this.textModelNumber.setBorder(BorderFactory.createLineBorder(Color.BLACK));
		this.textModelNumber.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		this.textModelNumber.setEditable(false);
		this.textModelNumber.setText("");
		
		this.textType.setSize(125, 460);
		this.textType.setLocation(50, 70);
		this.textType.setBorder(BorderFactory.createLineBorder(Color.BLACK));
		this.textType.setCursor(new Cursor(Cursor.DEFAULT_CURSOR));
		this.textType.setEditable(false);
		this.textType.setText("");

		// Finalize UI
		this.frameMain.add(this.productUI);
		this.frameMain.add(this.buttonAdd);
		this.frameMain.add(this.buttonRemove);
		this.frameMain.add(this.buttonEdit);
		this.frameMain.add(this.buttonInfo);
		this.frameMain.add(this.buttonFile);
		this.frameMain.add(this.buttonClear);
		this.frameMain.add(this.buttonExit);
		this.frameMain.add(this.labelInformation);
		this.frameMain.add(this.labelOptions);
		this.frameMain.add(this.labelName);
		this.frameMain.add(this.labelDescription);
		this.frameMain.add(this.labelBrand);
		this.frameMain.add(this.labelModelNumber);
		this.frameMain.add(this.labelType);
		this.frameMain.add(this.textName);
		this.frameMain.add(this.textDescription);
		this.frameMain.add(this.textBrand);
		this.frameMain.add(this.textModelNumber);
		this.frameMain.add(this.textType);
		this.frameMain.setVisible(true);

		// Events
		
		// Add button click
		this.buttonAdd.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Add product
				buttonEventAdd();
				updateInformation();
			}          
		});
		
		// Remove button click
		this.buttonRemove.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Remove product
				buttonEventRemove();
				updateInformation();
			}          
		});
		
		// Edit button click
		this.buttonEdit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Edit product
				buttonEventEdit();
				updateInformation();
			}          
		});
		
		// Info button click
		this.buttonInfo.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Display product info
				buttonEventInfo();
				updateInformation();
			}          
		});
		
		// File button click
		this.buttonFile.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Save to file
				try {
					buttonEventFile();
				} catch (IOException e1) {}
				updateInformation();
			}          
		});
		
		// Clear button click
		this.buttonClear.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// Clear products
				buttonEventClear();
				updateInformation();
			}      
		});

		// Exit button click
		this.buttonExit.addActionListener(new ActionListener() {
			public void actionPerformed(ActionEvent e) {
				// End program
				System.exit(0);
			}
		});
	}
	
	/**
	* Add button click event.
    * Add a product to the product list based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
	*/
	private void buttonEventAdd() {
		// Variables
		int result;
		boolean checkNameEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelType;
		JSpinner inputListType;
		SpinnerListModel modelListType;

		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelType = new JLabel("Type: ",JLabel.LEFT);
		
		// Other
		modelListType = new SpinnerListModel(this.productTypes);
		inputListType = new JSpinner(modelListType);
		
		// Finalize UI
		panelMain.setLayout(new GridLayout(2,1));
		panelMain.add(labelType);
		panelMain.add(inputListType);
		
		// Get result
		while (isRunning) {
			// Open dialog
			result = JOptionPane.showConfirmDialog(null, panelMain, "Please select the type of product", 
					JOptionPane.OK_CANCEL_OPTION);
			
			// Pressed OK
			if (result == JOptionPane.OK_OPTION) {
				// Check values
				checkNameEmpty = inputListType.getValue() == null;
			
				// Error
				if (checkNameEmpty) {
					// Name not selected
					JOptionPane.showConfirmDialog(null, "Error: Please select a type", "Error", 
							JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
				} else {
					// Add product
					isRunning = false;
					
					// Get result
					if (inputListType.getValue().equals("Graphics Card")) {
						// Type selected is Graphics Card
						
						// Create product
						ItemGraphicsCard tempProduct = ItemGraphicsCard.createProduct();
						
						// Error
						if (tempProduct.getName().equals("") || this.productManager.checkExists(tempProduct.getName())) {
							if (this.productManager.checkExists(tempProduct.getName())) {
								// Product already exists
								JOptionPane.showConfirmDialog(null, "Error: Product already exists in this product list", "Error", 
										JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
							}
						} else {
							// Add product
							this.productManager.add(tempProduct);
						}
					} else if (inputListType.getValue().equals("Hard Drive")) {
						// Type selected is Hard Drive
						
						// Create product
						ItemHardDrive tempProduct = ItemHardDrive.createProduct();
						
						// Error
						if (tempProduct.getName().equals("") || this.productManager.checkExists(tempProduct.getName())) {
							if (this.productManager.checkExists(tempProduct.getName())) {
								// Product already exists
								JOptionPane.showConfirmDialog(null, "Error: Product already exists in this product list", "Error", 
										JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
							}
						} else {
							// Add product
							this.productManager.add(tempProduct);
						}
					} else if (inputListType.getValue().equals("Processor")) {
						// Type selected is Processor
						
						// Create product
						ItemProcessor tempProduct = ItemProcessor.createProduct();
						
						// Error
						if (tempProduct.getName().equals("") || this.productManager.checkExists(tempProduct.getName())) {
							if (this.productManager.checkExists(tempProduct.getName())) {
								// Product already exists
								JOptionPane.showConfirmDialog(null, "Error: Product already exists in this product list", "Error", 
										JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
							}
						} else {
							// Add product
							this.productManager.add(tempProduct);
						}
					}
				}
			} else {
				// Pressed cancel
				isRunning = false;
			}
		}
	}
	
	/**
	* Remove button click event.
    * Remove a product from the product list.
    * A message dialog will appear asking the user which product to remove.
	*/
	private void buttonEventRemove() {
		// Variables
		int result;
		boolean checkNameEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelName;
		JSpinner inputListName;
		SpinnerListModel modelListName;
		ArrayList<String> names = new ArrayList<String>();
		
		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelName = new JLabel("Name: ",JLabel.LEFT);
		
		// There are products in this manager
		if (this.productManager.getNumProducts() > 0) {
			// Other
			for (int i = 0; i < this.productManager.getNumProducts(); i++) {
				names.add(this.productManager.getProducts().get(i).getName());
			}
			modelListName = new SpinnerListModel(names);
			inputListName = new JSpinner(modelListName);

			// Finalize UI
			panelMain.setLayout(new GridLayout(2,1));
			panelMain.add(labelName);
			panelMain.add(inputListName);
			
			// Get result
			while (isRunning) {
				// Open dialog
				result = JOptionPane.showConfirmDialog(null, panelMain, "Please select the name of the product", 
						JOptionPane.OK_CANCEL_OPTION);
				
				// Pressed OK
				if (result == JOptionPane.OK_OPTION) {
					// Check values
					checkNameEmpty = inputListName.getValue() == null;
				
					// Error
					if (checkNameEmpty) {
						// Name not selected
						JOptionPane.showConfirmDialog(null, "Error: Please select a name", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else {
						// Remove product
						isRunning = false;
						this.productManager.remove((String)inputListName.getValue());
					}
				} else {
					// Pressed cancel
					isRunning = false;
				}
			}
		} else {
			// There are not products in the product list
			JOptionPane.showConfirmDialog(null, "Error: There are no products in the product list", "Error", 
					JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
		}
	}
	
	/**
	* Edit button click event.
    * Edit a product in the product list based on the input information.
    * A message dialog will appear asking the user to enter in the information about the product.
	*/
	private void buttonEventEdit() {
		// Variables
		int result;
		boolean checkNameEmpty, isRunning = true;
		String type = "";
		JPanel panelMain;
		JLabel labelName;
		JSpinner inputListName;
		SpinnerListModel modelListName;
		ArrayList<String> names = new ArrayList<String>();
		
		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelName = new JLabel("Name: ",JLabel.LEFT);
		
		// There are products in this manager
		if (this.productManager.getNumProducts() > 0) {
			// Other
			for (int i = 0; i < this.productManager.getNumProducts(); i++) {
				names.add(this.productManager.getProducts().get(i).getName());
			}
			modelListName = new SpinnerListModel(names);
			inputListName = new JSpinner(modelListName);

			// Finalize UI
			panelMain.setLayout(new GridLayout(2,1));
			panelMain.add(labelName);
			panelMain.add(inputListName);
			
			// Get result
			while (isRunning) {
				// Open dialog
				result = JOptionPane.showConfirmDialog(null, panelMain, "Please select the name of the product", 
						JOptionPane.OK_CANCEL_OPTION);
				
				// Pressed OK
				if (result == JOptionPane.OK_OPTION) {
					// Check values
					checkNameEmpty = inputListName.getValue() == null;
				
					// Error
					if (checkNameEmpty) {
						// Name not selected
						JOptionPane.showConfirmDialog(null, "Error: Please select a name", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else {
						// Edit product
						isRunning = false;
						
						// Get result
						type = this.productManager.getTypeFromName((String)inputListName.getValue());
						
						if (type.equals("Graphics Card")) {
							// Type selected is Graphics Card
							
							// Create product
							ItemGraphicsCard tempProduct = this.productManager.getProductFromName((String)inputListName.getValue());
							
							// Error
							if (tempProduct != null) {
								ItemGraphicsCard.modifyProduct(tempProduct);
							}
						} else if (type.equals("Hard Drive")) {
							// Type selected is Hard Drive
							
							// Create product
							ItemHardDrive tempProduct = this.productManager.getProductFromName((String)inputListName.getValue());
							
							// Error
							if (tempProduct != null) {
								ItemHardDrive.modifyProduct(tempProduct);
							}
						} else if (type.equals("Processor")) {
							// Type selected is Processor
							
							// Create product
							ItemProcessor tempProduct = this.productManager.getProductFromName((String)inputListName.getValue());
							
							// Error
							if (tempProduct != null) {
								ItemProcessor.modifyProduct(tempProduct);
							}
						}
					}
				} else {
					// Pressed cancel
					isRunning = false;
				}
			}
		} else {
			// There are not products in the product list
			JOptionPane.showConfirmDialog(null, "Error: There are no products in the product list", "Error", 
					JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
		}
	}
	
	/**
	* Information button click event.
	* Show information about the product.
    * A message dialog will appear asking the user which product to get the information for.
	* A message dialog will appear showing the user all of the information about the product.
	*/
	private void buttonEventInfo() {
		// Variables
		int result;
		boolean checkNameEmpty, isRunning = true;
		JPanel panelMain;
		JLabel labelName;
		JSpinner inputListName;
		SpinnerListModel modelListName;
		ArrayList<String> names = new ArrayList<String>();
		
		// Panel
		panelMain = new JPanel();
		
		// Labels
		labelName = new JLabel("Name: ",JLabel.LEFT);
		
		// There are products in this manager
		if (this.productManager.getNumProducts() > 0) {
			// Other
			for (int i = 0; i < this.productManager.getNumProducts(); i++) {
				names.add(this.productManager.getProducts().get(i).getName());
			}
			modelListName = new SpinnerListModel(names);
			inputListName = new JSpinner(modelListName);

			// Finalize UI
			panelMain.setLayout(new GridLayout(2,1));
			panelMain.add(labelName);
			panelMain.add(inputListName);
			
			// Get result
			while (isRunning) {
				// Open dialog
				result = JOptionPane.showConfirmDialog(null, panelMain, "Please select the name of the product", 
						JOptionPane.OK_CANCEL_OPTION);
				
				// Pressed OK
				if (result == JOptionPane.OK_OPTION) {
					// Check values
					checkNameEmpty = inputListName.getValue() == null;
				
					// Error
					if (checkNameEmpty) {
						// Name not selected
						JOptionPane.showConfirmDialog(null, "Error: Please select a name", "Error", 
								JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
					} else {
						// Show product info
						isRunning = false;
						this.productManager.showInfo((String)inputListName.getValue());
					}
				} else {
					// Pressed cancel
					isRunning = false;
				}
			}
		} else {
			// There are not products in the product list
			JOptionPane.showConfirmDialog(null, "Error: There are no products in the product list", "Error", 
					JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
		}
	}
	
	/**
	* File button click event.
    * Save all of the information about each product currently in the product list to a file.
    * A message dialog will appear asking the user to choose a destination to save the file.
	*/
	private void buttonEventFile() throws IOException {
		// Variables
		int result;
		String fileName = "";
        FileWriter fileWriter;
		JFileChooser saveFileDialog;
		
		// There are products in the product list
		if (this.productManager.getNumProducts() > 0) {
			// Save file dialog
			saveFileDialog = new JFileChooser();
			saveFileDialog.setAcceptAllFileFilterUsed(false);
			saveFileDialog.setDialogTitle("Select file to save product list");
			saveFileDialog.setDialogType(JFileChooser.SAVE_DIALOG);
			saveFileDialog.setFileFilter(new FileNameExtensionFilter("Text Files", "txt"));
			saveFileDialog.setFileSelectionMode(JFileChooser.FILES_ONLY);
			result = saveFileDialog.showSaveDialog(null);

			// File saved
			if (result == JFileChooser.APPROVE_OPTION) {
				// Get file name
				fileName = saveFileDialog.getSelectedFile().getAbsolutePath();
				
				// Save file
		        fileWriter = new FileWriter(fileName + ".txt");
		        fileWriter.write("Product Information\r\n\r\n");

				// Write to file
				for (int i = 0; i < this.productManager.getNumProducts(); i++) {
					fileWriter.write(this.productManager.getProducts().get(i).getInfo() + "\r\n\r\n");
				}

				// Close file
				fileWriter.close();
			}
		} else {
			// There are not products in the product list
			JOptionPane.showConfirmDialog(null, "Error: There are no products in the product list", "Error", 
					JOptionPane.DEFAULT_OPTION, JOptionPane.ERROR_MESSAGE);
		}
	}
	
	/**
	* Clear button click event.
    * Clear all products in the product list.
    * A message dialog will appear asking the user if they want to clear all products in the product list.
	*/
	private void buttonEventClear() {
		// Open main dialog
		int result = JOptionPane.showConfirmDialog(null, "Are you sure you want to clear the product list?", "Clear product list", 
				JOptionPane.YES_NO_OPTION, JOptionPane.INFORMATION_MESSAGE);
		
		// Pressed Yes
		if (result == JOptionPane.YES_OPTION) {
			// Clear
			this.textName.setText("");
			this.textDescription.setText("");
			this.textBrand.setText("");
			this.textModelNumber.setText("");
			this.textType.setText("");
			this.productManager.clear();
		}
	}
	
	/**
	* Update all information in the product list user interface.
	* All information regarding the type, name, description, brand and model number will be updated and displayed.
	*/
	private void updateInformation() {
		// Update information
		if (this.productManager.getNumProducts() > 0) {
			// Clear
			this.textName.setText("");
			this.textDescription.setText("");
			this.textBrand.setText("");
			this.textModelNumber.setText("");
			this.textType.setText("");
			
			// Set text
			for (int i = 0; i < this.productManager.getNumProducts(); i++) {
				this.textName.setText(this.textName.getText() + this.productManager.getProducts().get(i).getName() + "\r\n");
				this.textDescription.setText(this.textDescription.getText() + this.productManager.getProducts().get(i).getDescription() + "\r\n");
				this.textBrand.setText(this.textBrand.getText() + this.productManager.getProducts().get(i).getBrand() + "\r\n");
				this.textModelNumber.setText(this.textModelNumber.getText() + this.productManager.getProducts().get(i).getModelNumber() + "\r\n");
				this.textType.setText(this.textType.getText() + this.productManager.getProducts().get(i).getType() + "\r\n");
			}
		} else {
			// Clear
			this.textName.setText("");
			this.textDescription.setText("");
			this.textBrand.setText("");
			this.textModelNumber.setText("");
			this.textType.setText("");
		}
	}
}
