import nmap


def start_nmap_scan(target_ip, ports="1-66535", arguments = "-sS -sV"):
    '''
    For the default values I have choosen the most frequently used setting
    by me. The settings include information as follows:
        - Ports: Scanning all ports as even thought, majority of servers are 
                running applications on default ports like 22 for SSH. When 
                we are attacking a particular target to perform a pentest
                we want to be 100% sure.
        - Arguments or flags:
            sS: Stealth mode because as a pentester we want to be as quiet
                as possible majority of time.
            sV: To get the version of software/service the client is using,
                this is helpful in finding the right exploit on ExploitDB 
                & in Metasploit.
            (discontinued)sA: To detect firewall settings which will be helpful as we can 
            then implement -f (fragment packets) in later steps to go undetected.
    '''
    nmap_scanner = nmap.PortScanner()
    result = nmap_scanner.scan('127.0.0.1', '1-1000')
    

    # print(result['scan'][f'{target_ip}'].keys())
    # print(result['scan'][f'{target_ip}']['22']['state'])
    # for proto in result[target_ip].all_protocols():
    #     print('----------')
    #     print('Protocol : %s' % proto)
    #     lport = result[target_ip][proto].keys()
    #     lport.sort()
    #     for port in lport:
    #         print ('port : %s\tstate : %s' % (port, result[host][proto][port]['state']))
    # for host, scan_result in result.all_hosts().items():
    #     open_ports = []
    #     for port, port_info in scan_result['tcp'].items():
    #         if port_info['state'] == 'open':
    #             open_ports.append(port)
    #     scan_results[host] = {
    #         'host': host,
    #         'status': scan_result['status']['state'],
    #         'open_ports': open_ports,
    #     }
        
    return result 
