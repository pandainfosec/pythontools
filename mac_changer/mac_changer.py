import os 
import subprocess
import optparse


def get_arguments():
     parser = optparse.OptionParser()
     parser.add_option("-i","--interface", dest="interface", help="Interface to change the mac address")
     parser.add_option("-m","--mac", dest="mac_address", help="New mac address")
     (options, arguments) = parser.parse_args()
     if not options.interface:
          #code to handle error
          parser.error(" Please specify the interface, use --help for info.")
     elif not options.new_mac:
          #code to handle error
          parser.error("Please specfiy a new mac address, use --help for more info.")
     return options



def change_mac(interface, mac_address):
     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
     subprocess.call(["ifconfig", interface, "down"])

    
options = get_arguments()
change_mac(options.interface, options.mac_address)






