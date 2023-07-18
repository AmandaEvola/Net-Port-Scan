import socket 

def scan_ports(target_host, ports):
     """Scan specified ports on the target host."""
     open_ports = []
     for port in ports: 
        try:
               # Create a socket object
               sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               sock.settimeout(1) # Set a timeout for the connection

               # Attempt to connect to the target host and port
               result = sock.connect_ex((target_host, port))
               if result == 0:
                   open_ports.append(port)
               sock.close()
 
        except socket.error:
               continue
        
        return open_ports
          
          
def main():
         target_host = input("Enter the target host IP address: ")
         port_range = input("Enter the range of ports to scan (e.g., 1-100): ")

         # Parse the port range from the input and generate a list of ports to scan
         start_port, end_port = map(int, port_range.split('_'))  
         ports_to_scan = range(start_port, end_port + 1) 

         open_ports = scan_ports(target_host, ports_to_scan)

         if open_ports:
              print(f"Open ports on {target_host}: {', '.join(map(str, open_ports))}")
         else:
              print("No open ports found.")

if __name__ ==  "__main__":
      main()