import getpass
import telnetlib

HOST = input("Enter Device IP:")
user = input("Enter your telnet username:")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"Username: ")
tn.write((user + "\n").encode('ascii'))
if password:
    tn.read_until(b"Password: ")
    tn.write((password + "\n").encode('ascii'))


def writefn(param):
    tn.write((param + "\n").encode('ascii'))


items = ["enable", "cisco", "conf t", "enable", "int loop 0", "ip address 1.1.1.1 255.255.255.255",
         "end", "exit"]

for item in items:
    writefn(item)

x = tn.read_all()
print(x)
