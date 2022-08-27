/********************************
 * Product Manager
 * ComputerProduct.java
 * Created by Justin Leonard
********************************/

package product;

/**
 * Base class for the products.
*/
public abstract class ComputerProduct {
	// Fields
	private String name, description, brand, modelNumber;
	
	/**
	* Class constructor specifying the name, description, brand and model number.
	*
	* @param  name the name of the product
	* @param  description the description of the product
	* @param  brand the brand of the product
	* @param  modelNumber the model number of the product
	*/
	public ComputerProduct(String name, String description, String brand, String modelNumber) {
    	this.name = name;
    	this.description = description;
    	this.brand = brand;
    	this.modelNumber = modelNumber;
	}
	
	/**
	* Get the name of the product.
	*
	* @return the name of the product
	*/
    public String getName() {
    	return this.name;
    }
	
    /**
    * Set the name of the product.
    *
    * @param  name the name of the product
    */
    public void setName(String name) {
    	this.name = name;
    }
	
	/**
	* Get the description of the product.
	*
	* @return the description of the product
	*/
    public String getDescription() {
    	return this.description;
    }
	
    /**
    * Set the description of the product.
    *
    * @param  description the description of the product
    */
    public void setDescription(String description) {
    	this.description = description;
    }
	
	/**
	* Get the brand of the product.
	*
	* @return the brand of the product
	*/
    public String getBrand() {
    	return this.brand;
    }
	
    /**
    * Set the brand of the product.
    *
    * @param  brand the brand of the product
    */
    public void setBrand(String brand) {
    	this.brand = brand;
    }
	
	/**
	* Get the model number of the product.
	*
	* @return the model number of the product
	*/
    public String getModelNumber() {
    	return this.modelNumber;
    }
	
    /**
    * Set the model number of the product.
    *
    * @param  modelNumber the model number of the product
    */
    public void setModelNumber(String modelNumber) {
    	this.modelNumber = modelNumber;
    }

    /**
    * Abstract methods for future implementation.
    */
    public abstract String getInfo();
    public abstract String getType();
}
