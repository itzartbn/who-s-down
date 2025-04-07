import os
import multiprocessing

SERVER_LIST_FILE = "servers.txt"

def load_servers(filename):
    """Load servers from a file. Each line should contain 'name ip_address'."""
    servers = []
    with open(filename, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) == 2:
                servers.append((parts[0], parts[1]))
    return servers

def ping_server(server):
    """Ping a server and return its name & IP if it's down (Windows version)."""
    name, ip = server
    response = os.system(f"ping -n 1 -w 2000 {ip} >nul")
    if response != 0:
        return name, ip
    return None


def check_servers():
    """Check all servers in parallel and report any that are down."""
    servers = load_servers(SERVER_LIST_FILE)
    
    with multiprocessing.Pool(processes=len(servers)) as pool:
        results = pool.map(ping_server, servers)
    
    down_servers = [res for res in results if res]  # Filter out None values

    if down_servers:
        print("The following servers are not responding:")
        for name, ip in down_servers:
            print(f"{name} ({ip})")
            input("Press Enter to exit...")
    else:
        print("All servers are up.")
        input("Press Enter to exit...")

if __name__ == "__main__":
    check_servers()
