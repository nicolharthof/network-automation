from netmiko import ConnectHandler

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


for vlan in range (10,51,100):
    config_commands = ["vlan " + str(vlan),"name NetmikoVLAN" + str(vlan)]
    output = connection.send_config_set(config_commands)
    print(output)


output = connection.send_command("show vlan brief")
print(output)

connection.disconnect()
