import nmap
nm = nmap.PortScanner()
print(nm.scan('127.0.0.1', '1-444,8000'))
print(nm.command_line())
# 'nmap -oX - -p 22-443 -sV 127.0.0.1'
print(nm.scaninfo())
# {'tcp': {'services': '22-443', 'method': 'connect'}}
print(nm.all_hosts())
# ['127.0.0.1']
print(nm['127.0.0.1'].hostname())
# 'localhost'
print(nm['127.0.0.1'].state())
# 'up'
print(nm['127.0.0.1'].all_protocols())
# ['tcp']
# nm['127.0.0.1']['tcp'].keys()
# [80, 25, 443, 22, 111]
print(nm['127.0.0.1'].has_tcp(22))
# True
print(nm['127.0.0.1'].has_tcp(23))
print(nm.scanstats())
print(nm._scan_result['scan']['127.0.0.1'])
# False
# nm['127.0.0.1']['tcp'][22]
# {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
# nm['127.0.0.1'].tcp(22)
# {'state': 'open', 'reason': 'syn-ack', 'name': 'ssh'}
# nm['127.0.0.1']['tcp'][22]['state']
# 'open'