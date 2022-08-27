/********************************
 * Product Manager
 * Node.java
 * Created by Justin Leonard
********************************/

package adt;

import product.ComputerProduct;

/**
 * Node for linked list.
*/
public class Node {
	// Fields
    private ComputerProduct contents;
    private Node next;
    
	/**
	* Class constructor specifying the node to add.
	*
	* @param  toHold the node to add
	*/
    public Node(ComputerProduct toHold) {
        this.contents = toHold;
        next = null;
    }
	
	/**
	* Get the contents of this node.
	* 
	* @return the contents of this node
	*/
    public ComputerProduct getContents() {
        return this.contents;
    }
	
	/**
	* Get the next node.
	*
	* @return the next node
	*/
    public Node getNext() {
        return this.next;
    }
	
	/**
	* Set the next node.
	*
	* @param  aNode the node to set
	*/
    public void setNext (Node aNode) {
        this.next = aNode;
    }
}