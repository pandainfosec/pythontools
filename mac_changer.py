

import os 
import subprocess        #subprocess is a module to execute os commands


interface = input("specify the interface > ")
mac_address = input("enter the mac address > ")


subprocess.call("ifconfig "+interface+" down", shell=True)
subprocess.call("ifconfig eth0 ether "+mac_address, shell=True)
subprocess.call("ifconfig "+interface+" up", shell=True)
