from cli import cli

# Configure BGP
cli('configure terminal')
cli('router bgp 65000')
cli('address-family ipv4 unicast')
cli('network 10.0.0.0 mask 255.255.255.0')
cli('neighbor 10.0.0.2 remote-as 65000')
cli('neighbor 10.0.0.2 update-source loopback0')
cli('exit')
cli('exit')

# Configure VLANs
cli('configure terminal')
cli('vlan 10')
cli('name vlan10')
cli('vlan 20')
cli('name vlan20')
cli('interface Ethernet1/1')
cli('switchport mode trunk')
cli('switchport trunk allowed vlan 10,20')
cli('exit')
cli('exit')

# Configure VXLAN
cli('configure terminal')
cli('feature nv overlay')
cli('vlan configuration 10-20')
cli('interface nve1')
cli('no shutdown')
cli('source-interface loopback0')
cli('host-reachability protocol bgp')
cli('member vni 10000')
cli('rd auto')
cli('protocol bgp')
cli('local-as 65000')
cli('peer 10.0.0.2')
cli('exit')
cli('exit')
