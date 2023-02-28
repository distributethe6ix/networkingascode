import json
from cisco_nxos import device as dev
from cisco_nxos import exception as exc

# Define the switch connection parameters
switch_ip = '192.168.1.1'
username = 'admin'
password = 'password'

# Define the BGP configuration
bgp_config = {
    "router_bgp": {
        "as": 65000,
        "vrf": {
            "default": {
                "address_family": {
                    "ipv4": {
                        "unicast": {
                            "network": ["10.0.0.0/24"],
                            "neighbor": {
                                "10.0.0.2": {
                                    "remote_as": 65000,
                                    "update_source": "loopback0"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

# Define the VLAN configuration
vlan_config = {
    "vlan": {
        "10": {
            "name": "vlan10"
        },
        "20": {
            "name": "vlan20"
        }
    },
    "interface": {
        "Ethernet1/1": {
            "switchport": {
                "mode": "trunk",
                "trunk": {
                    "allowed": ["10", "20"]
                }
            }
        }
    }
}

# Define the VXLAN configuration
vxlan_config = {
    "vlan": {
        "configuration": ["10-20"]
    },
    "interface": {
        "nve1": {
            "shutdown": False,
            "source_interface": "loopback0",
            "host_reachability_protocol": "bgp",
            "member_vni": {
                "10000": {
                    "rd": "auto",
                    "protocol": {
                        "bgp": {
                            "local_as": 65000,
                            "neighbor": {
                                "10.0.0.2": {}
                            }
                        }
                    }
                }
            }
        }
    }
}

# Connect to the switch
switch = dev.Device(ip=switch_ip, username=username, password=password)

# Configure BGP
try:
    response = switch.send_config(json.dumps(bgp_config))
    print(response)
except exc.CommandError as e:
    print(e)

# Configure VLANs
try:
    response = switch.send_config(json.dumps(vlan_config))
    print(response)
except exc.CommandError as e:
    print(e)

# Configure VXLAN
try:
    response = switch.send_config(json.dumps(vxlan_config))
    print(response)
except exc.CommandError as e:
    print(e)

# Disconnect from the switch
switch.disconnect()
