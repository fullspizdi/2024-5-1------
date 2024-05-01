```python
# data_mining.py
import requests
import json

def mine_data(target_url, access_token):
    """
    Extracts valuable data from the target's core database using the access token.
    :param target_url: URL of the target's data endpoint.
    :param access_token: Access token for authentication.
    :return: Extracted data or None if the operation fails.
    """
    try:
        headers = {'Authorization': f'Bearer {access_token}'}
        response = requests.get(target_url, headers=headers)
        
        if response.status_code == 200:
            print("Data mining successful.")
            return json.loads(response.text)
        else:
            print(f"Data mining failed. Status code: {response.status_code}")
            return None
    except Exception as e:
        print(f"An error occurred during data mining: {e}")
        return None

if __name__ == "__main__":
    # Example usage
    target_url = 'http://example.com/api/data'
    access_token = 'your_access_token_here'
    
    # Mine data from the target
    data = mine_data(target_url, access_token)
    
    if data:
        print("Extracted Data:", data)
    else:
        print("No data extracted.")
```
