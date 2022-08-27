/********************************
 * IP Address Info
 * IPAddress.java
 * Created by Justin Leonard
********************************/

package ipaddressinfo;

import java.util.Scanner;

public class IPAddress {
    public static final String DEFAULT_IP = "127.127.127.127";
    public static final String DEFAULT_IP_ERROR = "0.0.0.0";
    public static final int DEFAULT_PREFIX_LENGTH = 8;
    public static final int DEFAULT_PREFIX_LENGTH_ERROR = -1;
    
    public static final char VALUE_BIN_0 = '0';
    public static final char VALUE_BIN_1 = '1';
    public static final String VALUE_IP_PART_DEFAULT = "01111111";
    public static final int VALUE_IP_PART_1 = 0;
    public static final int VALUE_IP_PART_2 = 1;
    public static final int VALUE_IP_PART_3 = 2;
    public static final int VALUE_IP_PART_4 = 3;
    public static final int VALUE_MIN_IP_LENGTH = 7;
    public static final int VALUE_MIN_PREFIX_LENGTH = 1;
    public static final int VALUE_MAX_IP_LENGTH = 15;
    public static final int VALUE_MAX_IP_PARTS = 4;
    public static final int VALUE_MAX_PREFIX_LENGTH = 32;
    
    public static String getIPAddress() {
        // Variables
        String ip;
        Scanner scan;
        
        // Get IP address
        scan = new Scanner(System.in);
        System.out.print("Please input a IPv4 address: ");
        ip = scan.nextLine();
        
        // Check IP address
        if (!IPAddress.checkIPAddress(ip))
            ip = IPAddress.DEFAULT_IP_ERROR;
        
        // Return
        return ip;
    }
    
    public static int getPrefixLength() {
        // Variables
        int prefixLength;
        Scanner scan;
        
        // Get prefix length
        scan = new Scanner(System.in);
        System.out.print("Please input the prefix length: ");
        prefixLength = scan.nextInt();
        
        // Check prefix length
        if (!IPAddress.checkPrefixLength(prefixLength))
            prefixLength = IPAddress.DEFAULT_PREFIX_LENGTH_ERROR;
        
        // Return
        return prefixLength;
    }
    
