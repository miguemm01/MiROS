import os
print("This script is only for Linux environments/Windows Subsystem For Linux environments")
x = input("Install MiROS development environment dependencies? y/n: ")

if(x == 'y'):
    username = input("Type your username: ")
    userinstall = "echo 'eval $(/home/linuxbrew/.linuxbrew/bin/brew shellenv)' >> /home/" + username + "/.profile"
    os.system("sudo apt update")
    os.system("sudo apt install build-essential")
    os.system("sudo apt install xorriso")
    os.system("sudo apt install grub-pc-bin")
    os.system("sudo apt install grub-common")
    os.system("/bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
    os.system(userinstall)
    os.system("sudo apt install libc6-dev")
    os.system("brew install gcc")
    os.system("brew link --overwrite gcc@5")
    os.system("brew unlink gcc@5 && brew link gcc@5")
    os.system("brew unlink gcc@5")
    os.system("brew link gcc")
    os.system("brew install x86_64-elf-gcc")
    os.system("brew link --overwrite x86_64-elf-binutils")
else:
    print("OK - Not installing")
    

