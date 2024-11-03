import socket
from concurrent.futures import ThreadPoolExecutor

def scan_port(ip, port):
    """
    Versucht, eine Verbindung zu einem bestimmten Port auf der IP-Adresse herzustellen.
    Wenn der Port offen ist, wird dies zurückgegeben, andernfalls wird er ignoriert.
    """
    try:
        # Erstellt ein Socket-Objekt
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Setzt einen Timeout, damit die Verbindung nicht ewig hängen bleibt
        sock.settimeout(1)
        # Versucht, den Port zu verbinden
        result = sock.connect_ex((ip, port))
        # Wenn der Rückgabewert 0 ist, ist der Port offen
        if result == 0:
            return port
        sock.close()
    except (socket.timeout, socket.error):
        pass

def scan_ports(ip, port_range):
    """
    Führt den Port-Scan über den gegebenen IP-Bereich mit Multithreading durch.
    """
    print(f"Scanning IP: {ip} in range {port_range[0]}-{port_range[1]}...")
    
    # Verwende einen Thread-Pool für schnelleres Scannen
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:
        # Führt den Port-Scan für jeden Port im angegebenen Bereich durch
        results = executor.map(lambda port: scan_port(ip, port), range(port_range[0], port_range[1] + 1))
    
    # Filtere die offenen Ports heraus
    open_ports = [port for port in results if port is not None]
    
    if open_ports:
        print(f"Offene Ports gefunden: {open_ports}")
    else:
        print("Keine offenen Ports gefunden.")
    
    return open_ports

if __name__ == "__main__":
    target_ip = input("Gib die Ziel-IP ein: ")
    port_range = (1, 600)  # Scanne alle Ports (1-65535)
    scan_ports(target_ip, port_range)
    input()
