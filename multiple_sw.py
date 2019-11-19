from netmiko import ConnectHandler

SW1 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '172.16.1.10',
    'username': 'S1',
    'password': 'cisco',
    'secret': 'cisco',
    'verbose': True
}
SW2 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '172.16.1.11',
    'username': 'S2',
    'password': 'cisco',
    'secret': 'cisco',
    'verbose': True
}
SW3 = {
    'device_type': 'cisco_ios_telnet',
    'ip': '172.16.1.12',
    'username': 'S3',
    'password': 'cisco',
    'secret': 'cisco',
    'verbose': True
}

switches = [SW1, SW2, SW3]

for switch in switches:
    connection = ConnectHandler(**switch)
    connection.enable()
    output = connection.send_command('sh ip int brief')
    print(output)
    isConfigModeEnabled = connection.check_config_mode()
    if not isConfigModeEnabled:
        connection.config_mode()

    for vlan in range(2, 4):
        print("Creating Vlan" + str(vlan))
        config_commands = ["vlan " + str(vlan), "name Netmiko" + str(vlan)]
        output = connection.send_config_set(config_commands)
        print(output)

    output = connection.send_command("sh vlan brief")
    print(output)

    connection.disconnect()


