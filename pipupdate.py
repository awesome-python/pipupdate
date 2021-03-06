# PIPupdate 1.0
# (c) 2016 o355 under the GNU GPL 3.0

print("Welcome to PIPupdate (v1.0)")
print("Loading...")
#Declaring number vars
updatecountint = 0
updatenumber = 0
#Try/Except for proper handling of possible import errors
try:
    import sys
except ImportError:
    raise ImportError("Please install sys to use PIPupdate!")
try:
    import pip
except ImportError:
    # We ask for an input, and determine if the user wants PIP installed.
    # To keep things organized, we launch an external script that installs PIP for them.
    print("Shucks. PIP isn't installed. Would you like me to install PIP for you?")
    pipinstall = input("Yes or No: ").lower()
    if pipinstall == "yes":
        print("Alright. Installing PIP now!")
        exec(open("pipinstall.py").read())
    elif pipinstall == "no":
        print("Alright. Not installing PIP, exiting PIPupdate.")
        sys.exit()
    else:
        print("I couldn't understand what you inputted.")
        print("I'll assume you didn't want to install PIP, exiting now.")
        sys.exit()
try:
    from subprocess import call
except ImportError:
    print("Please install subprocess/subprocess call to use PIPupdate!")
    sys.exit()
try:
    from colorama import init, Fore, Style
except ImportError:
    print("Shucks. PIPupdate is dependent on Colorama to run. Would you like me to install Colorama for you?")
    coloramainstall = input("Yes or No: ").lower()
    if coloramainstall == "yes":
        print("Alright. Installing Colorama now!")
        pip.main(['install', 'colorama'])
        try:
            from colorama import init, Fore, Style
            print("Installed Colorama!")
        except ImportError:
            print("Colorama wasn't installed...")
            print("Please try running pip install colorama in a Python terminal.")
            sys.exit()
    elif coloramainstall == "no":
        print("Alright. You can also run the pipupdate-nocolor.py script (coming 1.0.1) if you don't want to install Colorama.")
        sys.exit()
    else:
        print("I couldn't understand what you inputted.")
        print("I'll assume you didn't want to install Colorama. Exiting now!")
        sys.exit()
init()
#Here we find out how many packages we need to install
for pkgname in pip.get_installed_distributions():
    updatenumber = updatenumber + 1
#Run the int -> str conversion for printing progress
updatenumberstr = str(updatenumber)
#Run the loop, and the updater does it's thing.
for pkgname in pip.get_installed_distributions():
    print(Fore.GREEN + Style.BRIGHT + "PIPupdate: Now attempting to update package " + pkgname.project_name + "..." + Style.RESET_ALL)
    updatecountint = updatecountint + 1
    updatecountstr = str(updatecountint)
    call("pip install --upgrade " + pkgname.project_name, shell=True)
    print(Fore.GREEN + Style.BRIGHT + "PIPupdate: Updated package " + pkgname.project_name + ". Progress: " + updatecountstr + "/" + updatenumberstr + " updates")

print(Style.RESET_ALL)
print("PIPupdate is done, updated " + updatecountstr + " packages!")
print("Thank you for using PIPupdate!")
