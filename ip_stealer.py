import socket
import sys
import nmap

if len(sys.argv) < 2 :
    print('[!] input ip address!\nex) py ip_stealer.py [Ip address] ')
    sys.exit(0)

ip = sys.argv[1]

nm = nmap.PortScanner()

def steal():
    soc = socket.socket()
    try:
        soc.bind((ip, 80))
        print(f'Listening on {ip} ...')
    except:
        print('[ERROR] Network issue ')
        sys.exit(0)
        
    
    while True:
        try:
            soc.listen(5)
            conn, address = soc.accept()
            print(f'[+] IP Logged {str(address[0])}')
            recon = nm.scan(address[0],arguments='-O')
            print('IP_address : '+address[0])

            if 'mac' in recon['scan'][address[0]]['addresses']:
                mac = recon['scan'][address[0]]['addresses']['mac']
            else:
                mac = '-'

            print('Mac_address : '+mac)

            #print('OS_info : '+recon['scan'][address[0]]['osmatch'][0]['osclass'][0]['osfamily'])
            print('OS_info : '+recon['scan'][address[0]]['osmatch'][0]['name'])
            keep = input('[!] Continue?(Y/N): ')

            if keep == 'N' or keep == 'n':
                sys.exit(0)
            else:
                 print(f'Listening on {ip} ...')
                 continue
        
        except:
            print('[!] Interrupt occured')
            soc.close()
            sys.exit(0)
            

        
steal()


