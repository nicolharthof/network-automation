import pyserial_def


console = pyserial_def.open_console()
pyserial_def.check_initial_configuration(console)
pyserial_def.run_command(console, 'enable')
pyserial_def.run_command(console, 'conf t')
pyserial_def.run_command(console, 'hostname R1')      #zmiana nazwy urządzenia
pyserial_def.run_command(console, 'enable password cisco')
pyserial_def.run_command(console, 'no ip domain-lookup')
pyserial_def.run_command(console, 'ip address 192.168.1.6 255.255.255.0')       #zmiana adresu IP
pyserial_def.run_command(console, 'no sh')
pyserial_def.run_command(console, 'ip default-gateway 192.168.1.1')              #zmiana bramy domyślnej
pyserial_def.run_command(console, 'ip domain-name cisco-lab.com')
pyserial_def.run_command(console, 'crypto key generate rsa modulus 1024')
pyserial_def.run_command(console, 'username R1 password cisco')                 #zmiana username
pyserial_def.run_command(console, 'line vty 0 4')
pyserial_def.run_command(console, 'transport input ssh telnet')
pyserial_def.run_command(console, 'login local')
pyserial_def.run_command(console, 'end')


output = pyserial_def.read_from_console(console)
print(output)

