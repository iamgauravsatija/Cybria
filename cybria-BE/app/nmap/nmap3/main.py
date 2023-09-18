# import nmap3

# nmap_scanner = nmap3.Nmap()

# def os_detection(website = "www.hackerspub.org", target_ip=""):
#     if website != "":
#         os_result = nmap3.nmap_os_detection(website)
#     elif target_ip != "":
#         os_result = nmap3.nmap_os_detection(target_ip)
#     else:
#         return "Error No target defined"
    
#     return os_result

# def start_nmap_scan(target_ip, ports="1-66535", arguments = "-sS -sV"):
#     '''
#     For the default values I have choosen the most frequently used setting
#     by me. The settings include information as follows:
#         - Ports: Scanning all ports as even thought, majority of servers are 
#                 running applications on default ports like 22 for SSH. When 
#                 we are attacking a particular target to perform a pentest
#                 we want to be 100% sure.
#         - Arguments or flags:
#             sS: Stealth mode because as a pentester we want to be as quiet
#                 as possible majority of time.
#             sV: To get the version of software/service the client is using,
#                 this is helpful in finding the right exploit on ExploitDB 
#                 & in Metasploit.
#             (discontinued)sA: To detect firewall settings which will be helpful as we can 
#             then implement -f (fragment packets) in later steps to go undetected.
#     '''
