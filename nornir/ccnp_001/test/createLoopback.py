from netmiko import ConnectHandler
from colorama import Fore, Style

devices = '''
172.29.129.2
172.29.129.3
172.29.129.4
172.29.129.5
172.29.129.6
172.29.129.7
172.29.129.8
172.29.129.9
172.29.129.10
172.29.129.11
172.29.129.12
172.29.129.13
'''.strip().splitlines()

device_type = 'cisco_ios'
username = 'wayne'
password = 'cisco'
verbose = True

for device in devices:
    print("\n")
    print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
    print(" " * 26 + "Welcome to " + Fore.RED + "Netmiko!" + Style.RESET_ALL)
    print(" " * 6 + Fore.GREEN + "This is a script to create Loopbacks for my CCNP_001 Lab!" + Style.RESET_ALL)
    print(Fore.YELLOW + "#" * 70 + Style.RESET_ALL)
    print(" Connecting to Device: " + device)
    net_connect = ConnectHandler(ip=device, device_type=device_type, username=username, password=password)
    prompter = net_connect.find_prompt()
    if '>' in prompter:
            net_connect.enable()

    output = net_connect.send_command('show ip int br')
    loopAdd = device[11:] + '.' + device[11:] + '.' + device[11:] + '.' + device[11:] + ' 255.255.255.255'
    loop_commands = ['conf t', 'int l0', 'ip add ' + loopAdd]
    if not 'Loopback0' in output:
        print('No Loopbacks are enabled on device: ' + device)
        answer = input('Would you like you enable default Loopback settings on: ' + device + ' <y/n> ')
        if answer == 'y':
            output = net_connect.send_config_set(loop_commands)
            print(output)
            print('Loopbacks are now configured!')
        else:
            print('No changes have been made!')

    else:
        print("Loopbacks are already configured on device: " + device)