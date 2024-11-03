""" See License in the LICENSE.md
    See Guidelines in GuideLines.md
    Credits to cx_freeze. The exe is made with cx_freeze.
    Made with help from ChatGPT and Perplexity"""



import pyfiglet
import os
import webbrowser

currentpath = os.getcwd()

filepath = currentpath + r'\files'


os.system('title MultiHack - By Maxib226 and EpicNori')

# Generate ASCII art text using pyfiglet
ascii_art = pyfiglet.figlet_format(text='MultiHack', font='ansi_shadow')

# Define colors for the gradient
colors = [
    "\033[38;2;0;0;255m",    # Blue
    "\033[38;2;51;0;204m",   # Blueish Purple
    "\033[38;2;102;0;153m",  # Mid Blue-Purple
    "\033[38;2;153;0;153m",  # Purple
    "\033[38;2;179;0;153m",  # Light Purple
    "\033[38;2;204;0;204m"   # Pinkish Purple
]





#hier noch das mit dem loop für das Zeichen(<<<)text\code(>>>)

#Start Texte (anpassbar)

# Print each line with the corresponding color

print()
print('\033[38;2;0;0;255mWelcome to')
while True:
    print()
    print()
    for i, line in enumerate(ascii_art.splitlines()):
        if i < len(colors):  # Ensure we have enough colors
            print(f"{colors[i]}{line}")

    print()
    print()

    print("Your own hacking tool")


#Main


    command = input('''

        ╔(1) Internet options
        ║
        ╠═(2) cmd 
        ║
        ╠═══(3) Hacks (Not really)
        ║ 
        ╠════(4) Chat Room (pmp) 
        ║ 
        ╠══════(6) Restart    
        ║
        ╠═══════(7) Quit  
        ║
        ╚═══════>''')
    
    
    
    if command == '6':
        os.system(rf'start /min {filepath}\restart.py')   #restart command
        exit()
         
    elif command == '7':
            exit()

    elif command == '1': #internet subfolder
         os.system('cls')
         wifioptions = input('''

        ╔(1) Portscanner
        ║
        ╠══(2) Open URL
        ║
        ╠═══(3) Ip Scanner
        ║
        ╠════(4) Show Networks (only shows networks that the device ever connected to)
        ║
        ╠═════(5) Show network info (only works on networks that the device ever connected to)
        ║
        ╠══════(6) Go back 
        ║
        ╚════>''')
         
         if wifioptions == '6':
            pass

         elif wifioptions == '1':
             os.system("cls")
             os.system(rf'python {filepath}\portscanner.py')

         elif wifioptions == '3':
             os.system("cls")
             os.system(rf'python {filepath}\ipscanner.py')

         elif wifioptions == '2':
             os.system("cls")
             url = input("URL:")
             webbrowser.open(url)

         elif wifioptions == "4":
             os.system("cls")
             os.system("cmd /c netsh wlan show profile ")
             input()

         elif wifioptions == "5":
             os.system("cls")
             network = input("Network SSID:")
             os.system(f"cmd /c netsh wlan show profile {network} key=clear")
             input()

         else:
              print('Option not found.')
              input()
    
    elif command == '3':
        os.system('cls') #hacks subfolder
        hackoptions = input('''

            ╔(1) NeverClosingWindow
            ║
            ╠═(2) Spam Bot
            ║
            ╠══(3) Ip Logger prepare    
            ║
            ╠═══(4) Go back       
            ║
            ╚════>''')
        
        if hackoptions == '1':
             os.system(rf'start /min {filepath}\NeverClosingWindow.py')
        
        elif hackoptions == '2':
            os.system(rf'start {filepath}\pyspam.py')

        elif hackoptions == '3':
            os.system(rf'start {filepath}\Iploggerprepare.py')


        elif hackoptions == '4':
            pass
              
         
    elif command == '4':
        os.system('cls') #pmp subfolder
        chatroom = input('''

            ╔(1) Start PMP client
            ║
            ╠══(2) Start PMP Server      
            ║
            ╠═══(3) Go back  
            ║
            ╚═════>''')
       
        os.system('cls') 
        
        if chatroom == '1':
            os.system(rf'py {filepath}\pmp\pmp.py')

        elif chatroom == '2':
            os.system(rf'start  {filepath}\pmp\pmpserver.py')

        elif chatroom == '3':
            pass
            
       
    elif command == "2":
        os.system("cls")
        os.system("cmd")


    else:
        print('Option not found.')
        input()

    
    
    os.system('cls')



