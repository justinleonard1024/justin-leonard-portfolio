/********************************
 * Product Manager
 * ListADT.java
 * Created by Justin Leonard
********************************/

package adt;

import product.ComputerProduct;

/**
 * Basic list abstract data type interface.
*/
public interface ListADT {
    public void add(ComputerProduct item);
    public void remove(int pos);
    public void clear();
    public ComputerProduct get(int pos);
    public int size();
    public boolean isEmpty();
    public String toString();
}


