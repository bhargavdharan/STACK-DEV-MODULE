# first we will import the subprocess module
import subprocess

# now we will store the profiles data in "data" variable by running the lst cmnd using subprocess.check_output
data = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')

# now we will store the profile by converting them to lst
profiles = [i.split(":")[1][1:-1] for i in data if "All user profile" in i]

# using for loop in python we are checking and printing the wifi pswds if they are available using the 2nd cmd 
for i in profiles:
    # running the 2nd cmd to check pswds
    results = subprocess.check_output(['netsh','wlan','show','profiles',i,'key=clear']).decode('utf-8').split('\n')

    # storing pswds after converting them to list
    results = [b.split(":")[1][1:-1] for b in results if "Key content" in b]

    # printing the profiles with their paswds using try and except method
    try:
        print("{:<30} | {:<}".format(i, results[0]))
    except IndexError:
        print("{:<30} | {:<}".format(i, ""))

