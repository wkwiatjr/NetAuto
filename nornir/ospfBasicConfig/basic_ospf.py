from netmiko import ConnectHandler

devices = '''
172.29.129.11
172.29.129.12
172.29.129.13
172.29.129.14
172.29.129.15
172.29.129.16
172.29.129.17
172.29.129.18
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'wayne'
password = 'cisco'
verbose = True

for device in devices:
        print(" Connecting to Device: " + device)
        net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
        prompter = net_connect.find_prompt()
        if '>' in prompter:
                net_connect.enable()

        output = net_connect.send_command('show run | sec ospf')
        ospf_commands = ['router ospf 1', 'net 0.0.0.0 255.255.255.255 area 0']
        if not 'router ospf' in output:
            print('OSPF is not enabled on device: ' + device)
            answer = input('Would you like you enable default OSPF settings on: ' + device + ' <y/n> ')
            if answer == 'y':
                output = net_connect.send_config_set(ospf_commands)
                print(output)
                print('OSPF is now configured!')
            else:
                print('No OSPF configurations have been made!')

        else:
            print("OSPF is already configured on device: " + device)