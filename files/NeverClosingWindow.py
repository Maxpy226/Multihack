import os
import keyboard
import time

# Get the user's Downloads directory
downloads_dir = os.path.join(os.path.expanduser("~"), "Downloads")

# Define the path for the VBS file
vbs_file_path = os.path.join(downloads_dir, "do.vbs")

# VBS content (this is an example VBS script)
vbs_content = '''

do 
msgbox"Windows error",48,"Error"
loop

'''

# Write the VBS content to the file
with open(vbs_file_path, "w") as vbs_file:
    vbs_file.write(vbs_content)

print(f"VBS file has been created at: {vbs_file_path}")

os.system('start cmd')

time.sleep(0.5)
keyboard.write('cd ..',delay=0.10)
keyboard.send('enter')
keyboard.write('cd ..',delay=0.10)
keyboard.send('enter')
keyboard.write('cd downloads',delay=0.10)
keyboard.send('enter')
time.sleep(0.5)
keyboard.write('start do.vbs',delay=0.10)
keyboard.send('enter')
time.sleep(0.5)
keyboard.write('exit',delay=0.10)
keyboard.send('enter')

