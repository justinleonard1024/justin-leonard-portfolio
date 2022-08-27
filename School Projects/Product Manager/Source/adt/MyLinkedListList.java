/********************************
 * Product Manager
 * MyLinkedListList.java
 * Created by Justin Leonard
********************************/

package adt;

import product.ComputerProduct;

/**
 * Linked list based list abstract data type implementation.
*/
public class MyLinkedListList implements ListADT {
	// Fields
    private Node first;
    private int currSize;
	
	/**
	* Default constructor.
	*/
    public MyLinkedListList() {
        this.first = null; 
        this.currSize = 0;
    }
	
	/**
	* Add an item to the list.
	*
	* @param  item the item to add 
	*/
    public void add(ComputerProduct item) {
        Node newNode = new Node(item);
        newNode.setNext(this.first);
        this.first = newNode;      
        this.currSize++;
    }
	
	/**
	* Remove an item from the list.
	*
	* @param  pos position of the item
	*/
    public void remove(int pos) {
    	// Variables
        Node thingBefore = null;
        Node current = this.first;
        
    	// Array is not empty
    	if (!this.isEmpty()) {
    		// Input position is valid
        	if (pos < this.currSize) {
        		// Removing first item
        		if (pos == 0) {
                    this.first = this.first.getNext();
                    this.currSize--;
                } else {
                	// Find the node before the one to be deleted
                	for (int i = 0; i < pos; i++) {
                        thingBefore = current;
                        current = current.getNext();
                	}
                    
                    // Connect the node before to the one after
                    thingBefore.setNext(current.getNext());
                    this.currSize--;
                }
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
        this.first = null; 
        this.currSize = 0;
    }
	
	/**
	* Get an item from the list.
	*
	* @param  pos position of the item
	* @return the item
	*/
    public ComputerProduct get(int pos) {
    	// Variables
        Node current = this.first;
    	
    	// Array is not empty
    	if (!this.isEmpty()) {
    		// Input position is valid
        	if (pos < this.currSize) {
            	// Find the node before the one to be deleted
            	for (int i = 0; i < pos; i++) {
                    current = current.getNext();
            	}
        	} else {
        		throw new IndexOutOfBoundsException("Invalid position");
        	}
    	} else {
    		throw new IllegalArgumentException("List is empty");
    	}
    	
    	// Return item
    	return current.getContents();
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
        Node current = this.first;

    	// Array is not empty
        if (!this.isEmpty()) {
        	// Get info
            for (int pos = 0; pos < this.currSize; pos++) {
                result += "\n" + current.getContents().getInfo();
                current = current.getNext();
            }
        }
        
        // Return result
        return result;
    }    
}
