import os
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

time.sleep(1)
print("debug enabled file")
print(vbs_file_path)
print("current dir: ", os.getcwd())
os.system(f"start {vbs_file_path}")
print("started")

