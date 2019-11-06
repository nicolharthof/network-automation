import getpass
import telnetlib


items = ['enable', 'password', 'conf t', 'int loop 0', 'ip address 1.1.1.1 255.255.255.255', 'end', 'exit']


def write_fn(param):
    tn.write((param + '\n').encode('ascii'))


HOST = input("Enter Device IP:")
user = input("Enter your telnet username:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
write_fn(user)

if password:
    tn.read_until(b"Password: ")
    write_fn(password)

for item in items:
    write_fn(item)

x = tn.read_all()
print(x.decode('ascii'))
