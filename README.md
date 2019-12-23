# Phyton-Network-Automation

topologi jaringan : <br/>
PC: 192.168.99.99/24 e0/0 <br/>
MLS1 : 192.168.99.1/24 e0/0 </br>

//configurasi ip address pada switch <br/>
interface vlan1 <br/>
no shutdown<br/>
ip address 192.168.99.1 255.255.255.0<br/>

//mengaktifkan telnet pada switch<br/>
username user secret user123<br/>
username user previlage 15<br/>
line vty 0 4<br/>
transport input telnet<br/>
login local<br/>


