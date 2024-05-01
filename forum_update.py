```python
# forum_update.py
import requests

def update_forum_contributions(forum_url, username, contribution_points):
    """
    Updates the hacker's contribution points on a specified hacker forum.
    :param forum_url: URL of the hacker forum.
    :param username: Username of the hacker on the forum.
    :param contribution_points: Points to add to the hacker's profile.
    :return: None
    """
    try:
        # Construct the payload with the necessary data
        payload = {
            'username': username,
            'contribution_points': contribution_points
        }
        
        # Send a POST request to the forum to update the contribution points
        response = requests.post(forum_url, json=payload)
        
        # Check if the update was successful
        if response.status_code == 200:
            print("Forum contribution points updated successfully.")
        else:
            print(f"Failed to update contribution points. Status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred while updating forum contributions: {e}")

if __name__ == "__main__":
    forum_url = "http://example-hacker-forum.com/update_points"
    username = "elite_hacker_2024"
    contribution_points = 500  # Example points to add to the profile

    update_forum_contributions(forum_url, username, contribution_points)
```