    public static String getSubnetAddress(String ip, int prefixLength) {
        // Variables
        int[] ipArray;
        String[] ipNumbers;
        StringBuilder binaryBuilder;
        
        // Set
        ipArray = new int[]{127, 127, 127, 127};
        ipNumbers = IPAddress.convertIPAddressToBinaryArray(ip);
        
        // Get
        for (int i = prefixLength; i < IPAddress.VALUE_MAX_PREFIX_LENGTH; i++) {
            if(i >= 0 && i < 8) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_1]);
                binaryBuilder.setCharAt(i, IPAddress.VALUE_BIN_0);
                ipNumbers[IPAddress.VALUE_IP_PART_1] = binaryBuilder.toString();
            }
            else if(i >= 8 && i < 16) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_2]);
                binaryBuilder.setCharAt(i - 8, IPAddress.VALUE_BIN_0);
                ipNumbers[IPAddress.VALUE_IP_PART_2] = binaryBuilder.toString();
            }
            else if(i >= 16 && i < 24) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_3]);
                binaryBuilder.setCharAt(i - 16, IPAddress.VALUE_BIN_0);
                ipNumbers[IPAddress.VALUE_IP_PART_3] = binaryBuilder.toString();
            }
            else if(i >= 24 && i < 32) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_4]);
                binaryBuilder.setCharAt(i - 24, IPAddress.VALUE_BIN_0);
                ipNumbers[IPAddress.VALUE_IP_PART_4] = binaryBuilder.toString();
            }
        }
        
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            try {
                ipArray[i] = Integer.parseInt(ipNumbers[i], 2);
            }
            catch (NumberFormatException e) {
                return IPAddress.DEFAULT_IP;
            }
        }
        
        // Return
        return IPAddress.convertArrayToIPAddress(ipArray);
    }
    
    public static String getSubnetMaskAddress(int prefixLength) {
        // Variables
        int[] ipArray;
        String[] ipNumbers;
        
        // Set
        ipArray = new int[]{127, 127, 127, 127};
        ipNumbers = IPAddress.convertPrefixLengthToBinaryArray(prefixLength);
        
        // Get
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            try {
                ipArray[i] = Integer.parseInt(ipNumbers[i], 2);
            }
            catch (NumberFormatException e) {
                return IPAddress.DEFAULT_IP;
            }
        }
        
        // Return
        return IPAddress.convertArrayToIPAddress(ipArray);
    }
    
    public static String getDefaultBroadcastAddress(String ip, int prefixLength) {
        // Variables
        int[] ipArray;
        String[] ipNumbers;
        StringBuilder binaryBuilder;
        
        // Set
        ipArray = new int[]{127, 127, 127, 127};
        ipNumbers = IPAddress.convertIPAddressToBinaryArray(ip);
        
        // Get
        for (int i = prefixLength; i < IPAddress.VALUE_MAX_PREFIX_LENGTH; i++) {
            if(i >= 0 && i < 8) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_1]);
                binaryBuilder.setCharAt(i, IPAddress.VALUE_BIN_1);
                ipNumbers[IPAddress.VALUE_IP_PART_1] = binaryBuilder.toString();
            }
            else if(i >= 8 && i < 16) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_2]);
                binaryBuilder.setCharAt(i - 8, IPAddress.VALUE_BIN_1);
                ipNumbers[IPAddress.VALUE_IP_PART_2] = binaryBuilder.toString();
            }
            else if(i >= 16 && i < 24) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_3]);
                binaryBuilder.setCharAt(i - 16, IPAddress.VALUE_BIN_1);
                ipNumbers[IPAddress.VALUE_IP_PART_3] = binaryBuilder.toString();
            }
            else if(i >= 24 && i < 32) {
                binaryBuilder = new StringBuilder(ipNumbers[IPAddress.VALUE_IP_PART_4]);
                binaryBuilder.setCharAt(i - 24, IPAddress.VALUE_BIN_1);
                ipNumbers[IPAddress.VALUE_IP_PART_4] = binaryBuilder.toString();
            }
        }
        
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            try {
                ipArray[i] = Integer.parseInt(ipNumbers[i], 2);
            }
            catch (NumberFormatException e) {
                return IPAddress.DEFAULT_IP;
            }
        }
        
        // Return
        return IPAddress.convertArrayToIPAddress(ipArray);
    }
    
    public static String getAvailableHosts(int prefixLength) {
        // Variables
        int hosts;
        
        // Get
        hosts = (int)(Math.pow(2, IPAddress.VALUE_MAX_PREFIX_LENGTH - prefixLength) - 2);
        
        // Return
        return Integer.toString(hosts);
    }
    
    public static String getAddressRange(String ip, int prefixLength) {
        // Variables
        String ipSubnet, ipBroadcast, ipFinal;
        int[] ipArray;
        
        // Get
        ipArray = IPAddress.convertIPAddressToArray(IPAddress.getSubnetAddress(ip, prefixLength));
        ipArray[IPAddress.VALUE_IP_PART_4]++;
        ipSubnet = IPAddress.convertArrayToIPAddress(ipArray);
        
        ipArray = IPAddress.convertIPAddressToArray(IPAddress.getDefaultBroadcastAddress(ip, prefixLength));
        ipArray[IPAddress.VALUE_IP_PART_4]--;
        ipBroadcast = IPAddress.convertArrayToIPAddress(ipArray);
        
        // Final
        ipFinal = String.format("%s ~ %s", ipSubnet, ipBroadcast);
        
        // Return
        return ipFinal;
    }
    
    public static boolean checkIPAddress(String ip) {
        // Variables
        boolean isValid = true;
        String[] ipNumbers = ip.split("\\.");
        
        // Check IP address
        if(ipNumbers.length != IPAddress.VALUE_MAX_IP_PARTS || ipNumbers[IPAddress.VALUE_IP_PART_4] == "0"
                || ip.length() < IPAddress.VALUE_MIN_IP_LENGTH || ip.length() > IPAddress.VALUE_MAX_IP_LENGTH
                || ip == IPAddress.DEFAULT_IP_ERROR || ip.contains("[a-zA-Z]+"))
            isValid = false;
        
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            try {
                if(Integer.parseInt(ipNumbers[i]) < 0 || Integer.parseInt(ipNumbers[i]) > 255)
                    isValid = false;
            }
            catch (NumberFormatException e) {
                isValid = false;
            }
        }
        
        // Return
        return isValid;
    }
    
    public static boolean checkIPAddressArray(int[] ipArray) {
        // Variables
        boolean isValid = true;
        
        // Check IP address array
        if (ipArray.length != IPAddress.VALUE_MAX_IP_PARTS)
            isValid = false;
        
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            if(ipArray[i] < 0 || ipArray[i] > 255)
                isValid = false;
        }
        
        // Return
        return isValid;
    }
    
    public static boolean checkPrefixLength(int prefixLength) {
        // Variables
        boolean isValid = true;
        
        // Check prefix length
        if (prefixLength < IPAddress.VALUE_MIN_PREFIX_LENGTH
                || prefixLength > IPAddress.VALUE_MAX_PREFIX_LENGTH
                || prefixLength == IPAddress.DEFAULT_PREFIX_LENGTH_ERROR)
            isValid = false;
        
        // Return
        return isValid;
    }
    
    public static int[] convertIPAddressToArray(String ip) {
        // Variables
        int[] ipArray;
        String[] ipNumbers;
        
        // Check IP address
        if (!IPAddress.checkIPAddress(ip))
            return new int[]{127, 127, 127, 127};
        
        // Split array
        ipArray = new int[]{127, 127, 127, 127};
        ipNumbers = ip.split("\\.");
        
        // Get IP numbers
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            try {
                ipArray[i] = Integer.parseInt(ipNumbers[i]);
            }
            catch (NumberFormatException e) {
                return new int[]{127, 127, 127, 127};
            }
        }
        
        // Return
        return ipArray;
    }
    
    public static String convertArrayToIPAddress(int[] ipArray) {
        // Variables
        String ip = "";
        
        // Check IP address array
        if (!IPAddress.checkIPAddressArray(ipArray))
            return IPAddress.DEFAULT_IP;
        
        // Get IP address
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            try {
                ip += Integer.toString(ipArray[i]) + (i != 3 ? "." : "");
            }
            catch (Exception e) {
                return IPAddress.DEFAULT_IP;
            }
        }
        
        // Return
        return ip;
    }
    
    public static String[] convertIPAddressToBinaryArray(String ip) {
        // Variables
        String mainBin, tempBin, defBin = "00000000";
        int[] ipArray = IPAddress.convertIPAddressToArray(ip);
        String[] binaryArray = new String[]{"01111111", "01111111", "01111111", "01111111"};
        
        // Check IP address
        if (!IPAddress.checkIPAddress(ip))
            return new String[]{"01111111", "01111111", "01111111", "01111111"};
        
        // Convert
        for (int i = 0; i < IPAddress.VALUE_MAX_IP_PARTS; i++) {
            mainBin = Integer.toBinaryString(ipArray[i]);
            tempBin = "";
            
            if(mainBin.length() < 8) {
                tempBin = defBin.substring(mainBin.length());
            }
            
            binaryArray[i] = tempBin + mainBin;
        }
        
        // Return
        return binaryArray;
    }
    
    public static String[] convertPrefixLengthToBinaryArray(int prefixLength) {
        // Variables
        String[] binaryArray = new String[]{"00000000", "00000000", "00000000", "00000000"};
        StringBuilder binaryBuilder;
        
        // Check prefix length
        if (!IPAddress.checkPrefixLength(prefixLength))
            return new String[]{"01111111", "01111111", "01111111", "01111111"};
        
        // Convert
        for (int i = 0; i < prefixLength; i++) {
            if(i >= 0 && i < 8) {
                binaryBuilder = new StringBuilder(binaryArray[IPAddress.VALUE_IP_PART_1]);
                binaryBuilder.setCharAt(i, IPAddress.VALUE_BIN_1);
                binaryArray[IPAddress.VALUE_IP_PART_1] = binaryBuilder.toString();
            }
            else if(i >= 8 && i < 16) {
                binaryBuilder = new StringBuilder(binaryArray[IPAddress.VALUE_IP_PART_2]);
                binaryBuilder.setCharAt(i - 8, IPAddress.VALUE_BIN_1);
                binaryArray[IPAddress.VALUE_IP_PART_2] = binaryBuilder.toString();
            }
            else if(i >= 16 && i < 24) {
                binaryBuilder = new StringBuilder(binaryArray[IPAddress.VALUE_IP_PART_3]);
                binaryBuilder.setCharAt(i - 16, IPAddress.VALUE_BIN_1);
                binaryArray[IPAddress.VALUE_IP_PART_3] = binaryBuilder.toString();
            }
            else if(i >= 24 && i < 32) {
                binaryBuilder = new StringBuilder(binaryArray[IPAddress.VALUE_IP_PART_4]);
                binaryBuilder.setCharAt(i - 24, IPAddress.VALUE_BIN_1);
                binaryArray[IPAddress.VALUE_IP_PART_4] = binaryBuilder.toString();
            }
        }
        
        // Return
        return binaryArray;
    }
}
