#telnet ke switch menggunakan module telnetlib
import telnetlib
#get input password from user using getpass
import getpass

#getting the user information about ip address and username and password add value to variable
host = raw_input("enter switch ip address : ")
user = raw_input("enter your telnet username:")
password = getpass.getpass()

#telnet into variable host that user pass value
tn = telnetlib.Telnet(host)

#read_until means that the script will read user input until the condition ex Username:
tn.read_until("Username: ")
tn.write(user + "\n")
if password:
tn.read_until("Password: ")
tn.write(password + "\n")

#making Vlan10 and 20
tn.write("conf t\n")
tn.write("vlan 10\n")
tn.write("name PythonVlan10\n")
tn.write("vlan 20\n")
tn.write("name PythonVlan20\n")
tn.write("end\n")
tn.write("exit\n")

#print The tellnet
print tn.read_all()
