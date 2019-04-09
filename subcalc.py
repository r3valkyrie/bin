#!/usr/bin/env python3

# IPv4 Subnet calculator by Valkyrie.
#
# Usage: ./subcalc.py [IP]/[CIDR]
#
# Accepts multiple IPv4 addresses and cidr as arguments

from sys import argv
import re


def ip_to_binary(ip):
    # Convert address to binary
    octet_int = address.split('.')
    octet_binary = [format(int(octet), '08b') for octet in octet_int]
    binary = ("").join(octet_binary)
    return binary


def get_subnet_mask(cidr):
    lots_of_ones = '1' * 32
    subnet_mask_bin = lots_of_ones[0:int(cidr)].ljust(32, '0')
    subnet_mask_list_bin = [
        subnet_mask_bin[x:x + 8] for x in range(0, len(subnet_mask_bin), 8)
    ]

    subnet_mask_list = []
    for binary in subnet_mask_list_bin:
        subnet_mask_list.append(str(int(binary, 2)))

    subnet_mask_formatted = '.'.join(subnet_mask_list)
    subnet_mask_bin_formatted = '.'.join(subnet_mask_list_bin)
    return subnet_mask_formatted, subnet_mask_bin_formatted


def get_network_id(address, cidr):
    ip_binary = ip_to_binary(address)
    network_id_bin = ip_binary[0:int(cidr)]
    full_network_id_bin = network_id_bin.ljust(32, '0')
    full_net_id_list_bin = [
        full_network_id_bin[x:x + 8]
        for x in range(0, len(full_network_id_bin), 8)
    ]

    network_id_list = []
    for binary in full_net_id_list_bin:
        network_id_list.append(str(int(binary, 2)))

    print("\n")
    print("IP Address:", address + "/" + cidr)
    print("Subnet ID:", '.'.join(network_id_list) + "/" + cidr)

    subnet_mask = get_subnet_mask(cidr)
    print("Subnet Mask:", subnet_mask[0])
    print("Subnet Mask (Binary):", subnet_mask[1])


for ip in argv[1:]:
    # Split IP from the cidr
    split_ip = re.match(r'^(.*)\/(.*)$', ip)

    address = split_ip.group(1)
    cidr = split_ip.group(2)

    get_network_id(address, cidr)
