```python
# security_monitor.py
import subprocess
import time

def monitor_network_activity(target_ip):
    """
    Monitors network activity for any unusual behavior or potential security threats.
    :param target_ip: IP address of the target system.
    :return: None
    """
    try:
        print(f"Monitoring network activity on {target_ip}...")
        while True:
            # Simulate checking network logs for suspicious activity
            # In a real-world scenario, this would involve analyzing network traffic and logs
            print("Checking for unusual network traffic...")
            result = subprocess.run(['ssh', f'root@{target_ip}', 'tail -n 100 /var/log/syslog'], capture_output=True, text=True)
            
            if "unauthorized" in result.stdout:
                print("Warning: Unauthorized access detected!")
            else:
                print("No unusual activity detected.")
            
            # Sleep for a while before checking again
            time.sleep(10)
    except Exception as e:
        print(f"An error occurred while monitoring network activity: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python security_monitor.py <target_ip>")
        sys.exit(1)
    
    target_ip = sys.argv[1]
    
    # Start monitoring network activity on the specified target system
    monitor_network_activity(target_ip)
```
