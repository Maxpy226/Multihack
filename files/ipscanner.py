"""Made by ChatGPT"""



import scapy.all as scapy
import socket


def scan_network(ip_range):
    # Create ARP request packet
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request

    # Send packets and capture responses
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices_list = []
    for element in answered_list:
        device = {"ip": element[1].psrc, "mac": element[1].hwsrc}
        devices_list.append(device)

    return devices_list


def get_hostname(ip):
    try:
        hostname = socket.gethostbyaddr(ip)[0]
    except socket.herror:
        hostname = "Unknown"
    return hostname


def check_common_ports(ip):
    common_ports = [80, 443, 22, 21]
    open_ports = []
    for port in common_ports:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.1)
        result = sock.connect_ex((ip, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports


def main():
    ip_range = "192.168.1.0/24"  # Adjust this to your network range
    devices = scan_network(ip_range)

    print("Devices found on the network:")
    for device in devices:
        ip = device['ip']
        mac = device['mac']
        hostname = get_hostname(ip)
        open_ports = check_common_ports(ip)

        print(f"IP: {ip}, MAC: {mac}, Hostname: {hostname}")
        if open_ports:
            print(f"  Open ports: {', '.join(map(str, open_ports))}")
        print()


if __name__ == "__main__":
    main()
    input()