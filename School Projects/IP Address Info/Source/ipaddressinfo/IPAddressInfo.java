/********************************
 * IP Address Info
 * IPAddressInfo.java
 * Created by Justin Leonard
********************************/

package ipaddressinfo;

public class IPAddressInfo {
    public static void main(String[] args) {
        // Variables
        int prefixLength;
        String ip;
        
        // Get IP address information
        try {
            // Input
            ip = IPAddress.getIPAddress();
            prefixLength = IPAddress.getPrefixLength();

            // Check
            if(!IPAddress.checkIPAddress(ip)){
                System.out.print("\nError: Invalid IP address\n");
                return;
            }

            if(!IPAddress.checkPrefixLength(prefixLength)){
                System.out.print("\nError: Invalid prefix length\n");
                return;
            }

            // Output
            System.out.printf("\nSubnet address: %s\n", IPAddress.getSubnetAddress(ip,prefixLength));
            System.out.printf("Subnet mask address: %s\n", IPAddress.getSubnetMaskAddress(prefixLength));
            System.out.printf("Default B-cast: %s\n", IPAddress.getDefaultBroadcastAddress(ip,prefixLength));
            System.out.printf("Number of available hosts: %s\n", IPAddress.getAvailableHosts(prefixLength));
            System.out.printf("Address range of hosts: %s\n", IPAddress.getAddressRange(ip,prefixLength));
        }
        catch (Exception e) {
            System.out.print("\nError: Invalid input\n");
        }
    }
}
