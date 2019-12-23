# Phyton-Network-Automation

topologi jaringan : <br/>
PC: 192.168.99.99/24 e0/0 <br/>
MLS1 : 192.168.99.1/24 e0/0 /n

//configurasi ip address pada switch
interface vlan1
no shutdown
ip address 192.168.99.1 255.255.255.0

//mengaktifkan telnet pada switch
username user secret user123
username user previlage 15
line vty 0 4
transport input telnet
login local


