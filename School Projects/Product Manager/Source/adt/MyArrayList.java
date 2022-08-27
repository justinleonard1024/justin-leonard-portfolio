/********************************
 * Product Manager
 * MyArrayList.java
 * Created by Justin Leonard
********************************/

package adt;

import product.ComputerProduct;

/**
 * Array based list abstract data type implementation.
*/
public class MyArrayList implements ListADT {
	// Fields
    private ComputerProduct[] data;
    private int maxSize, currSize;
	
	/**
	* Default constructor.
	*/
    public MyArrayList() {
        this.maxSize = 100;
        this.currSize = 0;
        this.data = new ComputerProduct[this.maxSize];
    }
	
	/**
	* Add an item to the list.
	*
	* @param  item the item to add 
	*/
    public void add(ComputerProduct item) {
    	// Variables
		ComputerProduct[] tempData;

		// Current size to high
    	if (this.currSize >= this.maxSize) {
    		// Double max size
    		this.maxSize *= 2;
    		tempData = new ComputerProduct[this.maxSize];
    		
    		// Copy array
    		System.arraycopy(this.data, 0, tempData, 0, this.maxSize / 2);
    		
    		// Set item
    		this.data = tempData;
            this.data[this.currSize] = item;
            this.currSize++;
    	} else {
    		// Set item
            this.data[this.currSize] = item;
            this.currSize++;
    	}
    }
	
	/**
	* Remove an item from the list.
	*
	* @param  pos position of the item
	*/
    public void remove(int pos) {
    	// Array is not empty
    	if (!this.isEmpty()) {
    		// Input position is valid
        	if (pos < this.currSize) {
        		// Remove item
                for (int i = pos; i < this.currSize-1; i++) {
                    this.data[i+1] = this.data[i];
                }
                
                // Correct size
                this.data[this.currSize-1] = null;
                this.currSize--;
        	} else {
        		throw new IndexOutOfBoundsException("Invalid position");
        	}
    	} else {
    		throw new IllegalArgumentException("List is empty");
    	}
    }
	
	/**
	* Clear the list.
	*/
    public void clear() {
    	// Set sizes
    	this.maxSize = 100;
        this.currSize = 0;
        
        // Set empty array
        this.data = new ComputerProduct[this.maxSize];
    }
	
	/**
	* Get an item from the list.
	*
	* @param  pos position of the item
	* @return the item
	*/
    public ComputerProduct get(int pos) {
    	// Array is not empty
    	if (!this.isEmpty()) {
    		// Input position is valid
        	if (pos < this.currSize) {
        		// Return item
        		return this.data[pos];
        	} else {
        		throw new IndexOutOfBoundsException("Invalid position");
        	}
    	} else {
    		throw new IllegalArgumentException("List is empty");
    	}
    }
	
	/**
	* Get the number of items in the list.
	*
	* @return the number of items in the list
	*/
    public int size() {
		// Return size
    	return this.currSize;
    }
	
	/**
	* Get if the list is empty.
	*
	* @return if the list is empty
	*/
    public boolean isEmpty() {
		// Return if array is empty
        return this.currSize == 0;
    }
	
	/**
	* Get the info of the item.
	*
	* @return the info of the item
	*/
    public String toString() {
    	// Variables
        String result = "";

    	// Array is not empty
        if (!this.isEmpty()) {
        	// Get info
            for (int pos = 0; pos < this.currSize; pos++) {
                result += "\n" + this.data[pos].getInfo();
            }
        }
        
        // Return result
        return result;
    }
}
