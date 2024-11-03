import pyautogui
import time
import webbrowser
from tqdm import tqdm
import json
import random
import string
import os




currentpath = os.getcwd()

configpath = currentpath + r'\configs'

with open(rf'{configpath}\pyspamconfig.json', 'r') as f:
    data = json.load(f)

mcount = data['messagecount']

message = data["message"]

# Function to generate a random string
def generate_random_string(length):
    # Define the characters to choose from
    characters = string.ascii_letters + string.digits
    # Generate the random string
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# Generate a random string of length 10



webbrowser.open("web.whatsapp.com")
time.sleep(15)
print("now sending " + str(mcount) + " messages to chosen contact")

for i in tqdm(range(mcount)):
    random_string = generate_random_string(10)
    pyautogui.typewrite(message)
    pyautogui.typewrite(random_string)
    pyautogui.press('enter')


    


