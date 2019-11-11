import test
from netmiko import ConnectHandler

console  = test.open_console()
#test.check_initial_configuration(console)
test.run_command(console,'enable')
test.run_command(console, 'conf t')
test.run_command(console, 'enable password cisco')
test.run_command(console, 'no ip domain-lookup')
test.run_command(console, 'int vlan 1')
test.run_command(console, 'ip address 192.168.1.11 255.255.255.0')
test.run_command(console, 'no sh')
test.run_command(console, 'ip default-gateway 192.168.1.1')
test.run_command(console, 'hostname Nicol')
test.run_command(console, 'ip domain-name cisco-lab.com')
test.run_command(console, 'username S1 password cisco')
test.run_command(console, 'line vty 0 4')
test.run_command(console, 'transport input telnet')
test.run_command(console, 'login local')
test.run_command(console, 'end')


output = test.read_from_console(console)
print(output)


cisco_device = {
    'device_type': 'cisco_ios_telnet',
    'ip': '192.168.1.11',
    'username': 's1',
    'password': 'cisco',
    'secret': 'cisco',
    'verbose': True
     }


connection = ConnectHandler(**cisco_device)
connection.enable()

output = connection.send_command('sh ip int brief')
print(output)


for vlan in range (10, 51, 100):
    config_commands = ["vlan " + str(vlan) + "name NetmikoVLAN" + str(vlan)]
    output = connection.send_config_set(config_commands)
    print(output)


output = connection.send_command("show vlan brief")
print(output)

connection.disconnect()
