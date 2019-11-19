import pyserial_def


console  = pyserial_def.open_console()
pyserial_def.check_initial_configuration(console)
pyserial_def.run_command(console, 'enable')
pyserial_def.run_command(console, 'conf t')
pyserial_def.run_command(console, 'hostname S1')   #zmiana nazwy hosta
pyserial_def.run_command(console, 'enable password cisco')
pyserial_def.run_command(console, 'no ip domain-lookup')
pyserial_def.run_command(console, 'int vlan 1')
pyserial_def.run_command(console, 'ip address 172.16.1.11 255.255.255.0')     #zmiana adresu IP
pyserial_def.run_command(console, 'no sh')
pyserial_def.run_command(console, 'ip default-gateway 172.16.1.1')             #zmiana adresu bramy domyślnej
#pyserial_def.run_command(console, 'ip domain-name cisco-lab.com')
pyserial_def.run_command(console, 'username S1 password cisco')              #zmiana username
pyserial_def.run_command(console, 'line vty 0 4')
pyserial_def.run_command(console, 'transport input telnet')
pyserial_def.run_command(console, 'login local')
pyserial_def.run_command(console, 'end')


output = pyserial_def.read_from_console(console)
print(output)

