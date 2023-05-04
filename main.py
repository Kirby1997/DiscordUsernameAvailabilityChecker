import time
import requests


# Set the Discord authorization token
token = "" # INSERT YOUR TOKEN INTO THE QUOTES. DO NOT SHARE THIS TOKEN.
# IF SHARING THIS FILE, REMEMBER TO REMOVE YOUR TOKEN
headers = {"Authorization": token}

# Discord username API endpoint
endpoint = "https://discord.com/api/v10/users/@me/pomelo"

# Load the list of usernames from the file
with open("usernames.txt") as file:
    usernames = [line.strip() for line in file]


available_usernames = []

# Loop through each username in the list and check availability
for username in usernames:
    url = endpoint
    body = {
        "username": username
    }
    response = requests.post(url, headers=headers, json=body)

    # Rate limit check
    if response.status_code == 429:
        sleep_time = response.json()["retry_after"]
        print(f"Rate limit hit. Sleeping for {sleep_time}s")
        time.sleep(sleep_time)
        response = requests.post(url, headers=headers, json=body)

    #username available check
    if response.json()['code'] == 40001:
        print(f"{username} is available")
        available_usernames.append(username)

    #Username unavailable check
    elif response.json()['code'] == 50035:
        print(f"{username} is taken")

    #Some other error
    else:
        print(f"Error checking {username}: {response.json()['message']}")

# Write available usernames to a file
with open("available_usernames.txt", "w") as file:
    file.write("\n".join(available_usernames))
