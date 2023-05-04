# DiscordUsernameAvailabilityChecker
A Python script to check if words from a wordlist are available as a Discord username

Discord is changing the way it handles usernames. It is removing the discrimitor and replacing usernames with unique names.  
This is a bad change as it will mean users will compete for unique names to sell on just like every other large service out there.  
You can read more about Discord's rational here: https://discord.com/blog/usernames  

This script is to help you find the username you want. The usernames feature has not yet been released and so changes 
there may be changes to this script later to automate the claiming of names.

# Instructions:

To get started make sure you have Python 3 installed: https://www.python.org/downloads/

Download the files in this repo.  
Open a terminal in the download directory.  
Run the command `pip install -r requirements.txt`

This script requires Discord authentication. To do this you will need to get your Discord Authorization token.  
**DO NOT SHARE THIS WITH ANYBODY. ANYBODY WITH THIS CAN HIJACK YOUR ACCOUNT.**  

To get your Authorization token open Discord in a browser.  
Open developer tools with Ctrl+Shift+i.  
Navigate to the network tab.  
Search for "/api"  
Refresh the page.  
Copy the authorization token from the headers tab of a request and paste it into "main.py".  
For instructions with screenshots follow the guide here: https://www.golinuxcloud.com/discord-token/

Now you are ready to run the script.  
If you have specific names you are looking for replace the words in "usernames.txt" with your list.  
In terminal run the command `python main.py` and the script will run.  
Available names will be output into "available_usernames.txt"