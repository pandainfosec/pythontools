import os
import subprocess



def nmap(choice, ip_address):
   
    if choice == 1:
       subprocess.call(["nmap", "-T4", "-A", "-v", ip_address])
    elif choice == 2:
       subprocess.call(["nmap", "-sS", "-sU", "-T4", "-A", "-v", ip_address])
    elif choice == 3:
       subprocess.call(["nmap", "-p", "1-65535", "-T4", "-A", "-v", ip_address])
    elif choice == 4:
       subprocess.call(["nmap", "-T4", "-A", "-v", "-Pn", ip_address])
    elif choice == 5:
       subprocess.call(["nmap", "-sn", ip_address])
    elif choice == 6:
       subprocess.call(["nmap", "-T4", "-F", ip_address])
    elif choice == 7:
       subprocess.call(["nmap", "-sV", "-T4", "-O", "-F", ip_address])
    elif choice == 8:
       subprocess.call(["nmap", "-sn", "--traceroute", ip_address])
    elif choice == 9:
       subprocess.call(["nmap", ip_address])
    elif choice == 10:
       subprocess.call(["nmap", "-sC", "-sV", "-sT", ip_address])
    else:
        print("Invalid choice!")
   
    
      



choice = int(input("Enter the number of your scanning choice\n1.  Intense Scan\n2.  Intense Scan Plus UDP\n3.  Intense Scan all TCP Ports\n4.  Intense Scan no ping\n5.  Ping Scan\n6.  Quick Scan\n7.  Quick Scan Plus\n8.  Quick Traceroute\n9.  Regular Scan\n10. Author's favourite \n"))
ip_address = input("Enter the IP Address or URL > ")
             


nmap(choice, ip_address)

           
