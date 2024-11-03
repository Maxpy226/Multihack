import shutil
import os

currentpath = os.getcwd()
user = os.getlogin()
# Path to the source file
src = currentpath+r'\files\iplogger\Iplogger.py'
src2 = currentpath+r'\files\iplogger\loggersettings.json'
# Path to the destination (can be a directory or file path)
dst = currentpath+rf'\output\Iplogger.py'
dst2 = currentpath+rf'\output\loggersettings.json'


# Copy the file
shutil.copy(src, dst)
shutil.copy(src2, dst2)

input(r'Ip logger copied to \out dir')
