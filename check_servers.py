import os
import multiprocessing

SERVER_LIST_FILE = "servers.txt"

def load_servers():
    """Load servers from the servers.txt file."""
    servers = []
    if os.path.exists(SERVER_LIST_FILE):
        with open(SERVER_LIST_FILE, "r") as f:
            for line in f:
                parts = line.strip().split()
                if len(parts) == 2:
                    servers.append((parts[0], parts[1]))
    return servers

def save_servers(servers):
    """Save the current server list to servers.txt."""
    with open(SERVER_LIST_FILE, "w") as f:
        for name, ip in servers:
            f.write(f"{name} {ip}\n")

def add_server(name, ip):
    servers = load_servers()
    servers.append((name, ip))
    save_servers(servers)

def remove_server_by_name(name):
    servers = load_servers()
    servers = [s for s in servers if s[0] != name]
    save_servers(servers)

def ping_server(server):
    name, ip = server
    result = os.system(f"ping -n 1 -w 2000 {ip} >nul")
    if result != 0:
        return f"{name} ({ip})"
    return None

def check_servers(servers):
    with multiprocessing.Pool(processes=min(10, len(servers))) as pool:
        results = pool.map(ping_server, servers)
    return [r for r in results if r]
